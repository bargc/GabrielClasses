import Users

user1 = Users("Gabriel", "bar", "102030", "ghited2003@gmail.com")

user2 = Users("Danilo", "tuba", "304050", "d.canivel@gmail.com")

print type(user1)


user1.displayUserEmail()
user2.displayUserEmail()
# print "Total %d" % Users.userCount
print "Total Users {}".format(Users.userCount)