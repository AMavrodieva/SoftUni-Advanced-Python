from collections import deque
main_color = ["red", "yellow", "blue"]
secondary_color = ["orange", "purple", "green"]
string = deque(input().split())
collected_color = []
while string:
    left = string.popleft()
    right = string.pop() if string else ""
    attempt = left + right
    if attempt in main_color or attempt in secondary_color:
        collected_color.append(attempt)
        continue
    attempt = right + left
    if attempt in main_color or attempt in secondary_color:
        collected_color.append(attempt)
        continue
    left = left[0:-1]
    right = right[0:-1]
    if left:
        string.insert((len(string)//2), left)
    if right:
        string.insert((len(string) // 2), right)

result = []

forming_color = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
for color in collected_color:
    if color in forming_color:
        if forming_color[color][0] in collected_color and forming_color[color][1] in collected_color :
            result.append(color)
            continue
    else:
        result.append(color)
print(result)
