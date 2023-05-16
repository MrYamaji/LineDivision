# Figure area calculator / Программа подсчета площади фигур
# Figure types: circle, square, triangle, rectangle / Типы фигур: круг, квадрат, треугольник, прямоугольник

fig = input("Enter your figure type \\\n Введите тип вашей фигуры: ").lower()

if fig == "circle" or fig == "круг":
    r = float(input("Enter the radius of the circle \\\n Введите радиус вашего круга: "))
    S = 3.14 * (r ** 2)
    print(f"Area of your circle \\\n Площадь вашего круга: {S}")

elif fig == "square" or fig == "квадрат":
    a = float(input("Enter the first side of your figure \\\n Введите первую сторону вашей фигуры: "))    
    S = a ** 2
    print(f"Area of your square \\\n Площадь вашего квадрата: {S}")

elif fig == "rectangle" or fig == "прямоугольник":
    a = float(input("Enter the first side of your figure \\\n Введите первую сторону вашей фигуры: "))
    b = float(input("Enter the second side of your figure \\\n Введите вторую сторону вашей фигуры: "))
    S = a * b
    print(f"Area of your rectangle \\\n Площадь вашего прямоугольника: {S}")

elif fig == "triangle" or fig == "треугольник":
    a = float(input("Enter the first side of your figure \\\n Введите первую сторону вашей фигуры: "))
    b = float(input("Enter the second side of your figure \\\n Введите вторую сторону вашей фигуры: "))
    c = float(input("Enter the third side of your figure \\\n Введите третью сторону вашей фигуры: "))
    p = (a + b  + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Area of your triangle \\\n Площадь вашего треугольника: {S}")

else:
    print("Error, you entered incorrect data \\\n Ошибка, вы ввели не правильные данные")