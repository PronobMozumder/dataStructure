# n, m , k, s = list(map(int, input().split()))
# f = 0
#
# for i in range(n):
#     s1 = list(map(str, input().split()))[:m]
#     for j in range(len(s1)):
#         if s1[j] == '#':
#             break
#         elif s1[j] == '*' :
#             s += 4
#             f = 1
#         elif s1[j] == "." :
#             if s1[j-1] == "*" and f==1:
#                 s+=-2
#             else:
#                 s += -3
#     print("\n",s)
#     f=0
#
# if s>=k:
#     print("Yes")
#     print(s)
# else:
#     print("No")



n, m , k, s = list(map(int, input().split()))
res = False

for i in range(n):
    s1 = list(map(str, input().split()))[:m]
    if s>=k:
        for j in range(len(s1)):
            if s >= k:
                res = True
                if s1[j] == '#':
                    break
                elif s1[j] == '*':
                    if j == (len(s1) - 1):
                        s += 5
                    else:
                        s += 4
                elif s1[j] == ".":
                    if j == (len(s1) - 1):
                        s += -2
                    else:
                        s += -3
            else:
                res = False
                break
    else:
        res = False
        break

if res == True:
    print("Yes")
    print(s)
else:
    print('No')




