# Workout Logger API

API для ведения и отслеживания тренировок, реализованный с использованием FastAPI, SQLite и SQLAlchemy.

## Функционал

- Получение списка тренировок
- Фильтрация тренировок по категории
- Получение тренировки по ID
- Добавление новой тренировки
- Обновление тренировки
- Удаление тренировки
- Расчет общего количества сожженных калорий
- Поддержка pagination через query parameters (`limit`, `offset`)

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/workouts` | Получение списка тренировок |
| GET | `/workouts/category/{workout_category}` | Фильтрация по категории |
| GET | `/workouts/{workout_id}` | Получение тренировки по ID |
| POST | `/workouts` | Создание новой тренировки |
| PUT | `/workouts/{workout_id}` | Обновление тренировки |
| DELETE | `/workouts/{workout_id}` | Удаление тренировки |
| GET | `/workouts/{workout_id}/total-burned` | Расчет сожженных калорий |

## Технологии

- FastAPI
- SQLite
- SQLAlchemy
- Alembic
- Pydantic
- Docker
- Ruff
- uv
- Swagger / OpenAPI
- Postman

## Валидация

- `duration_minutes` > 0
- `burn_calories_per_minute` > 0
- `repeats` >= 0

Поддерживаемые категории:
- cardio
- strength
- stretching

## HTTP Status Codes

- `200 OK`
- `201 Created`
- `204 No Content`
- `404 Not Found`
- `422 Unprocessable Entity`

## Требования

- Docker

## Запуск через Docker

Сборка Docker image:

```bash
docker build -t workout-api .
```

Запуск контейнера:

```bash
docker run -p 8000:8000 workout-api
```

После запуска API будет доступен по адресу:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```