#1:
def print_params(a = 1, b ='строка', c = True):
    print(a, b, c)
print_params(1, 2, 3)
print_params()
print_params(b = 25)            # Проверил, работает
print_params(c = [1,2,3])       # Проверил, работает
#2:
values_list = [1, 'Правда', True]
values_dict = {'a' : 2, 'b' : 'строчка', 'c' : False}
print_params(*values_list)
print_params(**values_dict)
#3:
values_list_2 = (1, 'Два')
print_params(*values_list_2, 42)   # Проверил, работает
