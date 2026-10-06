# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Что это

Статический сайт курса индивидуальных занятий по программированию. Главная страница (`index.html`) подгружает `lessons.json` и рендерит карточки занятий с презентациями и домашними заданиями. Презентации строятся на [Reveal.js](utils/js/reveal.js).

## Команды

```bash
npm install   # один раз
npm run dev   # dev-сервер на http://localhost:8001
```

Сборки нет — сайт полностью статический, Vite используется только как dev-сервер.

## Потоки (табы)

На сайте два независимых потока, переключаются табами на главной и в админке (`?track=ege`):

| Поток | Данные | Презентации | Практика | Расписание |
|---|---|---|---|---|
| Программирование | `lessons.json` | `lessons/<NN-slug>/` | `practice/<NN-slug>/` | вс 11:00 (60) / пн 18:00 (90) |
| ЕГЭ | `ege.json` | `lessons-ege/<NN-slug>/` | `practice-ege/<NN-slug>/` | вт 19:00 (60) |

Нумерация занятий в каждом потоке своя. Правила генерации презентаций и практики для ЕГЭ те же, что для программирования. Список потоков задан константой `TRACKS` в `index.html` и `admin/index.html`, файлы для сохранения - `TRACK_FILES` в `vite.config.js`.

## Оплата

Общий счётчик по обоим потокам ведёт админка. Оплаты лежат в `payments.json` (`{ "payments": [{ "date", "lessons", "note" }] }`, файл в `.gitignore` - только локально), добавляются кнопкой «+ Оплата». Занятия обоих потоков с даты первой оплаты идут по порядку дат и по очереди списывают оплаченные уроки; в шапке - сколько осталось, на карточке - сколько останется к этому занятию (2 и меньше - пора платить).

## Архитектура

- **`lessons.json`** / **`ege.json`** — источники данных потоков. Занятие скрыто до наступления `date` (добавь `?view_all=true` в URL для предпросмотра).
- **`index.html`** — вся логика главной страницы встроена в `<script>`: fetch → renderLessons → DOM-генерация карточек.
- **`lessons/<NN-slug>/presentations/<N-slug>/index.html`** — каждая презентация самодостаточна, использует Reveal.js из `/utils/`.
- **`utils/`** — общий Reveal.js, шрифты, стили. Пути абсолютные (`/utils/...`), поэтому обязательно нужен dev-сервер.

## Структура презентации

Шаблон — `lessons/01-intro/presentations/1-intro/index.html`.

Каждая презентация подключает:
1. `/utils/css/reveal.css` + тему
2. `/utils/css/custom-base.css` — общие компоненты (`.opinion`, `.compare`, `.tools-list`, `.timeline`, `.arch-flow`)
3. `css-custom/custom.css` — стили, уникальные для данной лекции

Кастомный веб-компонент `<code-example>` рендерит живой HTML+CSS preview прямо на слайде.

## Добавление занятия

1. Добавить запись в `lessons.json`.
2. Создать `lessons/<NN-slug>/presentations/<N-slug>/`, скопировав из `01-intro/presentations/1-intro/`.
3. Обновить `presentations` в `lessons.json` с правильным `link`.

## Полезные классы слайдов

| Класс | Назначение |
|---|---|
| `.title-slide` | Титульный слайд |
| `.plan-list` | Нумерованный план |
| `.compare` / `.compare-block` | Два столбца для сравнения |
| `.tools-list` / `.tool-block` | Грид инструментов |
| `.timeline` / `.timeline-item` | Временная шкала |
| `.arch-flow` / `.arch-box` | Схема архитектуры |
| `<mark>` / `<mark class="green\|yellow">` | Подсветка текста |
| `pre.size-s\|size-m\|size-l` | Размер блока кода |
