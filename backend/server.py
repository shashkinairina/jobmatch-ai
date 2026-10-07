from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatchRequest(BaseModel):
    text: str

VACANCIES = [
    {
        "title": "Продакт-менеджер",
        "company": "VK",
        "skills": ["продакт", "продукт", "custdev", "cust dev", "a/b", "ab тест", "a/b тест", "юнит-экономика", "unit", "метрики", "аналитика", "дорожная карта", "roadmap", "бэклог", "пользователь", "mvp", "прототип", "исследование", "воронка", "конверсия", "ретеншн", "retention", "churn", "ltv", "cac", "mau", "dau"],
        "description": "Управление продуктом, CustDev, A/B-тесты, юнит-экономика"
    },
    {
        "title": "UX/UI Дизайнер",
        "company": "Yandex",
        "skills": ["дизайн", "figma", "фигма", "ux", "ui", "прототип", "прототипирование", "интерфейс", "wireframe", "макет", "дизайн-система", "user journey", "навигация", "компоненты", "анимация", "иллюстрация"],
        "description": "Проектирование интерфейсов, Figma, дизайн-системы"
    },
    {
        "title": "Аналитик данных",
        "company": "Avito",
        "skills": ["sql", "python", "питон", "tableau", "аналитик", "данные", "data", "статистика", "pandas", "numpy", "визуализация", "dashboard", "дашборд", "excel", "гипотеза", "воронка", "когортный", "ab тест", "a/b", "бд", "база данных", "etl", "airflow"],
        "description": "SQL, Python, анализ данных, визуализация"
    },
    {
        "title": "Маркетолог / Performance-маркетолог",
        "company": "Ozon",
        "skills": ["маркетинг", "маркетолог", "реклама", "контекст", "контекстная", "email", "рассылка", "таргет", "трафик", "roi", "romi", "cpa", "cpc", "ctr", "кампания", "продвижение", "seo", "sem", "соцсети", "smm", "лидогенерация", "воронка", "конверсия", "a/b", "бюджет", "яндекс директ", "google ads"],
        "description": "Контекстная реклама, email-маркетинг, аналитика кампаний"
    },
    {
        "title": "Frontend-разработчик",
        "company": "Tinkoff",
        "skills": ["javascript", "js", "react", "vue", "angular", "frontend", "фронтенд", "html", "css", "typescript", "ts", "вёрстка", "верстка", "dom", "api", "redux", "webpack", "sass", "scss", "tailwind", "node", "компонент", "spa"],
        "description": "JavaScript, React, TypeScript, вёрстка"
    },
    {
        "title": "Backend-разработчик",
        "company": "Sber",
        "skills": ["python", "django", "flask", "fastapi", "backend", "бэкенд", "api", "rest", "sql", "postgres", "postgresql", "redis", "docker", "kubernetes", "микросервис", "sqlalchemy", "orm", "celery", "база данных", "бд", "etl", "golang", "java", "c++"],
        "description": "Python, REST API, базы данных, микросервисы"
    },
    {
        "title": "Project-менеджер",
        "company": "Yandex",
        "skills": ["проект", "project", "менеджер", "agile", "scrum", "kanban", "jira", "трекинг", "планирование", "команда", "стейкхолдер", "milestone", "риск", "бюджет", "ресурс", "спринт", "ретроспектива", "standup"],
        "description": "Управление проектами, Agile, Scrum, Jira"
    },
    {
        "title": "Data Scientist",
        "company": "MTS",
        "skills": ["python", "ml", "machine learning", "машинное обучение", "data science", "дата сайенс", "numpy", "pandas", "scikit", "tensorflow", "pytorch", "модель", "нейросеть", "нейронная", "алгоритм", "регрессия", "классификация", "кластер", "nlp", "компьютерное зрение", "cv", "feature", "признак", "обучение"],
        "description": "ML, Python, нейросети, анализ данных"
    },
    {
        "title": "QA-инженер / Тестировщик",
        "company": "Avito",
        "skills": ["тест", "тестирование", "qa", "автотест", "selenium", "pytest", "unittest", "bug", "баг", "дефект", "тест-кейс", "api", "ручное тестирование", "автоматизация", "нагрузка", "regression", "smoke", "postman", "devtools"],
        "description": "Тестирование, автотесты, Selenium, Postman"
    },
    {
        "title": "Mobile-разработчик (iOS)",
        "company": "VK",
        "skills": ["swift", "swiftui", "ios", "xcode", "mobile", "мобайл", "iphone", "ipad", "objective-c", "uikit", "combine", "coredata", "react native", "flutter"],
        "description": "Swift, iOS, Xcode, мобильная разработка"
    },
    {
        "title": "Mobile-разработчик (Android)",
        "company": "Ozon",
        "skills": ["kotlin", "java", "android", "android studio", "mobile", "мобайл", "jetpack", "compose", "gradle", "rxjava", "coroutines", "react native", "flutter"],
        "description": "Kotlin, Android, мобильная разработка"
    },
    {
        "title": "DevOps-инженер",
        "company": "Sber",
        "skills": ["devops", "ci/cd", "docker", "kubernetes", "terraform", "ansible", "jenkins", "gitlab", "linux", "bash", "aws", "облако", "cloud", "микросервис", "мониторинг", "prometheus", "grafana", "nginx", "helm", "argocd"],
        "description": "Docker, Kubernetes, CI/CD, мониторинг"
    },
    {
        "title": "HR-менеджер",
        "company": "Tinkoff",
        "skills": ["hr", "рекрутинг", "найм", "кадры", "персонал", "собеседование", "интервью", "оценка", "адаптация", "онбординг", "мотивация", "удержание", "корпоративная культура", "компенсация", "грейд"],
        "description": "Рекрутинг, адаптация, корпоративная культура"
    },
    {
        "title": "Контент-менеджер / Редактор",
        "company": "Yandex",
        "skills": ["контент", "редактор", "копирайтер", "копирайтинг", "текст", "статья", "seo", "семантика", "редактура", "корректура", "инфографика", "медиа", "блог", "соцсети", "телеграм", "контент-план"],
        "description": "Контент, копирайтинг, редактура"
    },
    {
        "title": "Финансовый аналитик",
        "company": "MTS",
        "skills": ["финансы", "финансовый", "анализ", "excel", "модель", "бюджет", "прогноз", "отчёт", "отчет", "p&l", "баланс", "cash flow", "инвестиция", "npv", "irr", "ebitda", "контроллинг", "юнит-экономика", "cac"],
        "description": "Финансовое моделирование, P&L, бюджетирование"
    }
]

def calculate_match(user_text, vacancy):
    text_lower = user_text.lower().strip()
    skills = vacancy["skills"]
    matched = []
    for skill in skills:
        s = skill.lower()
        if s in text_lower:
            matched.append(skill)
    if len(matched) == 0:
        return 0, []
    denominator = min(len(skills), 6)
    match_percent = min(100, int((len(matched) / denominator) * 100))
    return match_percent, matched


@app.post("/match")
async def match_vacancies(request: MatchRequest):
    user_text = request.text
    results = []
    for vacancy in VACANCIES:
        percent, matched_skills = calculate_match(user_text, vacancy)
        if percent > 0:
            results.append({
                "title": vacancy["title"],
                "company": vacancy["company"],
                "description": vacancy["description"],
                "match_percent": percent,
                "matched_skills": matched_skills
            })
    results.sort(key=lambda x: x["match_percent"], reverse=True)
    return {"vacancies": results}
