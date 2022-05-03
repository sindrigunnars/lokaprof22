number = int(input())
numbers = []

while number >= 0:
    numbers.append(number)
    number = int(input())

print(' '.join([str(i) for i in sorted(numbers) if i%2 == 0]))