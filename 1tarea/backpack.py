from sys import stdin
def probar(arr,N,K,limit,maxi):
  ok = False
  if limit >= maxi:
    nights,travel,camp = 0,0,0
    while nights <= K and camp != N:      
      if travel+ arr[camp] <= limit:
        travel+= arr[camp]
        camp+=1
      else:
        nights +=1
        travel = 0
      #print("travel" + str(travel) + " " + "nights" + str(nights) + " " + "camp" + str(camp))
    if nights <= K:
      ok = True
    #print(str(nights) + " " + str(camp))
  return ok


def binary(arr,lo,hi,N,K,maxi):
  #print(maxi)
  while lo +1 != hi:
    mid = lo+((hi-lo)>>1)
    #print(mid)    
    if probar(arr,N,K,mid,maxi):
      hi = mid
    else:
      lo = mid
  return hi

def sumar(arr):
  n = len(arr)
  suma = 0
  maximo = 0
  for i in range(n):
    thing = arr[i]
    suma+=thing
    if maximo < thing:
      maximo = thing
  return suma,maximo

def solve(N, K, dist):
  lo = 0
  hi,maxi = sumar(dist)
  ans = binary(dist,lo,hi,N+1,K,maxi)  
  return ans

def main():
  N,K,dist = None,None,None
  line = stdin.readline()
  while len(line)!=0:
    N,K = map(int, line.split())
    dist = [ int(stdin.readline()) for _ in range(N+1) ]
    print(solve(N, K, dist))
    line = stdin.readline()

main()
