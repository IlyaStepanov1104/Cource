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

## Архитектура

- **`lessons.json`** — единственный источник данных курса. Занятие скрыто до наступления `date` (добавь `?view_all=true` в URL для предпросмотра).
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
