class Users():

    userCount = 0

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        Users.userCount += 1


    def displayUserCount(self):
        print "Total Users {}".format(Users.userCount)


    def displayUserEmail(self):
        print "Name ", self.name, " Email ", self.email

