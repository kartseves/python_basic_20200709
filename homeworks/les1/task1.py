"""
1. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько
чисел и строк и сохраните в переменные, выведите на экран.
"""

bool_var1 = True
bool_var2 = False

print(bool_var1, bool_var2, sep="; ")

int_var1 = 4325234
int_var2 = -2343443

print(int_var1, int_var2, sep=", ")

float_var1 = 23.4325234
float_var2 = -324.2343443

print(float_var1, float_var2, sep=", ")

print('-----------------------------------------')

str_var1 = 'Добрый день, '
str_var2 = "Давайте знакомиться?"
str_var3 = ' - это прекрасный возраст!'

str_question1 = 'Как Вас зувут?\n'
str_question2 = ', сколько Вам лет?\n'

print(str_var2, end=" ")

str_user_name = str(input(str_question1))
print(str_var1 + str_user_name + '!', end=' ')

str_user_age = str(input(str_user_name + str_question2))
print(str_user_name + ', ' + str_user_age + str_var3)
