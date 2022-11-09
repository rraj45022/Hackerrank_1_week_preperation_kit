# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
a = []
for i in range(q):
    x = list(map(int,input().split(' ')))
    if x[0] == 1:
        a.append(x[1])
    elif x[0] == 2:
        a.pop(0)
    elif x[0] == 3:
        print(a[0])
