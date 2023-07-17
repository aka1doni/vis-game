import random
r = open("russian.txt", "r")
w = r.read()
d = w.split("\n")
global f
def f(x, y):
    z = random.randint(x, y)
    golga = d[z]
    return golga
