#given a list in ascending order, locates the desired item's index with a recursive binary search algorithm
#if item is not in the list, returns -1 instead
def binarySearch(argList,low,high,item):

    mid = (low + high) // 2 #locates the middle item in the current part of the list the program is searching in

    if high >= low: #if  high becomes lower than low, or visa versa, then item is not in the list
        
        if argList[mid] == item: #base case is when the middle is the desired item's index
            return mid

        elif argList[mid] > item: #if item is in the lower half of the current part of the list
            high = mid - 1 #middle is not the item, and it is lower than mid, so mid - 1 is the new high
            return binarySearch(argList,low,high,item)

        elif argList[mid] < item: #if item is in the upper half of the current part of the list
            low = mid + 1 ##middle is not the item, and it is higher than mid, so mid + 1 is the new low
            return binarySearch(argList,low,high,item)
    else: 
        return -1

#main is just to test the binarySearch function
def main():
    argList = []
    for i in range(0,1000):
        argList.append(i)

    item = int(input("Enter item you want to search for in list(0 to 999 in default list): "))

    index = binarySearch(argList,0,len(argList)-1,item)

    if index == -1:
        print("The item is not in the list.")
    else:
        print("The item is at index", index,end=".")
main()
