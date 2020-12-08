if __name__ == '__main__':
    fin = open("input.txt")
    ops = []
    for line in fin:
        line = line.strip()
        cmd, arg = line.split(" ")
        ops.append([cmd, int(arg)])
    fin.close()

    def loop_or_terminate(ops):
        i = 0
        visited = set()
        accelerator = 0
        terminate = False
        while 0 <= i < len(ops) and i not in visited:
            visited.add(i)
            cmd, arg = ops[i]

            if cmd == 'acc':
                accelerator += arg
            if cmd == 'jmp':
                i += arg
            else:
                i += 1

            if i == len(ops):
                terminate = True
                break

        return terminate, accelerator
    
    for j in range(len(ops)):
        if ops[j][0] in ['jmp', 'nop']:
            tmp = ops[j][0] 
            ops[j][0] = 'jmp' if tmp == 'nop' else 'nop'
            terminate, accelerator = loop_or_terminate(ops)
            if terminate:
                break
            ops[j][0] = tmp