from math import pi, sin, tan, cos

def reverse_polish_notation(notation: str) -> float:
    stack = []
    tokens = notation.split() 

    for token in tokens:
        if token not in ["+", "-", "*", "/", "^", "sin", "tan", "cos"]:
            if token == "pi":
                stack.append(pi)
            else:
                stack.append(float(token))
        else:
            if token in ["sin", "tan", "cos"]:
                num = stack.pop()
                match token:
                    case "sin":
                        stack.append(sin(num))
                    case "tan":
                        stack.append(tan(num))
                    case "cos":
                        stack.append(cos(num))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match token:
                    case "+":
                        stack.append(num2 + num1)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num2 * num1)
                    case "/":
                        stack.append(num2 / num1)
                    case "^":
                        stack.append(num2 ** num1)

    return stack[0]

# took the test notations from https://leachlegacy.ece.gatech.edu/revpol/
# degrees are converted into radians

print(reverse_polish_notation("2 5 * 4 + 3 2 * 1 + /"))
print(reverse_polish_notation("5 8 pi 6 / sin * + 2 pi 4 / tan + /"))
print(reverse_polish_notation("pi 3 / cos 8 * 4 0.5 ^ 3 * 1 - /"))
