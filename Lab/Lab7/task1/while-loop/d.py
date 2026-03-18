a=int(input())
def func(a):
    while(a>1):
        if(a%2!=0):
            print("NO")
            return
            break
        a/=2
    print("YES")
func(a)

    