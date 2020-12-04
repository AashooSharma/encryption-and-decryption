def asreplace (A0):
	
	A1= A0.replace('a','˦')
	A2= A1.replace('b','΅')
	A3= A2.replace('c','¬')
	A4= A3.replace('d','¤')
	A5= A4.replace('e','¶')
	A6= A5.replace('f','Ħ')
	A7= A6.replace('g','Ŧ')
	A8= A7.replace('h','ȶ')
	A9= A8.replace('i','ǂ')
	A10= A9.replace('j','ϫ')
	A11= A10.replace('k','ð')
	A12= A11.replace('l','༆')
	A13= A12.replace('m','፹')
	A14= A13.replace('n','༗')
	A15= A14.replace('o','༇')
	A16= A15.replace('p','༉')
	A17= A16.replace('q','༖')
	A18= A17.replace('r','༜')
	A19= A18.replace('s','༤')
	A20= A19.replace('t','༺')
	A21= A20.replace('u','༅')
	A22= A21.replace('v','ༀ')
	A23= A22.replace('w','༻')
	A24= A23.replace('x','༕')
	A25= A24.replace('y','༞')
	A26= A25.replace('z','༟')
	return A26

def assr (B0):
	
	B1= B0.replace('˦','a')
	B2= B1.replace('΅','b')
	B3= B2.replace('¬','c')
	B4= B3.replace('¤','d')
	B5= B4.replace('¶','e')
	B6= B5.replace('Ħ','f')
	B7= B6.replace('Ŧ','g')
	B8= B7.replace('ȶ','h')
	B9= B8.replace('ǂ','i')
	B10= B9.replace('ϫ','j')
	B11= B10.replace('ð','k')
	B12= B11.replace('༆','l')
	B13= B12.replace('፹','m')
	B14= B13.replace('༗','n')
	B15= B14.replace('༇','o')
	B16= B15.replace('༉','p')
	B17= B16.replace('༖','q')
	B18= B17.replace('༜','r')
	B19= B18.replace('༤','s')
	B20= B19.replace('༺','t')
	B21= B20.replace('༅','u')
	B22= B21.replace('ༀ','v')
	B23= B22.replace('༻','w')
	B24= B23.replace('༕','x')
	B25= B24.replace('༞','y')
	B26= B25.replace('༟','z')
	return B26
	
print ("0) encryption        1) decryption ")
Z0 = input ("choose a method => ")



if Z0 == "0" :
		A0 = input("Enter your massage: \n ")
		C0 = asreplace(A0)
		
		
elif Z0 == "1" :
		B0 = input("Enter your code: \n ")
		C0 = assr(B0)
		
		
else :
		C0 = "worng input method "
		
		

 	
b= C0
print( b)


