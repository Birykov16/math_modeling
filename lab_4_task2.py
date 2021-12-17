def fgh(*args):
  l = len(args)
  k = 1
  for i in range (l):
    k = k * args[i]
  print(k)
fgh(4,7,1)