list = ["Anna", "Bob", "Caroline", "Don", "Ellen","Felix"]

def filterList(listToFilter):
    for item in listToFilter:
        if len(item)<4:
            listToFilter.remove(item)
    print("Filtered list is: ", listToFilter)

filterList(list)