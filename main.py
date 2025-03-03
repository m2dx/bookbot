import sys
	
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
print(f"------------------------------------------xxx{sys.argv}")	 
from stats import word_count
from stats import number_of_charachters
from stats import sort_de_list

def get_book_text(filepath):
	with open(filepath) as text_as_string:
		return text_as_string.read()
def main():
	filepath = sys.argv[1]
	
	text_for_output = get_book_text(filepath)
	word_num = word_count(text_for_output)
	dictonary_count = number_of_charachters(text_for_output)
	to_print = sort_de_list(dictonary_count)
	#print(f"-----------{to_print}")
	#print(f"{word_num} words found in the document {dictonary_count}{to_print}")
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count(text_for_output)} total words")
	print("--------- Character Count -------")
	for eintrag in to_print:
		print(f"{eintrag["Buchstabe"]}: {eintrag["zahl"]}")

	print("============= END ===============")
if __name__ == "__main__":
	main()