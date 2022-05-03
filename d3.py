numbers = '3 1 2 3 4 5 6 7 8 9'.split()
DIM = int(numbers[0])
numbers = [str(i) for i in numbers[1:]]

def make_2d(DIM, numbers):
    matrix = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index+DIM]
        index += DIM
        matrix.append(row)
    return matrix

def display(list):
    strings = []
    for i in range(DIM):
        strings.append(' '.join(list[i]))
    print('\n'.join(strings))

def printing(list1, list2):
    strings = []
    for i in range(DIM):
        strings.append(' '.join(list1[i]) + ' | ' + ' '.join(list2[i]))
    print('\n'.join(strings))
    

def mirror_list(numbers):
    return [[i for i in j[::-1]] for j in numbers]

org = make_2d(DIM, numbers)
mirr = mirror_list(org)
display(org)
printing(org, mirr)

