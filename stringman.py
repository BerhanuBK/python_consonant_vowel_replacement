con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def str_replace(word):
	length = len(con)
	for x in word:
		#print(x, word, length)
		if x in con:
			#print(x, con.index(x))
			if con.index(x) == (length - 1): 
				word = word.replace(x, con[(con.index(x)+1)-length]) 
				#print(word)
			else:
				word = word.replace(x, con[(con.index(x)+1)])
				#print(word)
	return(word)

print(str_replace("Abebe")) 
print(str_replace("zZZei"))  