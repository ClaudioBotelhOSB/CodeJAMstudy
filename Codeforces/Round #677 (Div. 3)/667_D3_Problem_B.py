for t in range(int(input())):
  input()
  x = str(input())
  x = x.replace(" ","")
  res = 0
  uns = x.count('1')
  p_uns = [i for i in range(len(x)) if x.startswith('1', i)]
  for i in range(len(p_uns)):
    if i+1<len(p_uns) and p_uns[i]+1 != p_uns[i+1]:
      res+=p_uns[i]+1-p_uns[i+1]
  res=abs(res)
  print(res)
