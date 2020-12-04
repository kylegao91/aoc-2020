def valid1(mini, maxi, ch, password):
    count = 0
    for c in password:
        if c == ch:
            count += 1
    return mini <= count <= maxi

def valid2(i, j, ch, password):
    return (password[i - 1] == ch) != (password[j - 1] == ch)

if __name__ == '__main__':
    fin = open("input.txt")
    count = 0
    for line in fin:
        i, left = line.split("-")
        i = int(i)
        j, left, password = left.split(" ")
        j = int(j)
        ch = left[0]

        if valid2(i, j, ch, password):
            count += 1
    print(count)
