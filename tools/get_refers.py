import random
def random_refers():
    refers = open("tools/refers.txt", "r").read().splitlines()
    return random.choice(refers)