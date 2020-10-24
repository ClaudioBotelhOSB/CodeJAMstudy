for t in range(int(input())):
  n = int(input())

  ax=n
  bx=1
  cx=0
  a=[ax]
  b=[bx]
 
  if((n/2)%2==0):
    for y in range(int(int(n)/2)):
      print((y+1)*2, end = ' ')
      ax+=(y+1)*2
    print(1, end = ' ')
    for y in range(int(int(n)/2)-1):
      print(y+3, end = ' ')
      bx+=y+3
    cx = 1+2*(int(int(n)/2)-1)
    bx+=cx
    while(ax!=bx):
      cx+=2
      bx+=cx
    print(cx)
  else:
    print('NO') 


