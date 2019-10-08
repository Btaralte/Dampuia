# Author: Lalbiakthuama, Btech, 2nd year, Civil Engineering,IIT KGP
import numpy as np 
def row(arr,val):
	i = len(arr)-1
	while i >= 0:
		if val in list(arr[i]):
			break
		i = i-1
	return i
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
arr = [primary]   
print(rel)
print("")
print(nodes)
print("")
print(arr)
print("-----------------------------------------------------------------------")
copy = []
empty_array = ['xx']*len(arr[0])
for i in range(0,2*len(nodes)):
	arr.append(empty_array)
arr = np.array(arr,dtype = 'object')	
for i in range(0,len(nodes)):
	insert = nodes[i]
	print(i)
	print("Insert_tur = "+insert)
	
	if len(rel[insert])==1:
		inputt = rel[insert][0]
		k = row(arr,inputt)
		r = list(arr[k]).index(inputt)
		kk = k+1
		while arr[kk][r]!='xx':
			kk = kk+1
		print("kk = "+str(kk))    
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
		while arr[kk][i1]!='xx':
			kk = kk+1


		if i1 == i2:
			arr[kk][i2] = insert
		else:
			copy.append(input2)
			arr[kk][i1] = input2
			kk = kk+1
			while arr[kk][i1]!='xx':
				kk = kk+1
			arr[kk][i1] = insert			

#Appearing later critical lines	 
	print(arr)            
	print("-----------------------------------------------------------------------------------")
arr = list(arr)
final_arr = []
for i in range(len(arr)):
	final_arr.append(arr[i])
	if all(arr[i]==empty_array):
		break	                               
final_arr = np.array(final_arr)
final_arr = final_arr.transpose()
print(final_arr)
print("Copy = "+str(copy))










