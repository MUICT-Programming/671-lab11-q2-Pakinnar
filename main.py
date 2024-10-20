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

def summation(list1, list2):
    list_sum=[]
    global n
    #คือการเรียกใช้ keyword เพราะไม่สามารถส้รางใน function ได้ 
    for i in range(n):
        sum=list1[i]+list2[i]
        list_sum.append(sum)
    return list_sum
    #ค่าในการบวกกันของlist 
list_sum = summation(list1,list2)
#ต้องเอาไปคิดต่อใน function ต่อไป
def find_min_max(list):
    max=list[0]
    min=list[0]
    for i in list:
        if i>max:
            max=i
        #else:
            #continue
    for i in list:
        if i<min:
            min=i
        #else:
            #continue
    min_max=(min,max)
    return min_max
    #การหาค่าจาก min และ max 

print(summation(list1,list2))
print(find_min_max(list_sum))
