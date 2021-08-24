from sys import stdin

def mergesort(arr):
    global count
    n = len(arr)
    if n>1:
        mid = n//2
        leftP=arr[:mid]
        rightP=arr[mid:]
        dl = len(leftP)
        rl = len(rightP)
        mergesort(leftP)
        mergesort(rightP)
        i,j,k,d = 0,0,0,0
        while i < dl and j < rl:
            if leftP[i] < rightP[j]:
                arr[k] = leftP[i]
                i+=1
                count+=d
            else:
                arr[k] = rightP[j]
                j+=1
                d+=1
            k+=1
        while i < dl:
            arr[k] = leftP[i]
            i+=1
            k+=1
            count+=d
        while j < rl:
            arr[k]= rightP[j]
            j+=1
            k+=1
    return 0


def solve(Arr):
    global count
    count = 0
    mergesort(Arr)
    r = count
    return r
"""def main():
    n = int(stdin.readline().strip())
    while n != 0:
        num =[int(stdin.readline()) for _ in range(n)]        
        print(solve(num))
        n = int(stdin.readline().strip())"""
def main():
    n = int(stdin.readline().strip())
    while n !=0:
        num = []
        for i in range(n):
            add = int(stdin.readline().strip())
            num.append(add)
        print(solve(num))
        n = int(stdin.readline().strip())

main()
