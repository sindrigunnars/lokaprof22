def file_to_dict(file_name, dict):
    for line in file_name:
        name, month, amount = line.strip().split(',')
        if name not in dict:
            dict[name] = [0 for _ in range(12)]
        dict[name][int(month)-1] += int(amount)

def months_to_dict(dict):
    months_not_null = {}
    for name in dict:
        if name not in months_not_null:
            months_not_null[name] = set()
        for i, v in enumerate(dict[name]):
            if v != 0:
                months_not_null[name].add(i)
    return months_not_null

def find_largest_intersection(dict):
    maximum = 0
    names = []
    for company in months:
        for company2 in months:
            if company != company2:
                intersection = months[company].intersection(months[company2])
                if maximum < len(intersection):
                    names = [company, company2]
                    maximum = len(intersection)
    print(f'{" & ".join(names)}: {maximum} months in common')

def print_summary(dict):
    for company in sorted(dict.keys()):
        print(f'{company}')
        print(f'Total: {sum(dict[company])}')
        for i, v in enumerate(dict[company]):
            print(f'\t{i+1}: {v}')

def print_highest(dict):
    totals = [[sum(i) for i in dict.values()], [i for i in dict]]
    highest = []
    for i, v in enumerate(totals[0]):
        if v == max(totals[0]):
            highest.append(totals[1][i])    
    print(f'Highest expenses:', ', '.join(sorted(highest)))

#--------- Main ---------
with open(input('Filename: ')) as file:
    expenses = {}
    file_to_dict(file, expenses)

print_summary(expenses)
print_highest(expenses)
if len(expenses.keys()) > 3:
    months = months_to_dict(expenses)
    find_largest_intersection(months)
    
