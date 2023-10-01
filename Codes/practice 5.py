a=input("Enter String : ")

#method 1
print("Reversed String : ",a[::-1])

#method 2
print(''.join(reversed(a)))

#method 3
i=len(a)-1
target=""
while i>=0:
    target=target+a[i]
    i=i-1
print(target)

