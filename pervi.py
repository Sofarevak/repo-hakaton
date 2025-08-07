a=int(input())
mina=1001
maxa=-1001
while a!=0:
    if a<mina:
        mina=a
    if a>maxa:
        maxa=a
    a=int(input())
print(abs(maxa-mina))