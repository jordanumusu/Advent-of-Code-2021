def solve():
    report = open("day1.txt","r")
    data = report.read().splitlines()
    data = list(map(int,data))
    count = 0
    j = 3
    i = 0
    prevMes = 0
    while j < len(data):
        prevMes = sum(data[i:j])
        i+=1
        j+=1
        if (sum(data[i:j]) - prevMes > 0):
            count+=1
    print(count)
    report.close()
solve()