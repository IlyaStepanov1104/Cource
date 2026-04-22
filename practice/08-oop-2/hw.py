# Создать класс Book с атрибутами title, author, year, pages. Реализовать методы: 
# is_new() - вышла ли книга за последние 5 лет, 
# short_info() - строка вида 'Толстой - Война и мир (1869)'. 
# Добавить __str__ и __eq__ (две книги равны, если совпадают автор и название). 


# Создать список из 3-4 книг и вывести только новые.


class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        
    def is_new(self):
        return self.year > 2021
        
    def short_info(self):
        return f"{self.author} - {self.title} ({self.year})"
    
    def __str__(self):
        return self.short_info()
    
    def __eq__(self, other) -> bool:
        return self.title == other.title and self.author == other.author and self.year == other.year and self.pages == other.pages
    
    
books = [
    Book("Война и мир", "Толстой", 1869, 1225),
    Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, 223),
    Book("Обломов", "Гончаров", 1859, 432),
    Book("Обломов", "Гончаров", 2025, 200)
]

for book in books:
    if book.is_new():
        print(book)
