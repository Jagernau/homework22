# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv):
    data = []
    list_ = csv.split("\n")
    for i in range(0,3):
        data.extend([list_[i].split(";")])
    return data


    # Фильтрация
def _filter(data: list):
    dat = []
    for i in data:
        if int(i[1]) > 10:
            dat.append(i)
    return sorted(dat, key=lambda x: int(x[1]) )


 
def get_users_list():
    data = _read(csv)
    return _filter(data)




if __name__ == '__main__':
    print(get_users_list())
