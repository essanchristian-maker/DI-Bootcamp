#Exercice 4

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        throws += 1
        if die1 == die2:
            return throws

def main():
    results = [throw_until_doubles() for _ in range(100)]

    total   = sum(results)
    average = total / len(results)

    print(f"Results after 100 doubles:")
    print(f"   Total throws          : {total}")
    print(f"   Average throws/double : {average:.2f}")
    print(f"   Fastest double        : {min(results)} throw(s)")
    print(f"   Slowest double        : {max(results)} throw(s)")

main()