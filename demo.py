numbers = []
for _ in range(int(input("How many numbers to enter in: "))):
    number = int(input("Number: "))
    numbers.append(number)
sortedlist = sorted(numbers)
cleaList = [i for i in sortedlist if sortedlist.count(i) != 2]
print (cleaList)