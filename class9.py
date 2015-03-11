# list vs Tuple

def Example():
    x = 10
    y = 12
    return x, y

listExample = [1,2,3,4,5]
tupleExample = (1,2,3)

print type(listExample)
print type(tupleExample)

# listExample[2]= 'Gabriel'
#
# print listExample
#
# tupleExample[2] = 'Gabriel'

foo, bar = Example()

foo = 'test'

print foo
print type(Example())

######################################################
import threading
import Queue
import urllib2

def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = ["http://yahoo.com", "http://www.asdsadasdasd.com"]

q = Queue.Queue()

for each_url in theurls:
    t = threading.Thread(target=get_url, args=(q, each_url))
    t.daemon = True
    t.start()

first_one_to_respond = q.get()
print first_one_to_respond

