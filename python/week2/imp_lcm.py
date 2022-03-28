def lcm(a,b):
  if (a > b):
      maximum = a
  else:
      maximum = b
  while (True):
      if (maximum % a == 0 and maximum % b == 0):
          break
      maximum = maximum + 1
  return maximum

def lcm_run():
  print("The LCM of 16, 12 is", lcm(16,12))
  print("The LCM of 377, 27 is",lcm(377, 27))