two pointers
sort the array
take two pointers start and end
while start < end:
mul = arr[start] * 2
if mul == arr[end]:
return True
elif mul < arr[end]:
start += 1
else:
end -= 1
return False
​