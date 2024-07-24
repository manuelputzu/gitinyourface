def find_substring(text, substring):
    """
    Function to find occurrences of a substring in a given text.

    Args:
        text (str): The text in which to search for the substring.
        substring (str): The substring to search for in the text.

    Returns:
        list: A list containing the indices of the occurrences of the substring in the text.
    """
    indices = []
    len_substring = len(substring)
    len_text = len(text)

    for i in range(len_text - len_substring + 1):
        if text[i:i + len_substring] == substring:
            indices.append(i)

    return indices