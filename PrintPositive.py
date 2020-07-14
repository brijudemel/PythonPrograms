list1=[]
list2=[]
print("Enter elements of the list. To stop entering inputs press any letter")
while True:
	n=input()
	if not n.isalpha():
		list1.append(int(n))
	else:
		break
for i in list1:
	if i>0:
		list2.append(i)
print("Output:	",list2)
