users = {'Ruslan4ik': {'password': 123, 'money': 1000},
         'Yusuf': {'password': 111, 'money': 2000}}
#--------------------------
admins = {'login': ['Ruslan4ik']}
print("Добро пожаловать!")
a = int(input("Log In or Log Up?\n"))
if a == 1:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    money = int(input("Введите кол-во денег: "))
    users[login] = {}
    users[login]['password'] = password
    users[login]['money'] = money
    while True:
        print("1.Баланс\n", "2.Снятие денег со счета\n", "3.Пополнить баланс\n", "4.Получить права админа\n", "5.Замена логина и пароля\n", sep="")
        operations = int(input("Какую операцию хотить выбрать?: "))
        if operations == 1:
            print(users[login]['money'])
        if operations == 2:
            take = int(input("Какую сумму хотите снять со счета?: "))
            users[login]['money'] = users[login]['money'] - take
        if operations == 3:
            put = int(input("Какую сумму хотите положить на счет?: "))
            users[login]['money'] = users[login]['money'] + put
        if operations == 4:
            admin_become = int(input("Хотите стать админом?\n"))
            if admin_become == 1:
                admin_password = input("Введите пароль для становления Admin: ")
                if admin_password == '777':
                    print("Вы стали админом")
                    print('------------')
                    print('')
                    print("Список всех пользователей: ")
                    admins['login'].append(login)
                    all_users = [x for x in users]
                    print(*all_users, sep='\n')
                    print('')
                    print('-------------')
                all_money = 0
                for x in users:
                    all_money = users[login]['money'] + all_money
                all_money += money
                print("Всего денег в банке: ", all_money)
        if operations == 5:
            login_n = input("Введите новый логин: ")
            password_n = input("Введите новый пароль: ")
            users[login].update(password=password_n)
            users[login]['money'] = money
            users[login_n] = users[login]
            del users[login]
            print(users)
if a == 2:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    try:
        users[login]
        users[login]['password']
        users[login]['money']
    except:
        login = input("Введите верный логин: ")
        password = input("Введите верный пароль: ")
    if login in admins['login']:
        print("Вы вошли как админ")
        all_users = [x for x in users]
        print(all_users)
    else:
        print("Вы вошли как обычный пользователь")
    while True:
        print("1.Баланс\n", "2.Снятие денег со счета\n", "3.Пополнить баланс\n", "4.Получить права админа\n",
              "5.Замена логина и пароля\n", sep="")
        operations = int(input("Какую операцию хотить выбрать?: "))
        if operations == 1:
            print(users[login]['money'])
        if operations == 2:
            take = int(input("Какую сумму хотите снять со счета?: "))
            users[login]['money'] = users[login]['money'] - take
        if operations == 3:
            put = int(input("Какую сумму хотите положить на счет?: "))
            users[login]['money'] = users[login]['money'] + put
        if operations == 4:
            admin_become = int(input("Хотите стать админом?\n"))
            if admin_become == 1:
                admin_password = input("Введите пароль для становления Admin: ")
                if admin_password == '777':
                    print("Вы стали админом")
                    admins['login'].append(login)
                    all_users = [x for x in users]
                    print(all_users)
        if operations == 5:
            login_n = input("Введите новый логин: ")
            password_n = input("Введите новый пароль: ")
            users[login].update(password=password_n)
            users[login]['money'] = money
            users[login_n] = users[login]
            del users[login]
            print(users)
print(users)
print(admins)
