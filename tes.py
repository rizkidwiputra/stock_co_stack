# barang = ["hp", "laptop", "hp", "tv", "hp", "tv"]
# tes = []

# barang.sort()

# # print(barang)

# def rekur(lis):
#     if len(lis) <= 1:
#         return lis 
#     else:
#         for i in range(len(lis)-2):
#             if lis[i] == lis[i+1]:
#                 tes.append(lis[i])
#                 lis.pop(i)

# rekur(barang)
# print(barang)
# print(tes)
# for u in range(len(barang)):
#     pass
# for i in range(len(barang)-1):
#     if barang[0] == barang[i+1]:
#         tes.append([barang[i+1]])
# print(tes)


# tes.append(barang[1])
# barang.pop(1)

# print(barang)
# print(tes)


a = ["TV", "Laptop", "TV"]
b = set(a)
print(b)
for i in b:
    jum = 0
    for j in a:
        if i == j:
            jum += 1
    print(i, jum)


# print(c)