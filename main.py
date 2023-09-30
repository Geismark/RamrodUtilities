import json
import re
from random import choice

def get_words() -> dict:
	with open('words.json', 'r') as file:
		words = json.load(file)
	return words

def parse_data(words, regex):
	valid_words = []

	for word in words:
		if re.match(regex, word):
			valid_words.append(word)
	return valid_words

def build_regex(min, max=None, repeating_characters=False):
	non_repeating = "(?:([A-Za-z])(?!.*\\1))"
	if max:
		range = f"{{{str(min)}, {str(max)}}}"
	else:
		range = f"{{{str(min)}}}"
	if repeating_characters:
		raise NotImplementedError
	return f"^{non_repeating}{range}$"

if __name__ == '__main__':
	words = get_words()
	regex = build_regex(10)
	output = parse_data(words, regex)

	print(output)
	print(f"Regex: {regex}")
	print(f"Randomly selected: {choice(output)}")
