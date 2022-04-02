from string import punctuation

paragraph = """This is a paragraph that has punctuation.  There isn't much.  But, there is some.  Thanks for reading it!"""

translator = str.maketrans('', '', punctuation)
print(translator)

paragraph_wo_punctuation = paragraph.translate(translator).lower()
print(paragraph_wo_punctuation)