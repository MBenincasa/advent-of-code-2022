"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.
The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.
The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
After the rearrangement procedure completes, what crate ends up on top of each stack?

"""

from io import TextIOWrapper
from queue import LifoQueue
import re

def getStacksGridAndCommansList(fileInput: TextIOWrapper):
    stacksInput, commands = fileInput.read().split("\n\n")
    stacksInputGrid = stacksInput.split("\n")
    commandsList = commands.split("\n")
    return stacksInputGrid, commandsList

def getNumStacks(stacksInputGrid: list[str]) -> int:
    return len(stacksInputGrid[len(stacksInputGrid) - 1].split())

def getLifoQueueList(nStacks: int):
    stacks = []
    for i in range(nStacks):
        stacks.append(LifoQueue())
    return stacks

def initializeStacks(stacksInputGrid, stacks):
    for rowGrid in reversed(stacksInputGrid):
        elementList = re.compile('(....?)').findall(rowGrid)
        print(elementList)
        for index, element in enumerate(elementList):
            if element[1] != ' ':
                stacks[index].put(element[1])
    return stacks

def runCommands(commandsList, stacks):
    for command in commandsList:
            commandSplitted = command.split()
            nMove = int(commandSplitted[1])
            stackFrom = int(commandSplitted[3])
            stackTo = int(commandSplitted[5])
            print(f"nMove: {nMove} - From: {stackFrom} to: {stackTo}")

            for i in range(nMove):
                e = stacks[stackFrom - 1].get()
                stacks[stackTo - 1].put(e)
    
    return stacks

def main() -> None:
    with open('../input.txt', 'r') as fileInput:
        stacksInputGrid, commandsList = getStacksGridAndCommansList(fileInput)
        nStacks = getNumStacks(stacksInputGrid)

        del(stacksInputGrid[len(stacksInputGrid) - 1])
        
        stacks = getLifoQueueList(nStacks)
        stacks = initializeStacks(stacksInputGrid, stacks)

        stacks = runCommands(commandsList, stacks)
        for index, stack in enumerate(stacks):
            print(f"Stack [{index + 1}]: {stack.get()}")

if __name__ == "__main__":
    main()