

def fact_rec(n):
  if (n == 0) or (n == 1):
    return 1
  else:
    return n * fact_rec(n - 1)
num = 6
result= fact_rec(num)
print("the factorial of 3 is",(num,result))