expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_index = int(stack.pop())
        end_index = i
        result = expression[start_index:end_index+1]
        print(result)
