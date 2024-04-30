import Factorial 
def calculator(x, y, operator):
  try:
    x= float(x)
    y = float(y)
  except :
    return "please Enter just int or float numbers"
  if operator == '+':
        return x + y
  elif operator == '-':
        return x - y
  elif operator == '*':
        return x * y
  elif operator == '/':
    if y != 0:  # Avoid division by zero
      return x / y
    else:
      return "Error: Division by zero!"
  elif operator == '!' :
      return Factorial.factorial(int(x))
  else:
      return "Error: Invalid operator!"
# Example usage
