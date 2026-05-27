# Workout Logger API

API для ведения и отслеживания тренировок, реализованный с использованием FastAPI, SQLite и SQLAlchemy.

## functions

- Получение списка тренировок
- Фильтрация тренировок по категории
- Получение тренировки по ID
- Добавление новой тренировки
- Обновление существующей тренировки
- Удаление тренировки
- Расчет общего количества сожженных калорий

## endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/workouts` | Получение списка тренировок |
| GET | `/workouts/category/{workout_category}` | Фильтрация по категории |
| GET | `/workouts/{workout_id}` | Получение тренировки по ID |
| POST | `/workouts` | Создание новой тренировки |
| PUT | `/workouts/{workout_id}` | Обновление тренировки |
| DELETE | `/workouts/{workout_id}` | Удаление тренировки |
| GET | `/workouts/{workout_id}/total-burned` | Расчет сожженных калорий |

## stack

- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Swagger / OpenAPI
- Postman

## validation

- `duration_minutes` > 0
- `burn_calories_per_minute` > 0
- `repeats` >= 0
- Поддерживаемые категории:
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

- Python 3.14.5

## Установка и запуск

Виртуального окружения:

```bash
python -m venv .venv
```

Активация виртуального окружения:

Linux / macOS:

```bash
source .venv/bin/activate
```

## Для линукс: 'activate'  может меняться в зависимости от вашего терминала если у вас fish то будет activate.fish и тд.


Windows:

```bash
.venv\Scripts\activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск приложения:

```bash
fastapi dev
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## Скриншот Swagger UI

![Swagger](swagger.png)