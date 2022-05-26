import pickle

class example_class:                                         # класс    
    print('Ты меня сериализовал')

class another_example:
    def add(x, y):
        return x + y

my_object = example_class                                    # объект класса
my_pickled_object = pickle.dumps(my_object)                  # сериализация объекта класса
new_func = pickle.loads(my_pickled_object)                   # функция, использующая сериализованный объект
new_func()                                                   # вызов функции, которая использует сериализованный объект

my_another_abject = another_example                                   # объект класса
my_another_pickled_object = pickle.dumps(my_another_abject.add(4, 5)) # сериализация функции класса
new_variable = pickle.loads(my_another_pickled_object)                # загрузка сериализованной функции в переменную
print(new_variable)                                                   # Вывод результата                