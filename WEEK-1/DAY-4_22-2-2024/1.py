# Approach - 1

s = input()
s1 = set(s)
if len(s1) == 27:
    print("Pangram")
else:
    print("Not a Pangram")

