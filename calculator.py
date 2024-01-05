from calculations import *

while True:
  print("******** CALCULATOR *********")
  print("Choose the calculation from below")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  print("Enter Q to exit")

  method = input("Enter your calculation method: ")
  if method == 'q' or method=='Q':
    break

  num1 = float(input("Add your first Number: "))
  num2 = float(input("Add your second number: "))

  if method == '1':
    addition(num1,num2)
  elif method == '2':
    subtraction(num1,num2)
  elif method == '3':
    multiplication(num1,num2)   
  elif method == '4':
    division(num1,num2)  
  else:
     print("Invalid input")      

