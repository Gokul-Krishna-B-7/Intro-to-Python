numbers=(1,2,3,4,5,3,4,3)
#numbers[0]=2 this is not possible because unlike lists items, tuple items are immutable
print(numbers.count(3))
print(numbers.index(3))
