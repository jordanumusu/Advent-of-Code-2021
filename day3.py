def solve():
    report = open("day3.txt", "r")

    i = 0
    gr = ""
    er = ""
    zeroes = 0
    ones = 0
    data = report.readlines()
    print(data[0])
    while (i < 12):
        for j in range(len(data)):
            if data[j][i] == "0":
                zeroes+=1
            elif data[j][i] == "1":
                ones+=1
        if zeroes > ones:
            gr += "0"
            er += "1"
        elif zeroes < ones:
            gr += "1"
            er += "0"
        zeroes = 0
        ones = 0
        i+=1
    print(gr)
    print(er)
    print(int(gr, 2) * int(er, 2))
    report.close()


solve()
