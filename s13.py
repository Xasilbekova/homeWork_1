def mySort(lst):
    newDict = {}
    for i in lst:
        total = sum(int(digit) for digit in str(i))
        if total not in newDict:
            newDict[total] = [i]
        else:
            newDict[total].append(i)

    newLst = []
    for j in sorted(newDict.keys()):
        newLst.extend(sorted(newDict[j]))

    return newLst
try:
    lst = input("Raqamlarni kiritng: ").split()
    lst = [int(x) for x in lst]
    print(mySort(lst))
except:
    print("Faqat butun son kiriting!")


