# exDict = {'Gabriel':[23, 'male'], 'Danilo':[32, 'male'], 'Jao':[27, 'unknow']}
# exDict2 = dict(a=23, b=25, c=44)
#
# print exDict2
#
# print exDict['Jao']
#
# exDict['Matheus'] = 31
#
# print exDict['Jao'][1]

# import time
#
# help(time)

# x = 9.23559
# print round(x, 3)
#
# list = [10, 23, 240, 100, 8]
# largest = max(list)
# smallest = min(list)
#
# print largest, smallest

# number_negative = -5
# number_positive = 5
#
# if abs(number_negative) == number_positive:
#     print ('True')
#
# print (abs(number_negative))

# intMe = 'aaaaa'
# print type(intMe)
# intMe = bool(intMe)
# print type(intMe)
# print intMe


# import os
#
# path = os.getcwd()
#
# os.mkdir('newDir')
# os.rename('newDir', 'newDir2')
# os.rmdir('newDir2')

# import urllib2
#
# # from urllib2 import Request
# link = 'http://www.globo.com/'
#
# req = urllib2.Request(link)
#
# resp = urllib2.urlopen(req)
#
# webpage = resp.read()
# titulos = (webpage.split('<span>')[2].split('</span>')[1])
# print titulos