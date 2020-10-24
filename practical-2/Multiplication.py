# Implementation of multiplication


B = 10

def mul(a, b):
  res = []
  for i in range(0,len(a)+len(b)):
    res.append(0)
  for j in range(0,len(a)):
    carry=0
    for k in range(0,len(b)):
      tmp=int(a[len(a)-1-j])*int(b[len(b)-1-k])+res[j+k]+carry
      carry=int(tmp/B)
      res[j+k]=(tmp%B)
    res[j+len(b)]=carry
  result = ""
  for l in range(len(res)-1,-1,-1):
    result = result + str(res[l])
  return result.lstrip('0')


if __name__ == '__main__':
  a = "30668554534232"
  b = "2035767543"
  mul_result=mul(a,b)
  print("\nThe multiplication of big integers \n ")
  print(a+" * "+b+" = "+mul_result)
