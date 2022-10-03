file = open('thai_food.txt', 'r')
for each in file:
    print(each)
file.close()

file = open('hungarian_food.txt', 'w')
file.write("1 Gulyas")
file.write("2 Porkolt")
file.close()

file = open('hungarian_food.txt', 'r')
for each in file:
    print(each)
file.close()

with open('thai_food.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
