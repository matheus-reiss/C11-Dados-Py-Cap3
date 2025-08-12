loja1 = {"iPhone 15", "Samsung Galaxy S23", "Xiaomi 13", "iPhone 11"}
loja2 = {"Samsung Galaxy S23", "Xiaomi 13", "iPhone 15", "iPhone 10"}

todos_modelos = loja1 | loja2
print("Modelos disponíveis no total:", todos_modelos)

modelos_comuns = loja1 & loja2
print("Modelos disponíveis em ambas as lojas:", modelos_comuns)