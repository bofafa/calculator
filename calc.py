def check_num(num):
  try:
    return float(num)
  except ValueError:
    print('input error ' + str( num))
    exit()

def check_op(operator):
  if operator in ['+','-','*','/']:
    return True
  else :
    print("Wrong operator")
    return False
 

def calc(a,b,op):
  loc_result = 0
  a = check_num(a)
  b = check_num(b)

  if check_op(op):
    if op =='+':
      loc_result = a + b
    if op =='-':
      loc_result = a - b
    if op =='*':
      loc_result = a * b
    if op =='/':
      if b == 0:
        print("** b can not be zero **")
      else: 
       loc_result = a / b
  return loc_result

result = 0
exp ='1 + 1'  #string, must have space
exp = exp.split() #from string to list
print(exp)


while (len(exp) >= 3 and len(exp)%2):
  a = exp[0]
  b = exp[2]
  op= exp[1]
  result = calc(a,b,op)
  del exp[:2]
  print(exp)
  exp[0] = result
print("expression result is : " + str (result))

# except ValueError:
#   print("Data error")
# except ZeroDivisionError:
#   print("b can not be zero")