numbers = [1, 2, 3, 4]
check = lambda x, y: x if x > y else y
def find_max(numbers, check):
    max = numbers[0]
    for i in numbers:
        max = check(max, i)
    return max
print(find_max(numbers, check))