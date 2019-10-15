arr = [1,2,3,4,5,6,7,8]

# for loop with conditions
for i in range(len(arr)):
    if i > 7:
        break
    elif i in [3,4]:
        print i
    else:
        continue;

st = ""
for val in arr:
    st = st + str(val)

print st