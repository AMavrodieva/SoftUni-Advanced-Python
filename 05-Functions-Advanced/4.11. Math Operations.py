def math_operations(*args, **kwargs):
    from collections import deque
    queue = deque(args)
    while queue:
        if queue:
            first_element = queue.popleft()
            kwargs['a'] += first_element
        if queue:
            second_element = queue.popleft()
            kwargs['s'] -= second_element
        if queue:
            third_element = queue.popleft()
            if third_element != 0:
                kwargs['d'] /= third_element
        if queue:
            fourth_element = queue.popleft()
            kwargs['m'] *= fourth_element

    sorted_result = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
