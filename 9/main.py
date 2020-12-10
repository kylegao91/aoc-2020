PRE = 25

if __name__ == '__main__':
    fin = open("input.txt")
    arr = []
    for line in fin:
        arr.append(int(line))
    fin.close()

    def find_wrong_idx():
        preamble = set(arr[:PRE])
        for i in range(PRE, len(arr)):
            found = False
            for x in preamble:
                if (arr[i] - x) in preamble:
                    found = True
                    break
            if not found:
                return i
            else:
                preamble.remove(arr[i - PRE])
                preamble.add(arr[i])
    
    wrong_idx = find_wrong_idx()
    wrong_num = arr[wrong_idx]
    print(wrong_num)

    accumulated = []
    sum_idx_map = {}
    for i in range(wrong_idx):
        if i == 0:
            accumulated.append(arr[i])
        else:
            accumulated.append(accumulated[i - 1] + arr[i])
        sum_idx_map[accumulated[i]] = i
    for left_idx in range(wrong_idx):
        right = wrong_num + accumulated[left_idx]
        if right in sum_idx_map:
            right_idx = sum_idx_map[right]
            break
    sub_arr = arr[left_idx:right_idx + 1]
    print(min(sub_arr) + max(sub_arr))