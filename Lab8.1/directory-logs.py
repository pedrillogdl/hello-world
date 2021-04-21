
import os
import keyboard
import time
import os.path
from os import path	
import unittest
import logging


logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)

class AGENDA():

	def __init__(self, name,email,age,country):
		self.name=name
		self.email=email
		self.age=age
		self.country=country

	def AddRecord(self):
		if os.path.exists("MyAgenda.txt"):
			newFile=open("MyAgenda.txt","a+")
		else:
			newFile=open("MyAgenda.txt","w+")
		newFile.write("\r")
		newFile.write("Name:"+self.name+"\n")
		newFile.write("E-mail:"+self.email+"\n")
		newFile.write("Age:"+str(self.age)+"\n")
		newFile.write("Country:"+self.country+"\n")
		newFile.close()


	def DeleteRecord(self,NameToDelete):
		OpenFile=open("MyAgenda.txt","r")
		lines=OpenFile.readlines()
		OpenFile.close()
		count=0
		ListRecord=[]
		for line in lines:
			if count>=1 and count<4:
				ListRecord.append(line)
				count=count+1
			if line.strip() == "Name:"+NameToDelete:
				ListRecord.append(line)
				count=count+1
		TheFile=open("MyAgenda.txt","w+")
		newListRecord= list(map(str.strip, ListRecord))
		newlines= list(map(str.strip, lines))
		for i in newListRecord:
			for line in newlines:
				if line.strip() == i:
					myindex=newlines.index(line.strip())
					break
			del newlines[myindex]
		for line in newlines:
			TheFile.write(line+"\n")
		TheFile.close()
			

	def FindRecord(self,NameToFind):
		OpenFile=open("MyAgenda.txt","r")
		lines=OpenFile.readlines()
		OpenFile.close()
		count=0
		ListRecord=[]
		for line in lines:
			if count>=1 and count<4:
				ListRecord.append(line)
				count=count+1
			if line.strip() == "Email:"+NameToFind:
				ListRecord.append(line)
				count=count+1
		if len(ListRecord)==0:
			print("The Record wasn't found:")
			User=False			
		else:
			for i in ListRecord:
				print(i)
			User=True
		return User


	def DisplayAll(self):
		OpenFile=open("MyAgenda.txt","r")
		lines=OpenFile.readlines()
		OpenFile.close()
		count=0
		ListRecord=[]
		for line in lines:
			print(line)


def Clear():
	if os.name == 'posix':
		_=os.system('clear')
	else:
		_=os.system('cls')


def PrintMenu():
	Clear()
	print ("                     Agenda 2021           ")
	print("a)Add a Record:")
	print("b)Delete a Record:")
	print("c)Find a Record:")
	print("d)Show all Records:")
	print("e)Exit:")
	while True:
		try:
			answer=input("Select the option(character that precedes the Action) from the Menu: ").lower()
			assert answer=="a" or answer=="b" or answer=="c" or answer=="d" or answer=="e"
		except ValueError:
			print("Sorry, that is not a valid option could you please try again?")
			logging.info("wrong value was entered")
		except AssertionError :
			print("Sorry, that is not a valid option could you please try again?")
			logging.info("wrong value was entered")
		else:
			break
	return answer



answerUser=PrintMenu()


while answerUser!="e":	
	
	if answerUser == "a":
		print (f"¨Please enter the information for the contact \r\n")
		while True:
			try:
				ContactName= input(f"Please Enter the Contact's Name: ")
				ContactEmail= input(f"Please Enter the Contact's Email: ")
				ContactAge= int(input(f"Please Enter the Contact's Age: "))
				ContactCountry= input(f"Please Enter the Contact's Country: ")
			except ValueError:
				print("Sorry, that is not a valid value could you please try again?")
				logging.info("wrong value was entered")
			else:
				ContactForSaving=AGENDA(ContactName,ContactEmail,ContactAge,ContactCountry)
				break
		ContactForSaving.AddRecord()
		print("The Contact has been saved in the MyAgenda.txt file")
		time.sleep(5)
	if answerUser == "b":
		earlyExit=False
		ContactFound=False
		while True:
			try:
				ContactName= input(f"Please Enter the Contact's Name: ")	
				myFile= open("MyAgenda.txt", mode="r")			
			except ValueError:
				print("Sorry, that is not a valid value could you please try again?")
				logging.info("wrong value was entered")
			except FileNotFoundError:
				print("Sorry there are no records, please first add a Record in the previous Menu ")
				logging.error("MyAgenda.txt File not found ")
				earlyExit=True
				break
			else:
				ContactForSaving=AGENDA(ContactName,"0","0","0")
				break
		if earlyExit==True:
			time.sleep(5)
		else:
			myFile.close()
			ContactFound=ContactForSaving.FindRecord(ContactName)
		if ContactFound==True:
			ContactForSaving.DeleteRecord(ContactName)
			print("The Record has been deleted from the MyAgenda.txt file")
			time.sleep(5)
		else:
			time.sleep(5)
	if answerUser == "c":
		earlyExit=False
		while True:
			try:
				ContactName= input(f"Please Enter the Contact's Name: ")
				myFile= open("MyAgenda.txt", mode="r")					
			except ValueError:
				print("Sorry, that is not a valid value could you please try again?")
				logging.info("wrong value was entered")
			except FileNotFoundError:
				print("Sorry there are no records, please first add a Record in the previous Menu ")
				logging.error("MyAgenda.txt File not found ")
				earlyExit=True
				break
			else:
				ContactForSaving=AGENDA(ContactName,"0","0","0")
				break
		if earlyExit==True:
			time.sleep(5)
		else:
			myFile.close()
			ContactFound=ContactForSaving.FindRecord(ContactName)
		if ContactFound==True:
			answerDisplay=input("Please press x to continue:").lower()
			if keyboard.read_key() == "x":
				time.sleep(5)
		else:
			time.sleep(5)
	if answerUser == "d":
		earlyExit=False
		while True:
			try:
				myFile= open("MyAgenda.txt", mode="r")	
			except FileNotFoundError:
				print("Sorry there are no records, please first add a Record in the previous Menu ")
				logging.error("MyAgenda.txt File not found ")
				earlyExit=True
				break
			else:
				break
		if earlyExit==True:
			time.sleep(5)
		else:
			myFile.close()
			ContactForSaving=AGENDA("0","0","0","0")
			ContactForSaving.DisplayAll()
			answerDisplay=input("Please press x to continue:").lower()
			if keyboard.read_key() == "x":
				time.sleep(5)
	answerUser=PrintMenu()





	