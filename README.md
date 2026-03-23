# Статический сайт для курса с занятиями, презентациями и домашними заданиями

## Структура директорий

```
├── index.html              # Главная страница — список занятий
├── lessons.json            # Данные курса (редактировать для добавления занятий)
├── style.css               # Общие стили
├── vite.config.js          # Dev-сервер
├── utils/                  # Reveal.js и шрифты (скопировано из lectures/utils)
├── package.json
│
└── lessons/                # Материалы занятий
    └── 01-intro/           # Занятие 1: Введение
        └── presentations/  # Презентации к занятию
            └── 1-intro/    # Презентация 1
                ├── index.html
                └── css-custom/
                    └── custom.css
```

## Запуск локального сервера

```bash
cd cources
npm install
npm run dev
```

## Редактирование курса — lessons.json

Весь контент курса хранится в `lessons.json`. Структура:

```json
{
  "course": {
    "title": "Название курса",
    "subtitle": "Описание"
  },
  "lessons": [
    {
      "number": 1,
      "title": "Название занятия",
      "date": "2026-03-19T10:00:00",
      "presentations": [
        {
          "title": "Название презентации",
          "link": "/lessons/01-intro/presentations/1-intro/",
          "order": 1
        }
      ],
      "homeworks": [
        {
          "title": "Краткое название задания",
          "description": "Развёрнутое описание (необязательно)",
          "link": "https://classroom.github.com/...",
          "deadline": "2026-03-26T23:59:59"
        }
      ]
    }
  ]
}
```

### Поля занятия

| Поле | Обязательное | Описание |
|-|-|-|
| `number` | + | Номер занятия (для сортировки и отображения) |
| `title` | + | Название занятия |
| `date` | + | ISO дата начала занятия — до наступления скрыто |
| `presentations` | — | Массив презентаций (может быть пустым) |
| `homeworks` | — | Массив ДЗ (может быть пустым или отсутствовать) |

### Поля презентации

| Поле    | Описание |
|-|-|
| `title` | Название |
| `link` | Путь к `index.html` или внешняя ссылка |
| `order` | Порядок в списке |

### Поля домашнего задания

| Поле          | Описание |
|-|-|
| `title`  Короткое название |
| `description` | Расширенное описание (необязательно) |
| `link` | Ссылка на GitHub Classroom, форму, задачник и т.д. |
| `deadline` | ISO дата дедлайна (необязательно) |

## Добавление нового занятия

### 1. Добавить запись в lessons.json

```json
{
  "number": 2,
  "title": "Тема занятия",
  "date": "2026-03-26T10:00:00",
  "presentations": [],
  "homeworks": []
}
```

### 2. Создать директорию занятия

```
lessons/
└── 02-topic-name/
    └── presentations/
        └── 1-topic/
            ├── index.html        ← скопировать из 01-intro/presentations/1-intro/
            └── css-custom/
                └── custom.css    ← скопировать и адаптировать
```

### 3. Создать презентацию

Скопируйте `lessons/01-intro/presentations/1-intro/` в новую директорию и:

- Измените `<title>` в `<head>`
- Измените содержимое слайдов
- Адаптируйте `css-custom/custom.css` при необходимости

### 4. Обновить lessons.json

Добавьте ссылку на новую презентацию в массив `presentations`:

```json
{
  "title": "Название презентации",
  "link": "/lessons/02-topic-name/presentations/1-topic/",
  "order": 1
}
```

## Добавление нескольких презентаций к занятию

```json
"presentations": [
  {
    "title": "Теория",
    "link": "/lessons/02-topic/presentations/1-theory/",
    "order": 1
  },
  {
    "title": "Практика",
    "link": "/lessons/02-topic/presentations/2-practice/",
    "order": 2
  }
]
```

## Шаблон презентации

`lessons/01-intro/presentations/1-intro/index.html` — полноценная первая презентация,
которую можно использовать как шаблон для последующих занятий.

**Основные классы слайдов:**

| Класс | Назначение |
|-------|---|
| `.title-slide` | Оформление титульного слайда |
| `.plan-list` | Нумерованный список плана занятия |
| `.topic-grid` / `.topic-card` | Сетка тем курса |
| `.grade-table` | Таблица оценивания |
| `.contact-block` / `.contact-row` | Блок контактов |

**Вспомогательные стили:**

| Класс/тег | Эффект |
|-----------|---|
| `<mark>` | Синяя подсветка |
| `<mark class="green">` | Зелёная подсветка |
| `<mark class="yellow">` | Жёлтая подсветка |
| `.muted` | Серый цвет текста |
| `pre.size-s / size-m / size-l` | Размер кода |

### Типы слайдов

| Тип | Шаблон |
|---|---|
| Раздел на фоне | `<section data-background-image="img/bg.jpg"><h1 style="text-shadow: #000 3px 2px 2px;">Текст</h1></section>` |
| Плюсы/минусы | `<ul class="opinion"><li class="plus fragment">...</li><li class="minus fragment">...</li></ul>` |
| Сравнение двух подходов | `.compare` > `.compare-block` (2-column grid) |
| Простой код | `<pre class="[html\|css\|javascript] size-l code-example-one"><code>...</code></pre>` |
| HTML + CSS вместе | `<code-example [fragment] [no-preview]><template data-type="html">...</template><template data-type="css">...</template></code-example>` |
| Грид инструментов | `.tools-list` > `.tool-block` |
| Временная шкала | `.timeline` > `.timeline-item` > `.timeline-label` + `.timeline-arrow` + `.timeline-desc` |
| Схема архитектуры | `.arch-flow` > `.arch-box[.highlight]` + `.arch-arrow` |
| Слайды в формате MD | `<section data-markdown data-separator="---"><script type="text/template">...markdown...</script></section>` |

Общие компоненты доступны из `/utils/css/custom-base.css` автоматически: `.opinion`, `.compare`/`.compare-block`, `.tools-list`/`.tool-block`, `.timeline`/`.timeline-item`, `.arch-flow`/`.arch-box`, `.wrapper`, `.iframe-container`.

`css-custom/custom.css` — только для стилей, уникальных для данной лекции.

## Горячие клавиши в презентации

| Клавиша | Действие |
|---------|---|
| `→` / `Space` | Следующий слайд |
| `←` | Предыдущий слайд |
| `F` | Полноэкранный режим |
| `S` | Режим докладчика |
| `O` | Обзор слайдов |
| `?` | Список всех горячих клавиш |
