from pythainlp.tokenize import word_tokenize
from pythainlp.spell import NorvigSpellChecker
checker = NorvigSpellChecker()
from num2thai import num2thai
text = "ตากลมยืนตากลมตากลมๆ"
num = "4569813748917589137548931798578644.11"
print(num2thai(num))
print(word_tokenize(num2thai(num), engine="icu"))  # ['โอเค', 'บ่', 'เรา', 'รัก', 'ภาษาถิ่น']
# word_tokenize(text, engine="icu")  # ['โอ', 'เค', 'บ่', 'เรา', 'รัก', 'ภาษา', 'ถิ่น']