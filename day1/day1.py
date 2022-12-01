with open("input1.txt") as file:
    model = []
    next = 0
    for line in file:
        if line in ("\n", "\r\n"):
            model.append(next)
            next = 0
        else:
            next += int(line.strip())
    new_list = sorted(model)

    print(new_list[-1] + new_list[-2] + new_list[-3])
