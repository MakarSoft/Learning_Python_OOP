from types import FunctionType, MethodType


class Foo:
    def bar(self):
        pass

    def baz(self):
        pass


def methods(cls) -> list[str]:
    return [
        name
        for name, val in cls.__dict__.items()
        if isinstance(val, MethodType)  # or isinstance(val, FunctionType)
    ]


def methods1(cls) -> list[str]:
    return [
        name
        for name, val in cls.__dict__.items()
        if isinstance(val, FunctionType)
    ]


print(methods(Foo))  #  -> []
print(methods1(Foo))  # -> ['bar', 'baz']

# почему функция methods(Foo) возвращает пустой список,
# а methods1(Foo) возвращает имена методов.
#
# Причины:
# Типы методов в классе:
# Когда вы определяете методы в классе, они становятся экземплярами MethodType,
# когда вы обращаетесь к ним через экземпляр класса.
# Однако в __dict__ класса они хранятся как обычные функции (FunctionType), а не как методы (MethodType).
# В вашем случае, когда вы вызываете cls.__dict__.items(), вы получаете атрибуты класса,
# и методы bar и baz являются экземплярами FunctionType, а не MethodType.
# Проверка типов:
# В функции methods, вы проверяете, является ли val экземпляром MethodType.
# Поскольку методы в __dict__ класса являются функциями, а не методами,
# проверка не проходит, и вы получаете пустой список.
# В функции methods1, вы проверяете, является ли val экземпляром FunctionType,
# и поскольку методы bar и baz являются функциями в __dict__, проверка проходит,
# и вы получаете их имена.
# Исправление:
# Если вы хотите получить имена методов класса, вам следует использовать FunctionType,
# как в methods1. Вот исправленный код:
#
# Заключение:
# Таким образом, methods(Foo) возвращает пустой список, потому что вы проверяете на MethodType,
# в то время как методы в __dict__ класса являются экземплярами FunctionType.
# Использование FunctionType в methods1 правильно, и именно поэтому вы получаете имена методов.
