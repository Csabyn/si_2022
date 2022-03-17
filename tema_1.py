
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)  # declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)

my_list.sort()
print(my_list)  # afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_list.reverse()
print(my_list)  # afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

print(my_list[::2])  # afișează o listă ce conține numerele pare din lista ordonată (folosind slice)

print(my_list[1::2])  # afișează o listă ce conține numerele impare din lista ordonată (folosind slice)

print(my_list[1:5:3])  # afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)