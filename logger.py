from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{surname}\n{name}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{surname};{name};{phone};{adress}\n"
    f"Выберите вариант"))
   
    while var !=1 and var !=2:
        print("Неправильный ввод")
    var = int(input('Введите данные'))

    if var == 1:
        with open('phone1','a', encoding='utf-8') as f:
            f.write(f"{surname}\n{name}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('phone2','a', encoding='utf-8') as f:
            f.write(f"{surname};{name};{phone};{adress}\n\n")

def print_data():
    print('Вывожу данные из 1 файла:\n')
    with open('phone1','r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_firs_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_firs_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_firs_list))
    print('Вывожу данные из 2 файла:\n')
    with open('phone2','r', encoding='utf-8') as f:
        data_second = f.readlines
        print(*data_second)

