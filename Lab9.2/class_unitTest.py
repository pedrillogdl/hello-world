
import os
import os.path
import unittest


class AGENDA():
    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = age
        self.country = country

    def AddRecord(self):
        if os.path.exists("MyAgenda.txt"):
            newFile = open("MyAgenda.txt", "a+")
        else:
            newFile = open("MyAgenda.txt", "w+")
        newFile.write("\r")
        newFile.write("Name:" + self.name + "\n")
        newFile.write("E-mail:" + self.email + "\n")
        newFile.write("Age:" + str(self.age) + "\n")
        newFile.write("Country:" + self.country + "\n")
        newFile.close()

    def DeleteRecord(self, NameToDelete):
        OpenFile = open("MyAgenda.txt", "r")
        lines = OpenFile.readlines()
        OpenFile.close()
        count = 0
        ListRecord = []
        for line in lines:
            if count > 0 and count < 4:
                ListRecord.append(line)
                count = count + 1
            if line.strip() == "Name:" + NameToDelete:
                ListRecord.append(line)
                count = count + 1
        TheFile = open("MyAgenda.txt", "w+")
        newListRecord = list(map(str.strip, ListRecord))
        newlines = list(map(str.strip, lines))
        for i in newListRecord:
            for line in newlines:
                if line.strip() == i:
                    myindex = newlines.index(line.strip())
                    break
            del newlines[myindex]
        for line in newlines:
            TheFile.write(line + "\n")
        TheFile.close()

    def FindRecord(self, NameToFind):
        OpenFile = open("MyAgenda.txt", "r")
        lines = OpenFile.readlines()
        OpenFile.close()
        count = 0
        ListRecord = []
        for line in lines:
            if count > 0 and count < 4:
                ListRecord.append(line)
                count = count + 1
            if line.strip() == "Name:" + NameToFind:
                ListRecord.append(line)
                count = count + 1
        if len(ListRecord) == 0:
            print("The Record wasn't found:")
            User = False
        else:
            for i in ListRecord:
                print(i)
            User = True
        return User

    def DisplayAll(self):
        OpenFile = open("MyAgenda.txt", "r")
        lines = OpenFile.readlines()
        OpenFile.close()
        for line in lines:
            print(line)


class TESTAGENDA(unittest.TestCase):
    def test_happyPath(self):
        # Right: Testing that the app is doing what it should do
        # adding a record, trying to add a fake record,
        # finding a valid record, finding an invalid record
        # deleting a valid record, deleting an invalid record
        # and displaying all records at once
        recordForTesting = AGENDA("UserForTesting", "Email@Testing.com", 00, "Mexico")
        fakeRecord = ""
        self.assertIsInstance(recordForTesting, AGENDA)
        self.assertIsNone(recordForTesting.AddRecord())
        with self.assertRaises(Exception):
            fakeRecord.AddRecord()
        self.assertTrue(recordForTesting.FindRecord("UserForTesting"))
        self.assertFalse(recordForTesting.FindRecord("UserForTestingg"))
        self.assertIsNone(recordForTesting.DeleteRecord("UserForTesting"))
        self.assertIsNone(recordForTesting.DeleteRecord("UserForTestingg"))
        self.assertIsNone(recordForTesting.DisplayAll())

    def test_boundary(self):
        # B: Testing boundaries, verfiying first that the file
        # recording the users doesn't exist
        # Testing that all actions doesn't work when the file doesn´t exist,
        # then after adding a record
        # verifying that the file is created
        recordForTestingB = AGENDA("UserForTestinB", "EmailB@Testing.com", 11, "MexicoB")
        if os.name == 'posix':
           # _ = os.system('rm -rf MyAgenda.txt')
           # self.assertNotEqual(os.system('ls MyAgenda.txt'), 0)
            #self.assertFalse(recordForTestingB.FindRecord("UserForTesting"))
            with self.assertRaises(Exception):
                recordForTestingB.FindRecord("UserForTesting")
            with self.assertRaises(Exception):
                recordForTestingB.DeleteRecord("UserForTesting")
            with self.assertRaises(Exception):
                recordForTestingB.DisplayAll()
            recordForTestingB.AddRecord()
            self.assertEqual(os.system('ls MyAgenda.txt'), 0)
        else:
            #_ = os.system('del MyAgenda.txt')
            self.assertNotEqual(os.system('dir MyAgenda.txt'), 0)
            with self.assertRaises(Exception):
                recordForTestingB.FindRecord("UserForTesting")
            with self.assertRaises(Exception):
                recordForTestingB.DeleteRecord("UserForTesting")
            with self.assertRaises(Exception):
                recordForTestingB.DisplayAll()
            recordForTestingB.AddRecord()
            self.assertEqual(os.system('dir MyAgenda.txt'), 0)


if __name__ == '__main__':
    unittest.main()
