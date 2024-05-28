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