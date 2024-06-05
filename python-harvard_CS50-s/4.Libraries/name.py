import sys as s

if len(s.argv)<2:
    s.exit("Too few argument")

for arg in s.argv[1:]:
    print("hello, my name is", arg)
