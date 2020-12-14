import math

def ext_euclid(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r # remainder
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_s, old_t, old_r

def solve_linear_modular_eq(a, b, n):
    """ Solve ax = b (mod n) 
        Returns c, m s.t. x = c (mod m)
    """
    print(f"Solving: {a}x = {b} (mod {n})")
    r, _, d = ext_euclid(a, n)
    if b % d != 0:
        return None
    m = n // d
    c = (r * b // d) % m
    return c, m

def solve_linear_modular_eq_list(a, b, n):
    prev_m = [1]
    prev_c = [0]
    for ai, bi, ni in zip(a, b, n):
        aa = math.prod(prev_m) * ai

        temp = 0
        for j in range(len(prev_c) - 1, 0, -1):
            temp = prev_m[j - 1] * (temp + prev_c[j])

        bb = (bi - ai * temp) % ni
        c, m = solve_linear_modular_eq(aa, bb, ni)
        prev_c.append(c)
        prev_m.append(m)

    m = 1
    c = 0
    for i in range(len(prev_c) - 1, 0, -1):
        m = prev_m[i] * m
        c = prev_m[i - 1] * (c + prev_c[i])
    return m, c

if __name__ == '__main__':
    fin = open("input.txt")
    start = int(fin.readline())
    schedule = [int(x) if x != 'x' else 'x' for x in fin.readline().strip().split(",")]
    fin.close()

    min_wait = None
    bus_id = None
    for s in schedule:
        if s == 'x':
            continue
        wait = (s - start % s)
        if min_wait is None:
            min_wait = wait
            bus_id = s
        elif wait < min_wait:
            min_wait = wait
            bus_id = s
    print(min_wait * bus_id)

    # Solve linear modular equations
    # s_0 * x = s_i - i (mode s_i)
    #   where s_i is the interval of bus_i and i in 0..#buses
    a = []
    b = []
    n = []
    for i, s in enumerate(schedule[1:]):
        if s != 'x':
            a.append(schedule[0])
            b.append(s - i - 1)
            n.append(s)
    m, c = solve_linear_modular_eq_list(a, b, n)
    print(schedule[0] * c)