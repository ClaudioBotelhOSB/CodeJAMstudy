t = int(input(""))
for i in range(1,t+1):
  n = input()
  a = ''
  b = ''
  for x in n:
    if x == '4':
      a+='2'
      b+='2'
    else:
      a+=x
      b+='0'
  a = int(a)
  b = int(b)
  print("Case #{}: {} {}".format(i, a, b))
