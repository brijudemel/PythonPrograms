def most_frequent(word):
	word=word.lower()
	n=[]
	l1=[]
	l2=[]
	for i in word:
		if not (i in n):
			n.append(i)
			l1.append([i,word.count(i)])
			l2.append(word.count(i))
	l2=list(set(l2))
	l2.sort(reverse=True)
	for i in l2:
		for j in l1:
			if i==j[1]:
				print(j[0]," = ",j[1])

word=input('Please Enter a string:	')
most_frequent(word)
