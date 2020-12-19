OPS = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y
}
PRE = {
    '*': 1,
    '+': 2
}

def tokenize(st):
    fields = st.split(" ")
    tokens = []
    for f in fields:
        remain = f
        while remain[0] == '(':
            tokens.append('(')
            remain = remain[1:]
        right = []
        while remain[-1] == ')':
            right.append(')')
            remain = remain[:-1]
        if remain not in OPS:
            remain = int(remain)
        tokens.append(remain)
        tokens += right
    return tokens

def evaluate(exp):
    op_stack = []
    num_stack = []
    for tok in exp:
        print(op_stack, num_stack, tok)
        if isinstance(tok, int):
            num_stack.append(tok)
        elif tok in OPS:
            while op_stack and op_stack[-1] in OPS and PRE[op_stack[-1]] >= PRE[tok]:
                right = num_stack.pop()
                left = num_stack.pop()
                op = op_stack.pop()
                num_stack.append(OPS[op](left, right))
            op_stack.append(tok)
        elif tok == '(':
            op_stack.append(tok)
        elif tok == ')':
            while op_stack and op_stack[-1] in OPS:
                right = num_stack.pop()
                left = num_stack.pop()
                op = op_stack.pop()
                num_stack.append(OPS[op](left, right))
            op_stack.pop()
    while op_stack:
        right = num_stack.pop()
        left = num_stack.pop()
        op = op_stack.pop()
        num_stack.append(OPS[op](left, right))
    return num_stack[-1]


if __name__ == '__main__':
    total = 0
    fin = open("input.txt")
    for line in fin:
        print(line)
        result = evaluate(tokenize(line.strip()))
        print(result)
        total += result
    fin.readline()
    print(total)
