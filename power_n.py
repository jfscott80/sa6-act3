numbers = [1,2,3,4]
def power_of_n(a, n):
    result = list(map(lambda x: x**n, a))
    return result
print(power_of_n(numbers, 2))