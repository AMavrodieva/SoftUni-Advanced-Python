n = int(input())
best_intersection = set()
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    current_interaction = first_set.intersection(second_set)
    if len(current_interaction) > len(best_intersection):
        best_intersection = current_interaction

print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")

