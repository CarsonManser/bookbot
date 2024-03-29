def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
        num_words = word_count(text)
        num_letters = letter_count(text)
        ordered = sorter(num_letters)
        results = report(path, num_words, num_letters, ordered)


def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    #print(count)
    return count

def letter_count(text):
    lower_case = text.lower()
    character_count = {}
    for c in lower_case:
        if c in character_count and c.isalpha():
            character_count[c] += 1
        elif c.isalpha():
            character_count[c] = 1
    return character_count

def sorter(num_letters):
    ordered = []
    for c in num_letters:
        key = c
        value = num_letters[c]
        key_pair = {"key": key}
        key_pair["value"] = value
        ordered.append(key_pair)
    ordered.sort(reverse=True, key=lambda d: d["value"])
    return ordered

def report(path, num_words, num_letters, ordered):
    print(f"--- Begin Report of {path} ---")
    print(f"There are {num_words} words in the document.")
    print("")
    for i in range(0, len(ordered)):
        test = ordered[i].values()
        test = list(test)
        print(f"There are {test[1]} instances of the {test[0]} character")
    print("--- End of Report ---")

main()
