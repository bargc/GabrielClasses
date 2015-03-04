
def write_to_file(content, filename, writetype):
    savefile = open(filename, writetype)
    savefile.write(content)
    savefile.close()




filename = 'test1.txt'
content = 'Test to save in a file \nNew Line of text \n Line 3 testing sd asd asd as das das das das d asdd asd '

write_to_file(content, filename, 'w')


names_list = ['Gabriel', 'Joao', 'Matheus']

count = 0
for each_name in names_list:
    write_to_file('\n{} {} {}'.format(count, each_name, 'Canivel'), filename, 'a')
    count += 1



readMe = open(filename, 'r').readlines()
print type(readMe)

print readMe[2]