# In python, function is a group related statements that perform a specific task.

sum = 0


def fun(a, b):
    sum = a + b
    return sum


c = fun(4, 3)
print(c)


# lamda expression
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

# Finding the Adults
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)