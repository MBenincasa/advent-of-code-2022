"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.
Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

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

            stackTemp = LifoQueue()
            for i in range(nMove):
                e = stacks[stackFrom - 1].get()
                stackTemp.put(e)
            
            while not stackTemp.empty():
                stacks[stackTo - 1].put(stackTemp.get())
    
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