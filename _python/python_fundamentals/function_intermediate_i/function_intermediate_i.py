import random

def randInt(min=0, max=100):
    num = random.randint(min, max)
    return num


print(randInt(min=50, max=500))