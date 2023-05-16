# Line division \ Деление строк пополам

text = input("Введите вашу строку для деления: ")

a = text[:(len(text)+1) // 2]
b = text[(len(text)+1) // 2 :]
print(f"Получаем строчки {b}\n {a}")
