def binary_search(arr,num):
    lower_bound=0
    upper_bound=len(arr)-1
    while lower_bound<=upper_bound:
        middle_element=(lower_bound+upper_bound)//2
        if(num==arr[middle_element]):
            return print("Element found at index: ",middle_element)
        elif(num<arr[middle_element]):
            upper_bound=middle_element-1
        else:
            lower_bound=middle_element+1
            
    return print("Element not found")        



arr=[2, 3, 4, 10, 40]
a=int(input())

binary_search(arr,a)