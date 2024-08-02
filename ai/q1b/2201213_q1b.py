def analyze_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        lines = text.count('\n') + 1
        words = len(text.split())
        spaces = text.count(' ')
        unique_words = set(text.split())
        word_frequency = {}
        for word in text.split():
            word_frequency[word] = word_frequency.get(word, 0) + 1
        longest_word = max(unique_words, key=len)
        total_length = sum(len(word) for word in text.split())
        average_length = total_length / words

        return {
            "total_words": words,
            "total_lines": lines,
            "total_spaces": spaces,
            "unique_words": len(unique_words),
            "word_frequency": word_frequency,
            "longest_word": longest_word,
            "average_word_length": average_length}


def compare_texts(text1, text2):
    if text1 == text2:
        return 1
    else:
        return 0


filename = "example.txt"
result = analyze_text(filename)
print("Total Words:", result["total_words"])
print("Total Lines:", result["total_lines"])
print("Total Spaces:", result["total_spaces"])
print("Unique Words:", result["unique_words"])
print("Word Frequency:", result["word_frequency"])
print("Longest Word:", result["longest_word"])
print("Average Word Length:", result["average_word_length"])

text1 = "This is a sample text."
text2 = "This is a sample text."
similarity = compare_texts(text1, text2)
print("Text Similarity:", similarity)
