# -*- coding: utf-8 -*-
"""Assignment5.ipynb

#Square Numbers and Return Their Sum
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)


result = Point(2, 3, 4)
print(result.sqSum())





#Implement a Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)


result = Calculator(15, 90)
print("Addition:", result.add())
print("Subtraction:", result.subtract())
print("Mutliplication:", result.multiply())
print("Division:", result.divide())




#Implement the Complete Student Class
class Student:
  __name = None
  __rollNumber =None

  def setName(self,name):
   self.__name = name
  def getName(self):
    return self.__name

  def setRollNumber(self, rollNumber):
    self.__rollNumber = rollNumber

  def getRollNumber(self):
    return self.__rollNumber


result = Student()
result.setName("Varun Kumar")
print("Name:", result.getName())
result.setRollNumber(7)
print("Roll Number:", result.getRollNumber())






#Implement a Banking Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getTitle(self):
        return self.title

    def getBalance(self):
        return self.balance   


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def getIR(self):
       return self.interestRate


result = SavingsAccount("Varun Kumar", 5000, 10)
print("Title:", result.getTitle())
print("Initial Balance(in Rs.):", result.getBalance())
print("Intrest Rate(%):", result.getIR())





#Handling a Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    # withdrawal method
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    # deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    # Return Value
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    # IntrestEarned Method
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


result = SavingsAccount("Varun Kumar", 5000, 3.5)
print("Initial Balance (in Rs.):", result.getBalance())
result.withdrawal(1000)
print("Balance after withdrawal (in Rs.):", result.getBalance())
result.deposit(500)
print("Balance after deposit (in Rs.):", result.getBalance())
print("Interest on current balance (in Rs.):", result.interestAmount())



