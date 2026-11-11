#True
#False

x = True

m = 10
n = 5
r = 2
p = 12

if m > n and p < r: 
    print("Ok")
else:
    print("m no es mayor")

if m > n or p < r: 
    print("Ok")
else:
    print("m no es mayor")
#                                        v
#                         v             and        v
#               v         or     f      and        v
#       v      and    v   or     f      and    v   or  f
if (m < p > r) and (m < p or m > p + 3) and (m < p or n > p):
    pass