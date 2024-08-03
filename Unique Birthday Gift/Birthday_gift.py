class solution:
    @staticmethod
    def output(n,a):
        if k==1:
            for i in range(1,n+1):
                a.append([i])
        else:
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if j%i == 0:
                        a.append([i,j])
        return len(a)
        
n=int(input())
k=int(input())
a=[]
Solution=solution()
result=Solution.output(n,a)
print(result)