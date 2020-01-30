s = input()
p = input()

p_reversed = ""
for char in p:
    if char.isdigit() is False:
        if char.isupper():
            p_reversed = p_reversed + char.lower()
        else:
            p_reversed = p_reversed + char.upper()
    else:
        p_reversed = p_reversed + char

if s == p:
    # P and S are identical;
    print("Yes")
elif s[0].isdigit() and s[1:] == p:
    # S can be formed from P by prepending a single digit (0–9);
    print("Yes")
elif s[-1].isdigit() and s[:-1] == p:
    print("Yes")
elif p_reversed == s:
    print("Yes")
else:
    print("No")
