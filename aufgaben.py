strings = ["intro", "to", "list", "comps"]
# uppercase = []
# for string in strings:
#     string = string.upper()
#     uppercase.append(string)


uppercase = [string.upper() for string in strings]
print(uppercase)

nums = [1, 2, 3, 4, 5]
'''
funktion times_five, die jedes Element mit 5
eine neue Liste erstellen und mit den resultaten fülllen
mit normaler Schleife
'''

# def times_five(list):
#     result = []
#     for num in list:
#         num = num * 5
#         print("i " + str(num))  
#         result.append(num)
    
# times_five(nums)

def times_five(num):
    return num * 5
new_nums = [times_five(i) for i in nums]

print(new_nums)


'''
1.	Verwende eine for-Schleife:
	•	Iteriere über die Liste nums.
	•	Überprüfe, ob die Zahl gerade ist (d.h. ob die Zahl durch 2 teilbar ist).
	•	Falls die Zahl gerade ist, berechne das Quadrat dieser Zahl und füge es der Liste even_squares hinzu.
	•	Gib die Liste even_squares am Ende aus.
	2.	Verwende List Comprehension:
	•	Erstelle die gleiche Liste even_squares, aber diesmal mithilfe von List Comprehension.
	•	Gib die Liste even_squares am Ende aus.
'''
even_squares = []
for num in nums:
    if num%2 == 0:
        even_squares.append(num ** 2)

print(even_squares)

even_squares_compr = [num ** 2 for num in nums if num%2 == 0]
print(even_squares_compr)


muse = [{"song": "Do We Need This"}, {"song": "Escape"},{"song": "Verona"}]

songs = [i['song'] for i in muse]
print(songs)


'''
Aufgabe

Erstellt ein Python-Programm, das die folgenden Aufgaben erfüllt:

    Erstellen einer Liste von Quadratzahlen:
        Erstellt eine Liste der Quadratzahlen von 1 bis 10 mithilfe einer List Comprehension.

    Filtern von geraden Zahlen:
        Filtert die geraden Zahlen aus der Liste der Quadratzahlen mithilfe einer List Comprehension.

    Erstellen eines Wörterbuchs mit Wortlängen:
        Erstellt ein Wörterbuch, das die Wörter in einer Liste als Schlüssel und ihre Längen als Werte enthält.
        

Schritt-für-Schritt-Anleitung
1. Erstellen einer Liste von Quadratzahlen

Verwendet eine List Comprehension, um eine Liste der Quadratzahlen von 1 bis 10 zu erstellen.
2. Filtern von geraden Zahlen

Verwendet eine List Comprehension, um die geraden Zahlen aus der Liste der Quadratzahlen zu filtern.
3. Erstellen eines Wörterbuchs mit Wortlängen

Verwendet eine Dict Comprehension, um die Wörter in einer Liste als Schlüssel und ihre Längen als Werte zu speichern.

Probiert den Beispielcode aus und stellt sicher, dass ihr die Konzepte von List Comprehensions und Dictionary Comprehensions verstanden habt. Viel Spaß beim Programmieren!
Beispiel für die Ausgabe:

Quadratzahlen von 1 bis 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Gerade Quadratzahlen: [4, 16, 36, 64, 100]

Wortlängen: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}


'''
print('\nNew tasks')

squares = [num ** 2 for num in range(1, 11)]
print(squares)

squares_even = [square for square in squares if square%2==0]
print(squares_even)

tracks = ['Sunburn', 'Fillip', 'Cave', 'Showbiz', 'Unintended', 'Uno', 'Sober', 'Escape', 'Overdue']
word_lengths = {track: len(track) for track in tracks}
print(word_lengths)

tracks = ['Sunburn', 'Muscle Museum', 'Fillip', 'Cave', 'Showbiz', 'Unintended', 'Uno', 'Sober', 'Escape', 'Overdue']
word_lengths = {track: len(track) for track in tracks}
print(word_lengths)


'''
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []

for fruit in fruits:
    output.append(fruit.upper())
    

# Übung 1 - Schreibe den obigen Beispielcode unter Verwendung der List Comprehension-Syntax um. Erstelle eine Variable namens uppercased_fruits, um die Ausgabe der List Comprehension zu speichern. Die Ausgabe sollte ['MANGO', 'KIWI', etc...] sein.

# Übung 2 - Erstelle eine Liste, die jede Frucht mit mehr als 5 Zeichen enthält.

# Übung 3 - Erstelle eine Liste, die jede Frucht mit genau 5 Zeichen enthält.

# Übung 4 - Erstelle eine Liste, die die Anzahl der Zeichen in jeder Frucht enthält. Die Ausgabe wäre [5, 4, 10, etc...]

# Übung 5 - Erstelle eine Variable namens fruits_with_letter_a, die eine Liste nur der Früchte enthält, die den Buchstaben "a" enthalten.

# Übung 6 - Erstelle eine Variable namens even_numbers, die nur die geraden Zahlen enthält.

# Übung 7 - Erstelle eine Variable namens odd_numbers, die nur die ungeraden Zahlen enthält.

# Übung 8 - Erstelle eine Variable namens positive_numbers, die nur die positiven Zahlen enthält.

# Übung 9 - Erstelle eine Variable namens numbers_squared, die die Liste der Zahlen enthält, wobei jedes Element quadriert ist. Die Ausgabe lautet [4, 9, 16, etc...]

# Übung 10 - Erstelle eine Variable namens odd_negative_numbers, die nur die Zahlen enthält, die sowohl ungerade als auch negativ sind.

# Übung 11 - Erstelle eine Variable namens numbers_plus_5. Darin soll eine Liste zurückgegeben werden, die jede Zahl um fünf erhöht.
'''

print('\nNew tasks 2')
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

over_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(over_five_chars)

five_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(five_chars)

fruits_lengths = [len(fruit) for fruit in fruits]
print(fruits_lengths)

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

even_numbers = [num for num in numbers if num%2 == 0]
print(even_numbers)

odd_numbers = [num for num in numbers if num%2 != 0]
print(odd_numbers)

positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

odd_negative_numbers = [num for num in numbers if num < 0 and num%2 != 0]
print(odd_negative_numbers)

numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)