# products_catalog = {
#     "Яблоки": {
#         "calories_per_100g": 52,
#         "items_in_package": 6
#     },
#     "Йогурт": {
#         "calories_per_100g": 85,
#         "items_in_package": 4
#     },
#     "Протеиновые батончики": {
#         "calories_per_100g": 410,
#         "items_in_package": 12
#     },
#     "Куринные яйца": {
#         "calories_per_100g": 155,
#         "items_in_package": 10
#     }
# }

# def add_product(catalog: dict, name: str, cals: int, items: int):
#     catalog.update({name: {"calories_per_100g": cals, "items_in_package": items}})

# add_product(products_catalog,
#             input("Введите название продукта: "),
#             int(input("Введите количество каллорий на 100г продукта: ")),
#             int(input("Введите кол-во предметов в упаковке: "))
#         )

# print(products_catalog)

new_set = set(range(100))

print(new_set)