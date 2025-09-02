import re
from collections import Counter

def main():
    paragraph = input("Enter a paragraph of text:\n")

    normalized_text = paragraph.lower()
    words = re.findall(r'\b\w+\b', normalized_text)
    total_words = len(words)

    total_chars = len(paragraph.replace(" ", ""))

    sentences = re.split(r'[.!?]+(?:\s|$)', paragraph.strip())
    sentences = [s for s in sentences if s]
    total_sentences = len(sentences)

    word_counts = Counter(words)
    most_common_word, most_common_count = word_counts.most_common(1)[0]

    print("\n--- Text Analysis Summary ---")
    print(f"Total number of words: {total_words}")
    print(f"Total number of characters (excluding spaces): {total_chars}")
    print(f"Number of sentences: {total_sentences}")
    print(f"Most frequent word: '{most_common_word}' ({most_common_count} times)")
    print("\nWord frequency (case-insensitive):")
    for word, count in word_counts.items():
        print(f"  {word}: {count}")

main()
