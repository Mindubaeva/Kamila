# TODO Найдите количество книг, которое можно разместить на дискете
number_of_pages = 100
number_of_str = 50
number_of_sym = 25
number_of_bite_book = 4
disk = 1.44
# 1Кб = 1024 байта
# 1Мб = 1024 Кб
# Объем дискеты:
fdd = disk * 1024 * 1024
# Объем книги:
book = number_of_pages * number_of_str * number_of_sym * number_of_bite_book
# Количество книг, которое можно поместить на дискету
number_of_book = fdd // book
number_of_book = int(number_of_book)

print("Количество книг, помещающихся на дискету:", number_of_book)
