users = {'Ruslan4ik' : {
    'password': '123',
    'money': '1000'
},
"Yusuf" : {
'password': '111',
'money': '2000'}}
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
if a == 2:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    try:
        users[login]
        users[login]['password']
    except:
        login = input("Введите верный логин: ")
        password = input("Введите верный пароль: ")
    if login in admins['login']:
        print("Вы вошли как админ")
    else:
        print("Вы вошли как обычный пользователь")
        admin_become = int(input("Хотите стать админом?\n"))
        if admin_become == 1:
            admin_password = input("Введите пароль для становления Admin: ")
            if admin_password == '777':
                print("Вы стали админом")
                admins['login'].append(login)



# комент
