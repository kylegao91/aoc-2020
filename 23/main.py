N = 1000000
M = 10000000

# N = 9
# M = 100

class Node():

    def __init__(self, num):
        self.num = num
        self.next = None

def wrap(i, n):
    if i == 0:
        return n
    elif i < 0:
        return i % n
    else:
        return i

if __name__ == '__main__':

    fin = open("input.txt")
    input_nums = [int(ch) for ch in fin.readline().strip()]
    fin.close()

    nums = {}   # num -> node
    prev = None
    for n in input_nums + list(range(10, N + 1)):
        node = Node(n)
        nums[n] = node
        if prev is not None:
            prev.next = node
        prev = node
    current = nums[input_nums[0]]
    prev.next = current

    for it in range(M):
        next_three = set()
        p = current
        for _ in range(3):
            p = p.next
            next_three.add(p.num)

        diff = 1
        dst_num = wrap((current.num - diff), N)
        while dst_num in next_three:
            diff += 1
            dst_num = wrap((current.num - diff), N)
        dst = nums[dst_num]

        temp = current.next
        current.next = p.next
        p.next = dst.next
        dst.next = temp

        current = current.next
    
    res = []
    p = nums[1]
    for _ in range(2):
        p = p.next
        res.append(p.num)
    print(res)
