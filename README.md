# JobMatch AI

Сервис подбора вакансий на основе описания опыта работы. Пользователь вводит описание своих навыков — система анализирует текст и подбирает подходящие вакансии с процентом совпадения.

## Технологии

- **Backend:** FastAPI, Python
- **Frontend:** HTML, CSS, JavaScript
- **Контейнеризация:** Docker, Docker Compose

## Запуск через Docker

```bash
docker-compose up --build
```

- Фронтенд: http://localhost:8080
- API: http://localhost:8000

## Запуск без Docker

```bash
pip install -r requirements.txt
uvicorn backend.server:app --port 8000
```

Открыть `frontend/index.html` в браузере.

## API

### POST /match

Принимает описание опыта работы, возвращает топ-6 подходящих вакансий.

**Запрос:**
```json
{ "text": "работаю аналитиком данных, пишу на Python и SQL" }
```

**Ответ:**
```json
{
  "vacancies": [
    {
      "title": "Аналитик данных",
      "company": "Avito",
      "description": "SQL, Python, анализ данных, визуализация",
      "match_percent": 67,
      "matched_skills": ["sql", "python", "аналитик", "данные", "дашборд"]
    }
  ]
}
```

## Как работает матчинг

Текст пользователя приводится к нижнему регистру и проверяется на вхождение ключевых навыков из базы вакансий. Процент совпадения = совпавшие навыки / максимум 6 ключевых навыков.

