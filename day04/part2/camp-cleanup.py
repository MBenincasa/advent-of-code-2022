"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.
In how many assignment pairs do the ranges overlap?

"""

def main() -> None:
    with open('../input.txt', 'r') as fileInput:
        lines = fileInput.readlines()

        tot = 0
        for line in lines:
            lineSplitted = line.split(',')
            p1, p2 = lineSplitted[0], lineSplitted[1]
            print(f"p1: {p1} - p2: {p2}")
            partOneSplitted = p1.split('-')
            p1s1, p1s2 = int(partOneSplitted[0]), int(partOneSplitted[1])
            partTwoSplitted = p2.split('-')
            p2s1, p2s2 = int(partTwoSplitted[0]), int(partTwoSplitted[1])

            if ((p1s2 >= p2s1 and p1s2 <= p2s2) or (p2s2 >= p1s1 and p2s2 <= p1s2)):
                tot+=1
            print(f"Live total: {tot}")
                
        print(f"Total total: {tot}")

if __name__ == "__main__":
    main()