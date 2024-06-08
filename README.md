# Text Pattern Finder and Variations Generator

## Overview

This project aims to develop an application that identifies frequent text patterns within a given text corpus based on a user-assigned length of tokens. The application allows users to adjust the token length to find more or fewer patterns. Once the patterns are identified, it provides an option to generate variations of these patterns using an AI instance function, although this functionality is not automatically executed. Instead, the program returns statistical results, visualizes the top 20 patterns, and provides a text summary for them. Users can choose to save these findings or proceed with generating variations.

## NLTK Library

The Natural Language Toolkit (NLTK) is a powerful library in Python used for working with human language data (text). It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.

### History of NLTK

NLTK was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania. It was created to provide a platform for building Python programs to work with human language data. Since its inception, NLTK has become one of the most popular and widely used libraries for natural language processing (NLP).

### Capabilities of NLTK

NLTK can perform a variety of tasks, including but not limited to:
- Tokenization: Splitting text into words or sentences.
- Stemming and Lemmatization: Reducing words to their root forms.
- Part-of-Speech Tagging: Labeling words with their part of speech.
- Named Entity Recognition: Identifying entities such as names, dates, and locations in text.
- Text Classification: Categorizing text into predefined categories.
- Parsing: Analyzing the grammatical structure of sentences.
- Corpus Management: Accessing and utilizing large text corpora.

## Detailed Solution

The solution consists of several functions that work together to achieve the desired functionality:

### 1. `find_patterns`

```python
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
```

This function tokenizes the input text and generates n-grams of the specified token length. It filters out n-grams containing specified special characters or punctuation marks (except periods at the end) if the user chooses to do so. It then counts the occurrences of each n-gram and returns a `Counter` object with the pattern counts.

### 2. `save_results`

```python
def save_results(pattern_counts, filename):
    with open(filename, 'w') as file:
        for pattern, count in pattern_counts.items():
            file.write(f"{' '.join(pattern)}: {count}\n")
```

This function saves the pattern counts to a text file with the specified filename. Each pattern and its count are written to the file.

### 3. `visualize_top_patterns`

```python
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
```

This function visualizes the top `n` patterns using a horizontal bar chart. The patterns are displayed along the y-axis, and their frequencies are displayed along the x-axis. The chart is generated using `matplotlib`.

### 4. `read_text`

```python
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
```

This function reads the text from a file and returns it as a string. It uses UTF-8 encoding to ensure proper handling of various characters.

### 5. `main`

```python
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
```

The `main` function orchestrates the entire process. It reads the input text, prompts the user for various options, and calls the other functions to find patterns, visualize them, and save results if desired. It also allows users to change the token length and find more patterns in a loop until they choose to exit.

## Use Cases

This code can be used in various contexts, including:

- **Literary Analysis**: Identifying recurring phrases or motifs in literary texts.
- **Marketing**: Analyzing customer reviews to find common phrases and sentiments.
- **Content Creation**: Detecting overused phrases in content to improve diversity.
- **Academic Research**: Studying linguistic patterns in large text corpora.

## Business Implementations

In a business context, this code can be used for:

- **Customer Feedback Analysis**: Identifying common themes and issues in customer feedback.
- **Brand Monitoring**: Detecting frequently mentioned phrases in social media posts about a brand.
- **SEO Optimization**: Finding commonly used phrases in competitor content to enhance SEO strategies.

## Future Enhancements

To make this code even more powerful, consider the following enhancements:

- **Integration with More NLP Libraries**: Incorporate other NLP libraries like SpaCy or GPT for more advanced text analysis and pattern generation.
- **GUI Implementation**: Develop a graphical user interface to make the tool more user-friendly.
- **Advanced Filtering**: Implement more sophisticated filtering options, such as excluding stop words or specific parts of speech.
- **Pattern Clustering**: Group similar patterns together to provide higher-level insights.
- **Real-time Analysis**: Enable real-time text analysis for applications like live social media monitoring.

## Conclusion

This project leverages the NLTK library to identify and analyze frequent text patterns in a corpus. It provides a flexible and user-friendly way to explore textual data and derive meaningful insights. With potential applications in various fields, this tool can be a valuable asset for researchers, marketers, and content creators alike. 

