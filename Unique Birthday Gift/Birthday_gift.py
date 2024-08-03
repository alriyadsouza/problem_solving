class solution:
    @staticmethod
    def output(n,a[k]):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j%i == 0:
                    a.append([i,j])
        
n=int(input())
k=int(input())
a=[]
Solution=solution()
result=Solution.output(n,a[k])
print(result)