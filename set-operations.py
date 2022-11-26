print("Please enter a set of numbers:")
theset = set(map(int, input().split(" ")))
numofcom = int(input("and the number of commands that you want to do: "))
print("Please enter the commands in this format with space-> \"command number\" \nCommands: pop, remove, discard")
for i in range(numofcom):
    command= input().split(" ")
    if len(command)==2:
        if command[0]=="remove":
            theset.remove(int(command[1]))
        else:
            theset.discard(int(command[1]))
    else:
        theset.pop()
    print(f"updated: {theset}")
print(f"the total: {sum(theset)}")
