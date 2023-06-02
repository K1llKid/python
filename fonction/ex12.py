def ChangeCar(ch,ca1,ca2,debut=0,fin=0):
	if fin==0:
		fin=len(ch)
	ch2=""
	for i in range(len(ch)):
		if ch[i]==ca1 and i>= debut and i<fin:
			ch2=ch2+ca2
		else :
			ch2=ch2+ch[i]
	return ch2

# PP
phrase = 'Ceci est une toute petite phrase.'
print(ChangeCar(phrase,' ','*'))