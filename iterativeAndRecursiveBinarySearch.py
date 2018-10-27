def iterative_binary_search(target, dataList, high, low):
    for i in range(len(dataList)):
        mid = (low + high) // 2
        if dataList[mid] == target:
            return True
        elif dataList[mid] > target:
            high = mid - 1
        elif dataList[mid] < target:
            low = mid + 1
def recursive_binary_search(target, dataList, high, low):
    mid = (low + high) // 2
    if low > high:
        return False
    else:
        if target == dataList[mid]:
            return True
        elif dataList[mid] > target:
            return recursive_binary_search(target, dataList, mid - 1, low)
        elif dataList[mid] < target:
            return recursive_binary_search(target, dataList, high, mid + 1)

def main():
    dataList = [1,3,5,9,15,21,29,37,45,56,64]
    target = 56
    high = len(dataList) - 1
    low = 0

    print("Iterative:",iterative_binary_search(target, dataList, high, low))
    print("Recursive:",recursive_binary_search(target, dataList, high, low))

main()
    

    
