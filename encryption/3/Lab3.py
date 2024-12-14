def hash(st):
	rez = 0
	pw = 27
	for i in range(0,len(st)):
		rez = rez + ord(st[i]) * pw %  9223372036854775807 #int 64
		pw = pw * 27 
	return rez


st = ['h','e','l','l','o','w','o','r','l','d']

st2 = ['о','и','а','с','е','т','н','р','л','в','к','д','п','я','г','м','й','ы','ь','з','б','у','э','ц','ч','ю','х','ж','щ','ш','ф','ъ','ё']

st3 = ['e','l','l','o','w','o','r','l','d']

print(st)
print(hash(st))
print(st2)
print(hash(st2))
print(st3)
print(hash(st3))


