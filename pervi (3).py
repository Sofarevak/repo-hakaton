P, M, K, X, Z = map(int, input().split())
days=0
if K*21<3*(P+M):
    print(-1)
else:
    while X<Z:
        X+=K
        if days%7==6:
            X-=P
        if days&7==0:
            X-=M
        days+=1    
    print(days)                

