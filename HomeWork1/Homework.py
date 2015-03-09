__author__ = 'barFIRSTJOB!'


#importing libraries
import csv

def write_to_csv(content, filename, writetype):
    resultFile = open(filename, writetype)
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(content)
if __name__ == '__main__':
#opening the excell file
    with open('train.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")

    #Declaring an empty list for each column
        PassengerId = []
        Survived = []
        Pclass = []
        Name = []
        Sex = []
        Age = []
        SibSp = []
        Parch = []
        Ticket = []
        Fare = []
        Cabin = []
        Embarked = []

        for row in readCSV:
            PassengerId2 = row[0]
            Survived2 = row[1]
            Pclass2 = row[2]
            Name2 = row[3]
            Sex2 = row[4]
            Age2 = row[5]
            SibSp2 = row[6]
            Parch2 = row[7]
            Ticket2 = row[8]
            Fare2 = row[9]
            Cabin2 = row[10]
            Embarked2 = row[11]

            PassengerId.append(PassengerId2)
            Survived.append(Survived2)
            Pclass.append(Pclass2)
            Name.append(Name2)
            Sex.append(Sex2)
            Age.append(Age2)
            SibSp.append(SibSp2)
            Parch.append(Parch2)
            Ticket.append(Ticket2)
            Fare.append(Fare2)
            Cabin.append(Cabin2)
            Embarked.append(Embarked2)

        #all items are separated in columns, now let's check blank values

        #lets sum all our numbers at our str to get a mean
        i = len(Age) - 1
        q = 0
        while i >= 1:
            s = Age[i]
            i = i- 1

            t = Age[i]
            i = i - 1

            if s.isdigit():
                q = float(q) + float(s)
            else:
                if s == '':
                    None
                else:
                    q = float(q) + float(s)


            if t.isdigit():
                q = float(q) + float(t)
            else:
                if s == '':
                     None

                else:
                    q = float(q) + float(s)



        #we have our mean
        media = float (q) / float(len(Age))


        #Now lets change the value of all blanks slots
        i = len(Age)
        while i >= 1:

            i = i - 1
            s = Age[i]
            if s == '':
                Age[i] = int(media)

            i = i- 1
            if i == -1:
                break
            t = Age[i]

            if t == '':
                Age[i] = int(media)



        NewList = []

        while i < 892:
            NewList.append([PassengerId[i], Survived[i], Pclass[i], Name[i], Sex[i], Age[i], SibSp[i], Parch[i], Fare[i],Cabin[i],Embarked[i]])
            i = i + 1




        print (NewList)
        filename = 'train2.csv'

        write_to_csv(NewList, filename, 'wb')










