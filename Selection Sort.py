#This function takes a list and, using a selection sort algorithm, sorts the list in ascending order
def selectionSort(argList):

    #this loop basically positions the divider between sorted and unsorted
    for i in range(0,len(argList)):
        listMin = argList[i]
        minIndex = i #set this just to not get an error on the second if statement

        #this loop goes through the unsorted part of the list, finds the min, and swaps it to where it should be
        for j in range(i + 1,len(argList)):
            if argList[j] < listMin:
                listMin = argList[j]
                minIndex = j

        if minIndex == i:
            continue
        else:
            orig = argList[i]
            argList[i] = listMin
            argList[minIndex] = orig

    print(argList)
    #return argList
