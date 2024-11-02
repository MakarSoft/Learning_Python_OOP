# 03_03.py

import inspect


class Foo:
    def bar(self):
        pass

    def baz(self):
        pass


method_list = inspect.getmembers(Foo, predicate=inspect.ismethod)
print(method_list)  # []
print()

method_list = inspect.getmembers(Foo, predicate=inspect.isfunction)
print(
    *method_list, sep="\n"
)  # [('bar', <function Foo.bar at 0x7f18b0d3f2e0>), ('baz', <function Foo.baz at 0x7f18b0d3eb60>)]
print()

method_list = inspect.getmembers(
    Foo, predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x)
)
print(*method_list, sep="\n")
print()

foo_instance = Foo()
method_list = inspect.getmembers(foo_instance, predicate=inspect.ismethod)
print(*method_list, sep="\n")  # Выведет список методов экземпляра
print()


# Методы в классе:
# Когда вы определяете методы в классе, они становятся методами только тогда,
# когда вы обращаетесь к ним через экземпляр класса.
# В классе Foo методы bar и baz являются обычными функциями, когда вы смотрите
# на них через Foo.__dict__.
# inspect.ismethod проверяет, является ли объект методом, но в данном случае,
# когда вы вызываете inspect.getmembers(Foo, predicate=inspect.ismethod),
# вы проверяете методы на уровне самого класса, а не экземпляра.
# Поскольку в классе Foo методы bar и baz являются функциями, а не методами,
# проверка не проходит, и вы получаете пустой список.
#
# Использование экземпляра класса:
# Если вы хотите получить методы класса, вам нужно создать экземпляр класса и
# затем использовать inspect.getmembers на этом экземпляре.
# foo_instance = Foo()
# method_list = inspect.getmembers(foo_instance, predicate=inspect.ismethod)

items = inspect.getmembers(Foo)  # список кортежей (name, object)
for item in items:
    print(type(item))

    name, object = item
    if inspect.ismethod(object):
        print(f"Method: {name}, {object}")
    elif inspect.isfunction(object):
        print(f"Function: {name}, {object}")
    else:
        print(f"Not a method: {name}, {object}")

#  При ссылке на метод как на атрибут класса вы теперь получаете простой
# объект функции.


methods = inspect.getmembers(
    Foo, predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x)
)
print(*methods)
