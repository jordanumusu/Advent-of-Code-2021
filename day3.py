def solve():
    report = open("day3.txt", "r")

    i = 12
    gr = "000000000000"
    zeroes = 0
    ones = 0
    while (i > 0):
        temp = report.readline()
        if temp == "":
            i -= 1
            if zeroes > ones:
                gr += "0"
            elif ones > zeroes:
                gr += "1"
            zeroes = 0
            ones = 0
        else:
            if temp[12-i] == "0":
                zeroes += 1
            elif temp[12-i] == "1":
                ones += 1

    print(gr)
    print(int(gr, 2) * ((int(gr, 2) << 12) - 1 - 12))
    report.close()


solve()
