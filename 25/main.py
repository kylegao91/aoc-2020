SUBJECT = 7
MODE = 20201227

class Loop:

    def __init__(self, subject, mode):
        self.subject = subject
        self.mode = mode

        self.val = 1
        self.loop_size = 0

    def next(self):
        self.val = (self.val * self.subject) % self.mode
        self.loop_size += 1
        return self.val

def get_loop_size(key):
    loop = Loop(SUBJECT, MODE)
    while loop.val != key:
        loop.next()
    return loop.loop_size

if __name__ == '__main__':
    card_pub_key = 6270530
    door_pub_key = 14540258
    
    card_loop_size = get_loop_size(card_pub_key)
    decryp = Loop(door_pub_key, MODE)
    for _ in range(card_loop_size):
        decryp.next()
    print(decryp.val)