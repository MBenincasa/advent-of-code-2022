"""
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""

with open('../input.txt', 'r') as fileInput:
    Lines = fileInput.readlines()

    list = []

    sum = 0
    for line in Lines:
        i = line.strip()

        if i != '':
            sum += int(i)
            print(f"i: {i} - sum: {sum}")
        else:
            list.append(sum)
            print(f"list: {list}")
            sum = 0

    list.sort(reverse=True)
    print(f"list reverse sorted: {list}")
    
    result = list[0] + list[1] + list[2]
    print(f"result: {result}")