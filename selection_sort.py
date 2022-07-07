def selectionSort(arr):
    min = 0
    for i in range(len(arr)):
        min = i
        for j in range(i+1 ,len(arr)):
            if(arr[j]<arr[min]):
                min = j
        if min != i:
            arr[i],arr[min] = arr[min] , arr[i]
    return arr

          
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = selectionSort(arr)
    print(result)