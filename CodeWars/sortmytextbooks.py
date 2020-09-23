def sorter(textbooks):
    textbooks.sort(key=str.casefold)
    return textbooks   