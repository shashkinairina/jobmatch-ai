// JobMatch AI - Frontend логика

const API_URL = "http://localhost:8000";

const demoButton = document.getElementById("demo-btn");
const matchButton = document.getElementById("match-btn");
const userInput = document.getElementById("user-input");
const resultsDiv = document.getElementById("results");

// Демо-режим
if (demoButton) {
    demoButton.addEventListener("click", () => {
        const demoResults = [
            {
                title: "Продакт-менеджер",
                company: "VK",
                description: "Управление продуктом, CustDev, A/B-тесты, юнит-экономика",
                match_percent: 85,
                matched_skills: ["custdev", "a/b", "юнит-экономика", "метрики"]
            },
            {
                title: "Аналитик данных",
                company: "Avito",
                description: "SQL, Python, анализ данных, визуализация",
                match_percent: 72,
                matched_skills: ["a/b", "аналитика", "воронка"]
            },
            {
                title: "Маркетолог / Performance-маркетолог",
                company: "Ozon",
                description: "Контекстная реклама, email-маркетинг, аналитика кампаний",
                match_percent: 58,
                matched_skills: ["воронка", "конверсия"]
            }
        ];
        renderResults(demoResults);
    });
}

// Реальный поиск
if (matchButton) {
    matchButton.addEventListener("click", async () => {
        const text = userInput.value.trim();
        
        if (!text) {
            resultsDiv.innerHTML = '<p style="color: #ff6b6b; text-align: center;">Введите описание вашего опыта</p>';
            return;
        }

        resultsDiv.innerHTML = '<p style="text-align: center; color: #888;">Подбираем вакансии...</p>';

        try {
            const response = await fetch(API_URL + "/match", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error("Server error: " + response.status);
            }

            const data = await response.json();
            const vacancies = data.vacancies || [];

            if (vacancies.length === 0) {
                resultsDiv.innerHTML = '<p style="text-align: center; color: #888;">Не найдено совпадений. Попробуйте описать опыт подробнее — укажите навыки, инструменты, технологии.</p>';
            } else {
                renderResults(vacancies);
            }

        } catch (error) {
            resultsDiv.innerHTML = 
                '<p style="text-align: center; color: #ff6b6b;">Не удалось подключиться к серверу.</p>' +
                '<p style="text-align: center; color: #888; font-size: 14px;">Убедитесь, что сервер запущен: python3 -m uvicorn server:app --port 8000</p>' +
                '<p style="text-align: center; color: #888; font-size: 14px;">Или попробуйте демо-режим.</p>';
        }
    });
}

function renderResults(vacancies) {
    if (vacancies.length === 0) {
        resultsDiv.innerHTML = '<p style="text-align: center; color: #888;">Ничего не найдено</p>';
        return;
    }

    let html = "";
    vacancies.forEach(v => {
        const percent = v.match_percent;
        let barColor = "#4ecdc4";
        if (percent >= 70) barColor = "#51cf66";
        else if (percent >= 40) barColor = "#fcc419";
        else barColor = "#ff922b";

        const skillsHtml = v.matched_skills && v.matched_skills.length > 0
            ? '<div style="margin-top: 10px;">' + 
              v.matched_skills.map(s => '<span style="background: #2d2d3f; color: #a4a4b4; padding: 4px 10px; border-radius: 12px; font-size: 12px; margin-right: 5px; display: inline-block; margin-bottom: 5px;">' + s + '</span>').join("") +
              '</div>'
            : "";

        html += 
            '<div style="background: #1a1a2e; border-radius: 12px; padding: 20px; margin-bottom: 16px; border: 1px solid #2d2d3f;">' +
                '<div style="display: flex; justify-content: space-between; align-items: start;">' +
                    '<div>' +
                        '<h3 style="color: #fff; margin: 0 0 5px 0; font-size: 18px;">' + v.title + '</h3>' +
                        '<p style="color: #888; margin: 0 0 10px 0; font-size: 14px;">' + v.company + '</p>' +
                        '<p style="color: #a4a4b4; margin: 0; font-size: 14px;">' + v.description + '</p>' +
                        skillsHtml +
                    '</div>' +
                    '<div style="text-align: center; min-width: 70px;">' +
                        '<div style="font-size: 28px; font-weight: bold; color: ' + barColor + ';">' + percent + '%</div>' +
                        '<div style="font-size: 11px; color: #666;">совпадение</div>' +
                    '</div>' +
                '</div>' +
                '<div style="margin-top: 12px; background: #2d2d3f; border-radius: 6px; height: 6px; overflow: hidden;">' +
                    '<div style="width: ' + percent + '%; height: 100%; background: ' + barColor + '; border-radius: 6px; transition: width 0.5s;"></div>' +
                '</div>' +
            '</div>';
    });

    resultsDiv.innerHTML = html;
}
