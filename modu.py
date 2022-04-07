def sumofdigit(no):
 
    sum=0
    while no != 0:
        dig=no%10
        sum=sum+dig
        no=no//10
    return sum
'''
def array_sort(arr):
    temp=0
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp;    
    return arr

def array_desc(arr):
    temp=0
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] < arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp;    
    return arr
'''