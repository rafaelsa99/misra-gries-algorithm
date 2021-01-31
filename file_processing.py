"""file_processing.py: Module for processing the text file."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"


def get_data_stream(filename):
    """Process the file contents to get only the letters."""
    data = ""
    for char in get_file_content(filename):
        if char.isalpha():
            data += char.lower()
    return data


def get_file_content(filename):
    """Read and return the file contents."""
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content


def write_dict_to_file(filename, dic):
    """Write a dictionary to file."""
    with open(filename, 'w') as file:
        file.write(str(dic))
