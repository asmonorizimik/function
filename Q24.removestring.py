# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# x = []
# def reemovNestings(l):
#     for i in l:
#         if type(i) == list:
#             reemovNestings(i)
#         else:
#             x.append(i)
# print ('The original list: ', l)
# reemovNestings(l)
# print ('The list after removing nesting: ', x)
