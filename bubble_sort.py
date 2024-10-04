# def bubble_sort(l):
#     le = len(l)
#     for i in range(le):
#         swapped = False
#         for j in range(0,le-i-1):
#             if l[j]>l[j+1]:
#                 temp = l[j]
#                 l[j] = l[j+1]
#                 l[j+1] = temp
#                 swapped = True
#         if not swapped:
#             break

# input_list = input("Enter a list of numbers separated by spaces: ").split()
# l = [int(x) for x in input_list]
# bubble_sort(l)
# print("Sorted list : ",l)

# try:
#     if '1'!=1:
#         raise "SomeError"
#     else:
#         print("No error occurred")
# except:
#     print("SomeError has occurred")


my_dict = dict.fromkeys(['a','b'],0)
d = {key:0 for key in ['a','b']}

print(my_dict)
print(d)