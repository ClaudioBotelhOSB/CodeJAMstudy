import numpy as np

t= input()
t1=0
for ti in range(int(t)):
  t1+=1
  n0=input()
  n = int(n0)
  m = np.full((n, n), 0, dtype=int)

  stopv=stoph=ev=eh=diag=0

  for i in range(n):
    for j in range(n):
      m[i][j]=int(input())
      
  for i in range(n):
    for j in range(n):
      if i==j:
        diag+=m[i][j]
        for k in range (j, n):
          if stoph==0:
            if k>j:
              if m[i][j]==m[i][k]:
                eh+=1
                stoph=1
                print(i,j,i,k)
              break
            stoph=0
          if stopv==0:
            if m[j][i]==m[k][i]:
              if stopv==0:
                ev+=1
                stopv=1
              break       
          


  print("Case #"+str(t1)+": "+ str(diag)+" "+str(eh)+" "+str(ev))
