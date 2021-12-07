def solve():
    commands = open("day2.txt","r")
    horPos = 0
    aim = 0
    depth = 0
    for line in commands:
        command = line.split()
        if command[0] == "forward":
            horPos += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim+= int(command[1])
        elif command[0] == "up":
            aim-= int(command[1])
    print(horPos * depth) 
    commands.close()

solve()