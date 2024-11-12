# TODO Найдите количество книг, которое можно разместить на дискете
info_cap = 1.44
pages = 100
rows = 50
symbols = 25
weight = 4
info_cap_in_bytes = info_cap * 1024 * 1024
books = round(info_cap_in_bytes // (weight * symbols * rows * pages))
print("Количество книг, помещающихся на дискету:", books)
