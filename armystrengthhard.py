import sys

input = sys.stdin.readlines()
T = int(input[0])
for t in range(T):
  mG = max( map( int, input[4*t+3].split()))
  mM = max( map( int, input[4*t+4].split()))
  if mM > mG: print("MechaGodzilla")
  else: print("Godzilla")

