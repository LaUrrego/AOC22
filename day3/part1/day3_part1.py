import string
letter_band = [string.ascii_letters]
priority_sum = 0
with open("day3/input/input.txt") as file:
    for line in file:
        clean_line = line.strip()
        section1 = clean_line[:len(clean_line) // 2]
        section2 = clean_line[len(section1):]
        print(letter_band)
        print("section1:", section1)
        print("section2:", section2)
        common = set()
        for letter in section1:
            if letter in section2:
                common.add(letter)
        letter = list(common)[0]
        print(letter)
        priority = letter_band[0].index(letter) + 1
        priority_sum += priority
        print("letter is:", letter)
        print("priority is: ", priority)
        print("current priority sum: ", priority_sum)
print(priority_sum)
            

        
    