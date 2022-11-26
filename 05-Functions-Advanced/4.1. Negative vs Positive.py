def find_sum(*args):
    positive_sum, negative_sum = 0, 0
    for num in args:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num
    return positive_sum, negative_sum


numbers = [int(x) for x in input().split()]
positive_sum, negative_sum = find_sum(*numbers)
print(negative_sum)
print(positive_sum)
if positive_sum > abs(negative_sum):
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')
