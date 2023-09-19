s = input("Input string with brackets")
opcl = {")":"(","]":"[","}":"{"}
brackets = "()[]{}"
stack = []
valid = True

for i in s:
    if i in brackets:
        if i not in opcl:
            stack.append(i)
            continue
        if not stack or stack[-1]!=opcl[i]:
            valid = False
            break
        else:
            stack.pop()


if valid == True and not stack:
    print("valid")
else:
    print("invalid")
