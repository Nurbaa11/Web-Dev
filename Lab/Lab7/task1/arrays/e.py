n=int(input())
a=list(map(int,input().split()))
def func(n,a):
    for i in range(0,n-1):
       
        if(a[i]/abs(a[i])==a[i+1]/abs(a[i+1])):
            print("YES")
            return
    print("NO")
func(n,a)