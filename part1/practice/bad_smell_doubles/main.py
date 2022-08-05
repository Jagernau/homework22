# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def _sorted(self):
        self.lst.sort()
        return self.lst

    def _sorting(self):
        return sorted(self.lst)

    def _asc_sorting(self):
        return sorted(self.lst, reverse=False)

    def sorted_func(self):
        list_ = self.lst
        return sorted(list_, reverse=False)

some_list = SomeClass()
print(some_list.sorted_func())
