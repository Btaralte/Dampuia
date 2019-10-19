# Author: Lalbiakthuama, Btech, 2nd year, Civil Engineering,IIT KGP
import numpy as np 
def transpose(matrix):
	r_matrix = []
	k = max(list(map(len,matrix)))
	for i in range(k):
		temp = []
		for j in range(len(matrix)):
			if len(matrix[j])>=(i+1):
				temp.append(matrix[j][i])
		r_matrix.append(temp)
	return r_matrix
def row(arr,val):
	i = len(arr)-1
	while i >= 0:
		if val in list(arr[i]):
			break
		i = i-1
	return i
def column3(arr,val):
	for i in range(len(arr)):
		if val in arr[i]:
			break
	return i 		
def row2(arr,val,i):
	j = 0
	k = 0
	while j<i:
		if val in arr[j]:
			k = j
		j = j+1	
	return k
def check(arr,k):
	x = False
	if len(arr)==0:
		return x
	for i in range(len(arr)):
		if k in arr[i]:
			x = True
			break
	return x			
def func(arr):
	x = []
	for i in range(len(arr)):
		key = arr[i]
		if check(x,key):
			continue
		temp = []	
		for j in range(len(arr)):
			if key==arr[j]:
				temp.append(key)
		if len(temp)>1:
			x.append(temp)		
	y = []
	for i in range(len(x)):
		y.append(len(x[i]))
	return y				
lol = int(input("Enter the number of levels:"))	
rel = {}    
nodes = []
primary = []    
file_name = input("Enter the name of the file:").strip()
file1 = open(file_name,'r')
l = file1.readlines()
for i in range(len(l)):
	s = l[i]
	s = s.strip().replace(" ","")
	a = ''
	b = ''
	c = ''
	for j in range(len(s)):
		if s[j]==")" or s[j]=="\n":
			break
		if s[j] == "=" or s[j] == "(" or s[j]=="'" :
			continue
		if j < s.index("="):
			a = a+s[j]
		elif j < s.index("'"):
			b = b+s[j]
		else:
			c = c + s[j]
	nodes.append(a)
	if c == '':
		rel[a]=(b,)
	else:
		rel[a]=(b,c,)
	if b[0]=='x' and b not in primary:
		primary.append(b)
	if c!='' and c not in primary and c[0]=='x':
		primary.append(c)
for i in range(1,len(primary)):
	j = i-1
	key = primary[i]
	key1 = int(key[1:])
	while j >=0 and key1 < int(primary[j][1:]):
		primary[j+1] = primary[j]
		j = j-1
	primary[j+1] = key	
level = [[]]
for i in range(len(primary)):
	level[0].append(primary[i])
for i in range(1,lol):
	temp_array1	= []
	for node in nodes:
		x = rel[node]
		if len(x)==1:
			xx = row(level,x[0])
			if xx!=-1 and xx==(i-1):
				temp_array1.append(node)
		else:
			xx1 = row(level,x[0])
			xx2 = row(level,x[1])
			xx = max(xx1,xx2)
			if xx1!=-1 and xx2!=-1  and xx==(i-1):
				temp_array1.append(node)		
	level.append(temp_array1)
print("")	
print("Level 0 = "+str(level[0]))	
nodes1 = []			
for i in range(1,len(level)):
	print("Level "+str(i)+"= "+str(level[i]))
	for j in level[i]:
		nodes1.append(j)	
arr = [primary]   
copy = []
empty_array = ['']*len(arr[0])
for i in range(0,2*len(nodes1)):
	arr.append(empty_array)
arr = np.array(arr,dtype = 'object')	
for i in range(0,len(nodes1)):
	insert = nodes1[i]
	if len(rel[insert])==1:
		inputt = rel[insert][0]
		k = row(arr,inputt)
		r = list(arr[k]).index(inputt)
		kk = k+1
		while arr[kk][r]!='':
			kk = kk+1    
		arr[kk][r] = insert        
	else:
		input1 = rel[insert][0]
		input2 = rel[insert][1]
		k1 = row(arr,input1)
		k2 = row(arr,input2)
		i1 = list(arr[k1]).index(input1)
		i2 = list(arr[k2]).index(input2)
		k = max(k1,k2)
		kk = k+1
		while arr[kk][i2]!='':
			kk = kk+1
		if i1 == i2:
			arr[kk][i2] = insert
		else:
			copy.append(input1)
			arr[kk][i2] = input1
			kk = kk+1
			while arr[kk][i2]!='':
				kk = kk+1
			arr[kk][i2] = insert			

#Appearing  later and earlier critical lines	 
arr = list(arr)
final_arr = []
for i in range(len(arr)):
	final_arr.append(arr[i])
	if all(arr[i]==empty_array):
		break
real_final = final_arr		                               
final_arr = np.array(final_arr)
final_arr = final_arr.transpose()
final_arr = list(final_arr)
row1 = len(final_arr)
column = []
copy_with_primary = []
copy_without_primary = []
for i in copy:
	if i not in primary:
		copy_without_primary.append(i)
	if i in primary:
		copy_with_primary.append(i)
print("")
for i in range(len(final_arr)):
	print("-"*(len(nodes)+len(copy))*8)
	print("| ",end = "")
	column1 = 0
	for j in range(len(final_arr[i])):
		if final_arr[i][j]=='':
			continue
		if final_arr[i][j] in copy_without_primary:
			c = column3(arr,final_arr[i][j])
			if c!=j:
				print(final_arr[i][j]+"c"+" "*(5-len(final_arr[i][j]))+"| ",end = "")
			else:
				print(final_arr[i][j]+" "*(5-len(final_arr[i][j]))+"| ",end = "")	
				
		else:
			print(final_arr[i][j]+" "*(5-len(final_arr[i][j]))+"| ",end = "")
		column1 = column1+1
	column.append(column1)	
	print("")
column2 = max(column)	
print("-"*(len(nodes)+len(copy))*8)
print("")	
print("Copy = "+str(copy))
	
print("")
print("Copy without primary input = "+str(copy_without_primary))	
time_steps = len(nodes)+2*len(copy_without_primary)+len(copy_with_primary)+len(primary)	
sum1 = 0
p = 0
real_final = np.array(real_final)
real_final = real_final.transpose()
real_final1 = []
for i in range(len(list(real_final))):
	gg = []
	for j in range(len(list(real_final[i]))):
		if real_final[i][j]=='':
			continue
		gg.append(real_final[i][j])
	real_final1.append(gg)
real_final = list(real_final)
real_final = list(map(list,real_final))
real_final = transpose(real_final)
real_final1 = transpose(real_final1)
print(real_final)
print(real_final1)		
for i in range(1,len(real_final1)):
	col_vector = list(real_final1[i])
	temp = []
	for j in range(len(col_vector)):
		if col_vector[j][0]=='x':
			continue
		kk = rel[col_vector[j]]
		if len(kk)==1:
			inputt = kk[0]
			d = row2(real_final1,inputt,i)
			if d<i:
				temp.append((d,))
		else:
			input1 = kk[0]
			input2 = kk[1]
			d1 = row2(real_final1,input1,i)
			d2 = row2(real_final1,input2,i)
			if d1 < i and d2 < i:
				temp.append((d1,d2,))
	key = func(temp)
	print(temp)
	print(key)
	p = p+len(key)
	if len(key)!=0:
		for i in range(len(key)):
			sum1 = sum1+key[i]
print(sum1)
print(p)			
time_steps = time_steps-sum1+p
print("")
print("Row x Column : "+str(row1)+" x "+str(column2))
print("")
print("Timesteps = "+str(time_steps))








