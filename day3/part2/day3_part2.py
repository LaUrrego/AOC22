import string
letter_band = [string.ascii_letters]
priority_sum = 0
with open("day3/input/input.txt") as file:
    input_list = []
    for line in file:
        clean_line = line.strip()
        input_list.append(clean_line)
    groups = [input_list[n:n + 3] for n in range(0,len(input_list), 3)]
    for group in groups:
        common = set()
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:
                common.add(letter)
                print("common letter:", common)
        print("final common:", common)
        priority = letter_band[0].index(list(common)[0]) + 1
        priority_sum += priority
        print("priority: ", priority)
        print("current priority sum:", priority_sum)
        print("--------------")
print("Final sum:", priority_sum)
        
                


   