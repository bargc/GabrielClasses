import csv

with open('test1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")

    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

        #print only the values with letters because all the results are strings so you need only with letters

        for each_value in row:
            if each_value.isalpha():
                print each_value



    print dates
    print colors

# whatColor = input('What color do you wish to know the date of?:')
# coldex = colors.index(whatColor)
# theDate = dates[coldex]
# print('the date of', whatColor, 'is:', theDate)


# try:
#     whatColor = raw_input('What color do you wish to know the date of?')
#
#     if whatColor in colors:
#         coldex = colors.index(str(whatColor))
#         theDate = dates[coldex]
#         print('the date of', whatColor, 'is:', theDate)
#     else:
#         print ('Color not found')
#
# except Exception as e:
#     print(e)



try:
    whatColor = raw_input('What color do you wish to know the date of?')

    if True:
        division = 10/0



    if whatColor in colors:
        coldex = colors.index(str(whatColor))
        theDate = dates[coldex]
        print('the date of', whatColor, 'is:', theDate)
    else:
        print ('Color not found')

except Exception as e:
    print(e)





