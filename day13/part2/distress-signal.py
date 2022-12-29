"""
--- Part Two ---

Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.
The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.
For the example above, the result of putting the packets in the correct order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]

Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are 10th and 14th, and so the decoder key is 140.
Organize all of the packets into the correct order. What is the decoder key for the distress signal?

"""

from functools import cmp_to_key

def compare(left, right) -> int:
    if not isinstance(left, list):
        left = [left]

    if not isinstance(right, list):
        right = [right]

    for i in range(min(len(left), len(right))):
        if isinstance(left[i], list) or isinstance(right[i], list):
            result = compare(left[i], right[i])
            if result != 0:
                return result
        elif left[i] < right[i]:
            return -1
        elif left[i] > right[i]:
            return 1

    if len(left) < len(right):
        return -1

    if len(left) > len(right):
        return 1

    return 0

def main() -> None:
    with open('../input.txt', 'r') as fileInput:

        packets = []
        for block in fileInput.read().split("\n\n"):
            left_list, right_list = block.splitlines()
            left_list, right_list = eval(left_list), eval(right_list)

            packets.append(left_list)
            packets.append(right_list)

        d1 = [[2]]
        d2 = [[6]]
        packets.extend([d1, d2])

        packets = sorted(packets, key = cmp_to_key(compare))
        print(f"The decoder key is: {(packets.index(d1) + 1) * (packets.index(d2) + 1)}")

if __name__ == "__main__":
    main()