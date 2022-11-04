con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vwl = ['a', 'e', 'i', 'o', 'u']
def con_str_replace(word):
	length = len(con)
	word = word.lower()
	word2 = [x for x in word]
	#print(word, word2)
	for c in range(len(word)):
		x=word[c]
		if x in con:
			if con.index(x) == (length - 1): 
				word2[c] = con[(con.index(x)+1)-length] 
			else:
				word2[c] = con[con.index(x)+1]
	return("".join(word2))

def vow_str_replace(word):
	length = len(vwl)
	word = word.lower()
	word2 = [x for x in word]
	for c in range(len(word)):
		x=word[c]
		if x in vwl:
			if vwl.index(x) == (length - 1): 
				word2[c] = vwl[(vwl.index(x)+1)-length]
			else:
				word2[c] = vwl[vwl.index(x)+1]
	return("".join(word2))
print("----------------------------------------------------")
print("Sample consonant replacement")
print("DAbebe ==>", con_str_replace("DAbebe"))
print("Abebc ==>", con_str_replace("Abebc")) 
print("zZZei ==>", con_str_replace("zZZei"))
print("----------------------------------------------------")
print("Sample vowel replacement")
print("Abebe ==>", vow_str_replace("Abebe")) 
print("zuZZei ==>", vow_str_replace("zuZZei"))

  