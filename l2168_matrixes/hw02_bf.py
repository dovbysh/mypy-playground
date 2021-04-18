bf = input()

tape = [0] * 30000
pos = 0

for i in range(0, len(bf)):
    if bf[i] == ">":
        pos += 1
        if pos >= len(tape):
            pos = 0
    elif bf[i] == "<":
        pos -= 1
        if pos < 0:
            pos = len(tape) - 1
    elif bf[i] == "+":
        tape[pos] += 1
        if tape[pos] > 255:
            tape[pos] = 0
    elif bf[i] == "-":
        tape[pos] -= 1
        if tape[pos] < 0:
            tape[pos] = 255
    elif bf[i] == ".":
        print(tape[pos])
