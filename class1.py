# print('Ola mundo')

frase1 = 'inicio da frase'
frase2 = ' continuacao da frase'
bbbb = True
dddd = False
eeee = 1.2
ffff = 1

names_list = ['Gabriel', 'Joao', 'Matheus']

names_list_2 = names_list.append('Danilo')

number_list = [1, 2, 3, 4, 5, 6, 7]

number_list_2 = number_list.append('Danilo')

soma = 1 + 1
subt = 1 - 1
mult = 3 * 4
div = 4 / 2
expo = 4 ** 4

test_condition = 1

'''
while test_condition <= 10:
    print(test_condition)
    test_condition += 1
'''

# for x in range(12, 11):
#     print (x)
count = 1
for each_name in names_list:
    print('{} {} {}'.format(count, each_name, 'Canivel'))
    count += 1

for each_number in number_list:
    print(each_number)


    #print(bbbb + dddd)