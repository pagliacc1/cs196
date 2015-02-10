def factor(n):
  res=[]
  FirstPrime = [2, 3, 5, 7, 11]
  for p in FirstPrime:
    if p*p>n:
        if n==1: return res
        res.append((n, 1))
        return res
    if not n%p:
      e=1
      n//=p
      while not n%p:
        n//=p
        e+=1
      res.append((p, e))
  decalage=[2,4,2,4,6,2,6,4,\
            2,4, 6 ,6,2,6,4,\
            2, 6 ,4,6, 8 ,4,\
            2,4,2,4, 8 ,6,4,\
             6 ,2,4,6,2,6,6,\
              4,2,4,6,2,6,4,\
           2,4,2, 10 ,2, 10 ]
  q=11
  while True:
    for dec in decalage:
      q+=dec
      if q*q>n:
            if n==1: return res
            res.append((n, 1))
            return res
      if not n%q:
        e=1
        n//=q
        while not n%q:
            n//=q
            e+=1
        res.append((q, e))