## Using while loop

t=int(input())
while(t):
	t=t-1
	s1=input()
	s2=input()
	s3=s1[::-1]
	if s1 in s2:
		print("YES")
	elif s3 in s2:
		print("YES")
	else:
		print("NO")

## Using for loop

a = int(input())
for i in range(a):
    b = input()
    c = input()
    if (b in c) or (b[::-1] in c):
        print("YES")
    else:
        print("NO")