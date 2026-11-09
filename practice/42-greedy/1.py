def choose_lessons(lessons: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    ordered = sorted(lessons, key=lambda lesson: lesson[2])
    selected = []

    last_end = '00:00'

    for lesson in ordered:
        name, start, end = lesson
        if start >= last_end:
            selected.append(lesson)
            last_end = end
    
    return selected



lessons = [
    ("Рисование", "08:00", "10:00"),
    ("Английский", "08:30", "10:30"),
    ("Математика", "10:00", "11:00"),
    ("Информатика", "10:30", "11:30"),
    ("Музыка", "11:00", "12:00"),
]

print(choose_lessons(lessons))