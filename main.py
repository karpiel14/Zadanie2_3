import random
names=['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
firstLetters=[name[0] for name in names]
print("Pierwsze litery: ")
print(firstLetters)
numbers = [[random.randint(1,10) for i in range(4)] for j in range(5)]
print("Piecoelementowa lista zawierajaca 4 listy, w ktorych jest po 4 elementy: ")
print(numbers)