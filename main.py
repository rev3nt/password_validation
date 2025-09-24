password = 'pipipupu'

user_input = input('Введите пароль: ')

while user_input != password:
    print('Пароль неверный, попробуйте снова')
    user_input = input('Введите пароль: ')

print('Поздравляю, вы подобрали пароль!')