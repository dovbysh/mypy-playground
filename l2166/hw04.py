i = input().split()
# i="-5 -8 + 9 2 4 - 0 1 3 * + + - -".split()
stack = []
for o in i:
    try:
        stack.append(int(o))
    except ValueError:
        b = stack.pop()
        a = stack.pop()
        if o == "+":
            stack.append(a + b)
        elif o == "-":
            stack.append(a - b)
        elif o == "*":
            stack.append(a * b)

print(stack.pop())
