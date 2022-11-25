parentheses_string = input()
is_balanced = True
opening_parentheses = ['(', '{', '[']
closing_parentheses = [')', '}', ']']
parentheses = {
    '(': ')',
    '{': '}',
    '[': ']'
}
stack = []
for el in parentheses_string:
    if el in opening_parentheses:
        stack.append(el)
    elif not stack:
        is_balanced = False
        break
    elif el in closing_parentheses:
        if el == parentheses[stack[-1]]:
            stack.pop()
        else:
            is_balanced = False
            break
if is_balanced:
    print('YES')
else:
    print('NO')