# YOUR CODE HERE
# YOUR CODE HERE
list1=[]
list2=[]
n=int(input())

for i in range(n):
    a=int(input())
    list1.append(a)

for i in range(n):
    a=int(input())
    list2.append(a)

def summation(a, b):
    list_sum=[]
    global n
    for i in range(n):
        sum=a[i]+b[i]
        list_sum.append(sum)
    return list_sum

list_sum = summation(list1,list2)

def find_min_max(a):
    max=a[0]
    min=a[0]
    for i in a:
        if i>max:
            max=i
        else:
            continue
    for i in a:
        if i<min:
            min=i
        else:
            continue
    min_max=(min,max)
    return min_max

print(summation(list1,list2))
print(find_min_max(list_sum))
