import fun
import Calc
print (fun.funny())
while True:
  x = input('Enter the first number (x): ')
  if x.lower() == 'exit':
    break
  operator = input('Enter the operator (+, -, *, /,!): ')
  if operator.lower() == 'exit':
    break
  elif operator != '!':
      y = input('Enter the second number (y): ')
      if y.lower() == 'exit':
        break
      else :
          result = Calc.calculator(x, y, operator)
  elif operator == '!' :
      result = Calc.calculator(x, x, operator)
  
  if type(result) == float:
    print(x,operator,y,"=", result)
  else :
    print("X!=",result)

