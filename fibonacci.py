n=int(input("Enter the length of the Fibonacci series: "))
if n==1:
	print ("0")
elif n==2:
	print("0	1")
else:
	f=0
	s=1
	print("0	1",end="\t")
	i=0
	while i<n-2:
		print((f+s),end="\t")
		f,s=s,f+s
		i+=1
