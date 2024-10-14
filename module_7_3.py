from pprint import pprint

file_names = 'test_file.txt'
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuation:
                        line = line.replace(symbol, '' if symbol != ' - ' else ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        result_ = {}
        for i, word_ in self.get_all_words().items():
            result_[i] = word_.count(word.lower())
        return result_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
