import nltk
from nltk import word_tokenize
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import os
import datetime

def find_patterns(text, token_length, filter_periods, special_chars):
    tokens = word_tokenize(text)
    ngrams = nltk.ngrams(tokens, token_length)
    if filter_periods or special_chars:
        def is_valid_ngram(ngram):
            for token in ngram[:-1]:
                if token == '.' and not filter_periods:
                    continue
                if any(char in token for char in special_chars):
                    return False
            return True
        ngrams = [ngram for ngram in ngrams if is_valid_ngram(ngram)]
    pattern_counts = Counter(ngrams)
    return pattern_counts

def save_results(pattern_counts, filename):
    with open(filename, 'w') as file:
        for pattern, count in pattern_counts.items():
            file.write(f"{' '.join(pattern)}: {count}\n")

def visualize_top_patterns(pattern_counts, top_n=20):
    most_common = pattern_counts.most_common(top_n)
    patterns = [' '.join(pattern) for pattern, count in most_common]
    counts = [count for pattern, count in most_common]

    plt.figure(figsize=(10, 8))
    plt.barh(patterns, counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.title('Top Patterns')
    plt.gca().invert_yaxis()
    plt.show()

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main(file_path):
    text = read_text(file_path)

    token_length = int(input("Enter the initial token length: "))
    filter_periods = input("Do you want to filter out patterns with periods (except at the end)? (y/n): ").lower() == 'y'
    special_chars = input("Enter any special characters or punctuation marks to filter out (leave empty if none): ")
    base_filename = datetime.datetime.now().strftime("%B%d%Y")

    while True:
        pattern_counts = find_patterns(text, token_length, filter_periods, special_chars)
        visualize_top_patterns(pattern_counts)

        print("Top 20 Patterns:")
        for pattern, count in pattern_counts.most_common(20):
            print(f"{' '.join(pattern)}: {count}")

        save_choice = input("Would you like to save the results? (y/n): ")
        if save_choice.lower() == 'y':
            part_num = 0
            filename = f"{base_filename}.txt"
            while os.path.exists(filename):
                part_num += 1
                filename = f"{base_filename}_part{part_num}.txt"
            save_results(pattern_counts, filename)
            print(f"Results saved to {filename}")

        continue_choice = input("Would you like to change the token length and find more patterns? (y/n): ")
        if continue_choice.lower() == 'y':
            token_length = int(input("Enter the new token length: "))
            filter_periods = input("Do you want to filter out patterns with periods (except at the end)? (y/n): ").lower() == 'y'
            special_chars = input("Enter any special characters or punctuation marks to filter out (leave empty if none): ")
        else:
            exit_choice = input("Press any key to exit or 'c' to continue: ")
            if exit_choice.lower() != 'c':
                print("Exiting the program.")
                break

if __name__ == "__main__":
    filepath = r"C:\Users\magla\Downloads\mobydick.txt"

    main(filepath)


# def read_text(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()
#
# def main(file_path):
#     text = read_text(file_path)