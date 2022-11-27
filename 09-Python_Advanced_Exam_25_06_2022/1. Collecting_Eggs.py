from collections import deque


def is_wrapped(current_egg, current_paper, boxes):
    result = current_egg + current_paper
    current_boxes = boxes
    if result <= 50:
        current_boxes += 1
        return current_boxes
    return boxes


eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]
boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    current_paper = papers.pop()
    boxes = is_wrapped(current_egg, current_paper, boxes)

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(x) for x in papers])}')
