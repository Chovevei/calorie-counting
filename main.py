def find_elf_with_highest_calories(elves):
    highest_calories = 0

    for elf in elves:
        total_calories = 0
        for calories in elf:
            total_calories = total_calories + calories
            if highest_calories < total_calories:
                highest_calories = total_calories

    return highest_calories

with open('question.txt', 'r') as file:
    lines = file.readlines()
    elves = []
    current_elf = []

    for line in lines:
        line = line.strip()
        if len(line) > 0:
            current_elf.append(int(line))
        else:
            elves.append(current_elf)
            current_elf = []

print(find_elf_with_highest_calories(elves))