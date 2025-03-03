def word_count(text_for_output):
	word_num = 0
	words = text_for_output.split(None,-1)
	for word in words:
		word_num += 1
	return word_num

def number_of_charachters(text_for_output):
	word_dic = {}
	words_low = text_for_output.lower()
	
	
	for word_low in words_low:
		
		if word_low not in word_dic:
			word_dic[word_low] = 1
		else:
			word_dic[word_low] += 1

	#print(f"anzahl_buchstabe{word_dic}")
	return word_dic
def sort_de_list(dictonary_count):
	word_dic_sorted = []
	for buchstabe, zahl in dictonary_count.items():
		sorted_dic = {"Buchstabe":buchstabe ,"zahl":zahl}
		word_dic_sorted.append(sorted_dic)
	def sortiere_nach(dictonary_count):
		return dictonary_count["zahl"]
	word_dic_sorted.sort(reverse=True, key=sortiere_nach)
	#word_dic_sorted = []
	#word_dic_sorted.sort(dictonary_count_list)
	#print(f"-----{sorted_dic}")
	return word_dic_sorted
