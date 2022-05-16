def printsubarrays(arr, start, end):
    if end== len(arr):
        return 

    elif start>end:
        return printsubarrays(arr, 0, end+1)
    
    else:
        print(arr[start:end+1])
        return printsubarrays(arr, start+1, end)

arr=[1,2,3]
printsubarrays(arr,0,0)