t1=(1,1)
t2=(2,2)
t3=(3,3)
t4=(4,4)
t5=(5,5)
p=[t1,t2,t3,t4,t5]
x1,y1=p[0]
x2,y2=p[1]
m=(y2-y1)/(x2-x1)
c=y1-m*x1
straight=True
for i in range(len(p)):
    x,y=p[i]
    if y!=m*x+c:
            straight=False
            break
if straight:
    print("The points lie on a straight line.")
else:
    print("The points dont lie on a straight line.")
     