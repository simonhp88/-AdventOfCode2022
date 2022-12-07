with open('Day 1/input.txt') as file:
    elf_food = file.read()
calories=[]
for food in elf_food.split("\n\n"):
    elf_total=0
    for item in food.split("\n"):
        elf_total=elf_total+int(item)
    calories.append(elf_total)
print(sorted(calories)[-1])
print((sorted(calories)[-1]+sorted(calories)[-2]+sorted(calories)[-3]))