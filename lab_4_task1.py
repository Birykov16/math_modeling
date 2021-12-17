def frs(*args):
  l = len(args)
  k = 0
  for i in range (l):
    k = k + args[i]
  print(k / l)

frs(7,3,9)
