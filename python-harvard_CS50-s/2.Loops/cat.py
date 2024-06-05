""" 
First task

i = 0
while i < 3:
    print("meow")
    i += 1
"""

"""
Second task

for i in range(7):
    print("meow")
"""

"""
Third task

print("meow\n" *3, end="")
"""

"""
Fourth task

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whats' n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()