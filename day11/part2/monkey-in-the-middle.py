"""
--- Part Two ---

You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.
Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.
At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.

After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.
Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

"""

from collections import deque
from dataclasses import dataclass
from typing import Callable

@dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]
    test_divisible: int
    if_true: int
    if_false: int
    inspected_items: int

def parse_monkey(monkey_block):
    lines = monkey_block.splitlines()
    items = deque(map(int, lines[1].split(": ")[1].split(", ")))
    operation = lines[2].split("= ")[1]
    operation = eval(f"lambda old: {operation}")
    test_divisible = int(lines[3].split(" ")[-1])
    if_true = int(lines[4].split(" ")[-1])
    if_false = int(lines[5].split(" ")[-1])

    return Monkey(items, operation, test_divisible, if_true, if_false, 0)

def main() -> None:
    with open('../input.txt', 'r') as file_input:
        monkeys = []
        div = 1
        
        for monkey_block in file_input.read().split("\n\n"):
            monkey = parse_monkey(monkey_block)
            div *= monkey.test_divisible
            monkeys.append(monkey)

        for _ in range(10000):
            for monkey in monkeys:
                while len(monkey.items) > 0:
                    item = monkey.items.popleft()
                    item = monkey.operation(item) % div

                    next_monkey = monkey.if_true if item % monkey.test_divisible == 0 else monkey.if_false
                    monkeys[next_monkey].items.append(item)

                    monkey.inspected_items += 1

        inspected_items = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)
        print(f" The level of monkey business is: {inspected_items[0] * inspected_items[1]}")

if __name__ == "__main__":
    main()