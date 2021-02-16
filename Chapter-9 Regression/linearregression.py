#This is listsum which is







 #type of list.... 

    
def listsum(l):
    sum=0
    for item in l:
        sum=sum+item
    return sum

#To find the mean to using listsum.....
def mean(l):
    sum=listsum(l)
    n=len(l) 
    return  sum/n
#To find the bar value of x and y:
def subfromlist(l,value,rounddigit):
    newl=[]
    for item in l:
        newl=newl + [round(item-value,rounddigit)]
    return newl


def multiplylist(l1,l2):
    l=[]
    n=len(l1)
    for i in range(n):
        n1=l1[i]
        n2=l2[i]
        l=l + [n1*n2]
        return l

def equation(r,meanx,meany,x):
    y=meany + r*x-r*meanx
    return y

def RegressionProcess(x,y):
    #x=[1,2,3,4]
    #y=[3,5,7,9]
    #print(mean)
    meanx=mean(x)
    meany=mean(y)
    dx=subfromlist(x,meanx,0)
    dy=subfromlist(y,meany,2)
    sumdx=listsum(dx)
    sumdy=listsum(dy)
    dxdy=multiplylist(dx,dy)
    dxdx=multiplylist(dx,dx)
    dydy=multiplylist(dy,dy)
    sumdxdy=listsum(dxdy)
    #sumdydy=listsum(dydy)
    sumdxdx=listsum(dxdx)
    """
    print("X=",x)
    print("Y=",y)
    print("Mean x=",meanx,", Mean y=",meany)
    print("dx=",dx)
    print("dy=",dy)
    print("Sum dx=",sumdx)
    print("Sum dy=",sumdy)
    print("dxdy=",dxdy)
    print("dxdx=",dxdx)
    print("dydy=",dydy)
    print("Sum dxdy=",sumdxdy)
    print("Sum dxdx=",sumdxdx)
    print("Sum dydy=",sumdydy)
    """
    n=len(x)
    r=(sumdxdy-sumdx*sumdy/n)/(sumdxdx-sumdxdx/n)
    #print(r)
    
    xy=multiplylist(x,y)
    sumxy=listsum(xy)
    sumx=listsum(x)
    sumy=listsum(y)
    sumxsumy=sumx*sumy
    sumxx=listsum(multiplylist(x,x))
    sumyy=listsum(multiplylist(y,y))
    
    num=n*sumxy-sumx*sumy
    den=((n*sumxx-sumx*sumx)*(n*sumyy -sumy*sumy))**.5
    c=num/den
    """
    print('xy=',xy)
    print("sumxy=",sumxy)
    print(sumx,sumy)
    print("Num=",num)
    print('Sumx2=',sumxx)
    print("Correlation =",c)
    """
    return r,meanx,meany,c
       
r,meanx,meany,corelation=(RegressionProcess([1,2,3,4],[-1,-2,-3,-4]))
print(corelation)
y5=equation(r,meanx,meany,5)
print("Predict Y =",y5)