import MySQLdb
import hashlib


db = MySQLdb.connect("localhost", "root", "", "gabriel_db")
cursor = db.cursor()

try:
    sql = "SELECT * FROM users"
    cursor.execute(sql)

    results = cursor.fetchall()

    #print results

    for row in results:
        fname = row[1]
        fname2 = row[2]
        fname3 = row[3]
        fname4 = row[4]
        print ("Name: {} - {} - {} - {}".format(fname,fname2,fname3, fname4))

except Exception as e:
    print str(e)

name = "Bblabla3"
email = "blaaa3@blaa.com"
username = "bla3"
password = "102030"

sqlSearchUser = "Select count(*) FROM users WHERE username = '{}'".format(username)
sqlInsert = "INSERT INTO users (name, email, username, password, create_date) VALUES('{}','{}','{}',md5('{}'), now())".format(name, email, username,password)

try:
    cursor.execute(sqlSearchUser)
    results = cursor.fetchall()
    if results[0][0] >= 1:
        print "User alredy exists."
    else:
        try:

            cursor.execute(sqlInsert)
            db.commit()
            print "New user added"
        except Exception as e:
            print str(e)
            db.rollback()

except Exception as e:
    print str(e)
    db.rollback()

md5_password = hashlib.md5(password).hexdigest()

sqlSearchUserByusername = "Select name FROM users WHERE username = '{}' and password = '{}'".format(username, md5_password)
print sqlSearchUserByusername

try:
    cursor.execute(sqlSearchUserByusername)
    results = cursor.fetchall()

    if len(results) == 0:
         print "Your username or password is invalid"
    else:
        print "User {} logged.".format(results[0][0])

except Exception as e:
    print "Your username or password is invalid"
    print str(e)
    db.rollback()


db.close()

