with open("day4/input/input.txt") as file:
    total_match = 0
    for line in file:
        clean_line = line.strip()
        elf1, elf2 = clean_line.split(",")
        split = elf1.split("-")
        elf1_range = [x for x in range(int(split[0]),int(split[1]) + 1)]
        split = elf2.split("-")
        elf2_range = [x for x in range(int(split[0]),int(split[1]) + 1)]
        pair = [elf1_range, elf2_range]
        sorted_pair = sorted(pair, key=len)
        print(sorted(pair, key=len))
        in_count = 0
        match = 0
        for item in sorted_pair[0]:
            if item in sorted_pair[1]:
                print("The matching numbers are:", item)
                in_count += 1
        print("count is:", in_count)
        if in_count > 0:
            match += 1
        print("There was any match:", match)
        total_match += match
        print("Match so far is:", total_match)
print("Final count is:", total_match)