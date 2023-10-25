
def bin_search(arr: list, elem):
    l = 0
    r = len(arr)
    length = len(arr)
    
    while l <= r:
        mid = l + (r - l) // 2
        
        if mid >= length:
            break
        
        if elem == arr[mid]:
            return True
        elif elem > arr[mid]:
            l = mid + 1
        elif elem < arr[mid]:
            r = mid - 1
            
    return False
    


def main():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    ans = {True: "Yes", False: "No",}
    
    print("Arr:", arr)
    
    print()
    print("Range test:")
    for i in range(0, 100):
        print("is {n} in arr? - {a}".format(n=i, a=ans[bin_search(arr, i)]))
        
    print()
    print("Same elements test:")
    for i in arr:
        print("is {n} in arr? - {a}".format(n=i, a=ans[bin_search(arr, i)]))
    
if __name__ == "__main__":
    main()
