# def larg(largest):
#     num=max(largest)
#     return num

    
# largest = [3, 5, 7, 34, 2, 89, 2, 5]
# num=larg(largest)
# print(num)


def large(largest):
    i = 0
    lar=0
    while i < len(largest):
        if largest[i] > lar:
            lar = largest[i]
        i = i+1
    return lar
largest=[3, 5, 7, 34, 2, 89, 2, 5]
lar=large(largest)
print(lar)