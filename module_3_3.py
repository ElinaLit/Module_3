#Задача_1: Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(6)
print_params('космос')
print_params(b = 25)
print_params(c = [1, 2, 3])

#Задача_2: Распаковка параметров:
value_list = [3, 'медведя', False]
values_dict = {'a' : 1, 'b' : 'Маша', 'c' : True}
print_params(*value_list)
print_params(**values_dict)

#Задача_3: Распаковка + отдельные параметры:
values_list_2 = [3.14, 'число π – ']
print_params(*values_list_2, 'математическая постоянная')




