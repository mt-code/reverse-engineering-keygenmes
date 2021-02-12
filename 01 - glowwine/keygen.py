import random

target = 300

def generateKey():
    a = random.randint(48, 122)
    b = random.randint(48, 122)

    if target - (a + b) > 122 or target - (a + b) < 48:
        return generateKey()
    else:
        c = target - a - b

        return f"k@{chr(a)}{chr(b)}{chr(c)}"

print(generateKey())

