my_dict = {'Alina': 28122003, 'Igor': 13092001}
print(my_dict)
print(my_dict['Alina'])
print(my_dict.get('Baby'))
my_dict.update({'Girl': 13092029,
                'Boy': 28122030})
del my_dict['Girl']
print(my_dict)
my_set = {'Alina', 'Igor', 'Girl', 'Boy', 'Girl', 'Boy'}
print(my_set)
my_set.update({'Baby', 'Puppy'})
list = my_set
print(list.discard('Puppy'))
print(list)