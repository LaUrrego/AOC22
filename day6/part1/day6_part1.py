with open("day6/input/input.txt") as file:
    for line in file:
        clean_line = line.strip()
    collection = []
    for position in range(len(clean_line)):
        working_sequence = [clean_line[position:position + 4]]
        counter = 0
        print(working_sequence)
        for letter in working_sequence[0]:
            print("current letter:", letter)
            if working_sequence[0].count(letter) == 1:
                counter += 1
                print("Added to counter, currently:", counter)
        if counter == 4:
            print("4 unique after: ", position + 5)
            print("Current position in list is: ", position + 1)
            collection.append([f"current position with unique: {position + 1}, so after {position + 4}", f"sequence is {working_sequence}"])

print(collection)

            
