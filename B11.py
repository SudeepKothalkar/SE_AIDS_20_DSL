'''a)Write a Python program to store roll numbers of student in array who attended a training program in random order.Write function for searching whether particular student attended training program or not, using linear search and sentinel search
b) Write a Python program to store roll numbers of student array who attended training program in sorted order.Write function for searching whether particular student attended training program or not,using binary search and fibonacci search.'''
a=[]

def insert(a):
    n=int(input("Enter total number of students: "))
    for i in range(n):
        x = int(input("Enter the roll number of the students : "))
        a.append(x)
    print(a)

def sorted_List(a):
    for i in range (len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
                a[i], a[min] = a[min], a[i]
    print(a)
        
def linear_ser():
    x=int(input("Enter the roll no"))
    index=0
    for i in a:
        if i==x:
            print("Student have Attended Training")
            print("At index",index)
        else:
            index+=1
    if(index==len(a)):
        print("Student Not attended training")
# def sentinel():
        
def binary_search():
    n=int(input("Search element:"))
    first=0
    last=len(a)-1
    mid=0
    while(first <= last):
        mid=int((first+last)/2)
        if(n==a[mid]):
            print("Search element found at index",mid)
            break
        elif(n>a[mid]):
            first=mid+1
        else :
            last =mid-1
fibo = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fibonacci_Search():
    print("\n Sorted List: ", a)
    print("\n Fibonacci Series: ", fibo)
    key = int(input("\n\t Enter Roll No to search: "))
    k = 0 #....... To find fibo(k) >= Size of Sorted List
    while fibo[k] < len(a):
        k += 1   #....... Offset = -1
        offset = -1
    while k > 0: #.......Find index i = min((offset + fibo[k-2]) , size-1)
        i = min((offset + fibo[k-2]) , len(a)-1)
        if key == a[ i ]:
            print("\t Student Have Attended Training Program.")
            print("At index =",i)
            break
        elif key >a[ i ]:
            k = k-1
            offset = i
        else:
            k = k - 2
        if k <= 0:
            print("\t Student Have Not Attended Training Program.")
         
choice = 0
while(choice <= 6):  
    print("\n--------** MENU **-------- \n 1. Insert roll number. \n 2. Linear Search \n 3. Sentinel Search \n 4. Binary Search \n 5. Fibonacci Search \n 6. STOP/EXIT")
    choice = int(input("\n\t Enter your Choice(1/2/3/4/5/6): "))
    if choice==1:
        insert(a)
    elif choice == 2:
        linear_ser()
    # elif choice == 3:
    #     # sentinel()
    elif choice == 4:
        sorted_List(a)
        binary_search()
    elif choice == 5:
        fibonacci_Search()
    elif choice==6:
        exit(0)
    else: 
        print("Enter valid choice")

