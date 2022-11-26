def age_assignment(*args, **kwargs):
    people = {}
    for arg in args:
        first_letter = arg[0]
        if first_letter in kwargs:
            people[arg] = kwargs[first_letter]
    sorted_list = [f'{name} is {age} years old.' for name, age in sorted(people.items(), key=lambda x: x[0])]
    return '\n'.join(sorted_list)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))