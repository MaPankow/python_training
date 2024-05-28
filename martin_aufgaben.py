'''
Aufgabe 1: List Comprehension
Aufgabe: Schreibe eine List Comprehension, die die Quadrate aller geraden Zahlen von 0 bis 20
erzeugt.
'''
square_even = []
for i in range (0, 21):
    if i%2 == 0:
        i = i ** 2
        square_even.append(i)

print(square_even)

square_even_compr = [num ** 2 for num in range(0, 21) if num%2 == 0]
print(square_even_compr)


'''
Aufgabe 2: Dictionary Comprehension
Aufgabe: Erstelle ein Dictionary, das die Zahlen von 1 bis 10 als Schlüssel und ihre Quadrate als
Werte enthält.
'''

# nums_and_squares = [{1: 1}, {2: 4}, {3: 9}, {4: 16}, {5: 25}, {6: 36}, {7: 49}, {8: 64}, {9: 81}, {10: 100}]
nums_and_squares = {}
for num in range(1, 11):
    nums_and_squares[num] = num ** 2

print(nums_and_squares)

nums_squares_compr = {num: num ** 2 for num in range(1, 11)}
print(nums_squares_compr)
'''
Aufgabe 3: Iteration über ein Dictionary
Aufgabe: Schreibe ein Python-Skript, das über ein Dictionary von Produkten und ihren Preisen
iteriert und die Produkte mit einem Preis über 50 in ein neues Dictionary speichert.
'''

products = {"Laptop": 999, "Mouse": 25, "Keyboard": 45, "Monitor": 150}

# print(products)
# print(products['Laptop'])

# for product in products:
    
#     if products[product] > 50:
#         print(products[product])


products_over_50 = {product: products[product] for product in products if products[product] > 50}
print(products_over_50)


'''
Kombination von Iteration und Comprehension
Aufgabe: Schreibe ein Programm, das eine Liste von Zahlen filtert und die Quadrate der geraden
Zahlen berechnet, wobei du sowohl eine for-Schleife als auch eine List Comprehension
verwendest.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_square_even = [num ** 2 for num in numbers if num%2 == 0]
print(numbers_square_even)

even_odd = [num for num in numbers if num%2 == 0]
print(even_odd)