
def Quick_Sort(elements):
    """Sort the elements by using Quick Sort."""

    less = []
    equal = []
    greater = []

    if len(elements) > 1:
        pivot = elements[0]
        for x in elements:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
                
        return Quick_Sort(less)+equal+Quick_Sort(greater)  
    
    else:  
        return elements



elements=[12,4,5,6,7,3,1,15]
output = Quick_Sort(elements)

print('Given', elements)
print('Quick_Sorted',output)

