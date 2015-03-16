import MySQLdb
import hashlib

#login into the db
db = MySQLdb.connect("localhost", "root", "", "enterprise_db")
cursor = db.cursor()

#choose to log or create a new seller
log_in = input("Hello, type 1 for login as Seller or type 2 for create a New Seller:\n")
if log_in == 1: #log test
    print(("\nLogin with your Seller username and password: \n"))
    seller_login = raw_input("username = ")
    seller_password = raw_input("password = ")

    try:

        md5_password = hashlib.md5(seller_password).hexdigest() #autentication
        sqlSearchUserByusername = "Select password FROM seller WHERE username = '{}' and password ='{}'".format(seller_login, md5_password)


        try:
            cursor.execute(sqlSearchUserByusername)
            results = cursor.fetchall()

            if len(results) == 0:
                print "Your username or password is invalid"
            else:
                print "User {} logged in.\n".format(seller_login)
                print "Do you want to consult a client or register a new one?\n"
                check_client = input("Type 1 for consult or 2 for register: ")
                if check_client == 1:
                    name_of_client = raw_input("Type the name of your client: ")

                    try:
                        sql = "SELECT * FROM client WHERE name = '{}'".format(name_of_client)
                        cursor.execute(sql)

                        results = cursor.fetchall()

                        #print results

                        for row in results:
                            fname = row[1]
                            fname2 = row[2]
                            fname3 = row[3]
                            fname4 = row[4]
                            fname5 = row[4]
                            fname6 = row[4]
                            fname7 = row[4]
                            fname8 = row[4]
                            fname9 = row[4]
                            fname10 = row[4]
                            fname11 = row[4]
                            fname12 = row[4]
                            fname13 = row[4]
                            fname14 = row[4]

                            print ("Name: {} - {} - {} - {} -{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(fname,fname2,fname3, fname4, fname5, fname6, fname7, fname8, fname9, fname10, fname11, fname12, fname13, fname14))

                    except Exception as e:
                        print str(e)

                elif check_client == 2:
                    print "register"
                    name_of_client = raw_input("Type the name of the client\n")
                    fname2 = raw_input("Type the email of the client\n")
                    fname3 = input("Type the tellfone of the client\n")
                    fname4 = raw_input("Type the adress of the client\n")
                    fname5 = raw_input("Type the state of the client adress\n")
                    fname6 = raw_input("Type the country of the client adress\n")
                    fname7 = raw_input("Does the client want to buy the ITEM 1?\n")
                    fname8 = raw_input("Does the client want to buy the ITEM 2?\n")
                    fname9 = raw_input("Does the client want to buy the ITEM 3?\n")
                    fname10 = raw_input("Does the client want to buy the ITEM 4?\n")
                    fname11 = raw_input("Does the client want to buy the ITEM 5?\n")
                    fname12 = raw_input("Does the client want to buy the ITEM 6?\n")
                    fname13 = raw_input("Does the client want to buy the ITEM 7?\n")
                    fname14 = raw_input("Does the client want to buy the ITEM 8?\n")

                    sqlSearchUser = "Select * FROM client WHERE name = '{}'".format(name_of_client)
                    sqlInsert = "INSERT INTO client (name, email, tellphone, adress, state, country, item1, item2, item3, item4, item5, item6, item7, item8, seller, date_time)" \
                                " VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', now())".format(name_of_client,fname2,fname3, fname4, fname5, fname6, fname7, fname8, fname9, fname10, fname11, fname12, fname13, fname14, seller_login)

                    try:

                        cursor.execute(sqlInsert)
                        db.commit()
                        print "\n\nNew client created"

                    except Exception as e:
                        print str(e)
                        db.rollback()


        except Exception as e:
            print str("Error with your login, call 911 <3")
            db.rollback()

    except Exception as e:
        print str(e)
        db.rollback()

elif log_in == 2:
    pass_for_create = input("Type the password:\n")

    if pass_for_create == 102030:
        print("Okay. Type the new Sellers username and password")
        new_seller_login = raw_input("username = ")
        new_seller_password = input("password = ")
        sqlSearchUser = "Select count(*) FROM seller WHERE username = '{}'".format(new_seller_login)
        sqlInsert = "INSERT INTO seller (username, password, date_time) VALUES('{}',md5('{}'), now())".format(new_seller_login,new_seller_password)

        try:
            cursor.execute(sqlSearchUser)
            results = cursor.fetchall()
            if results[0][0] >= 1:
                print "User alredy exists."
            else:
                try:

                    cursor.execute(sqlInsert)
                    db.commit()
                    print "New user added\n\n"
                    print "Time to fill the profile"
                    name_profile = raw_input("Seller's name: ")
                    email_profile = raw_input("Seller's email: ")
                    adress_profile = raw_input("Seller's adress: ")
                    state_profile = raw_input("Seller's state: ")
                    country_profile = raw_input("Seller's country: ")

                    sqlSearchUser = "SELECT id FROM seller ORDER BY id DESC limit 1"

                    try:
                        cursor.execute(sqlSearchUser)
                        results = cursor.fetchall()

                        seller_id = results[0][0]

                        sqlInsert = "INSERT INTO seller_profile (name, email, adress, state, country, date_time) VALUES('{}','{}','{}','{}','{}' , now(), {})".format(
                            name_profile, email_profile, adress_profile, state_profile, country_profile, seller_id)


                        cursor.execute(sqlInsert)
                        db.commit()
                        print "profile created!"


                    except Exception as e:
                        print str(e)
                        db.rollback()


                except Exception as e:
                    print str("Error, call 911 <3")
                    db.rollback()

        except Exception as e:
            print str("Error, call 911 <3")
            db.rollback()



    else:
        print("Wrong code!")
        exit ()


db.close()