# -*- coding: utf-8 -*-

import requests
import re
import urllib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def binary_word_search(string, data):
    """A simple binary search algorithm to check if string exists in data."""
    string = str(string)
    if len(data) == 0:
        return False
    mid = len(data)//2
    if data[mid] == string:
        return True
    elif string < data[mid]:
        data = data[:mid]
    else:
        data = data[mid+1:]
    return binary_word_search(string, data)


def check_word(string):
    """ Checks if a given string of characters is a playable word
in the Polish version of Scrabble. """

    string = string.strip().lower()

    if not string.isalpha():  # Incorrect format
        return "Wygląda na to, że to nie jest prawidłowe słowo!"
    path = "./sorted_words/"
    filename = path+"words_"+string[0]
    with open(filename, 'r') as wfile:
        words = wfile.readlines()
        # This is where the magic happens!
        correct = binary_word_search(string+'\n', words)
        return parse_word_response(string, correct)


def parse_word_response(word, correct):
    word = word.capitalize()
    if correct:
        output = bcolors.BOLD + bcolors.OKGREEN + \
            word + bcolors.ENDC + " to prawidłowe słowo!\n"
        return '\n'.join((output, request_definition(word)))
    else:
        return (bcolors.BOLD + bcolors.FAIL + word +
                bcolors.ENDC + " nie jest słowem dopuszczalnym w Scrabble!\n")


def request_definition(word):
    """ Connects to sjp.pl and tries to define a given word
using regular expressions to find the definition."""
    word_url = "https://sjp.pl/"+word
    try:
        page = requests.get(word_url, timeout=5)
        if not page:
            return "Nie udało się połączyć z serwerem."
    except Exception:
        return ("Wystąpił błąd przy szukaniu definicji słowa. " +
                "Prawdopodobnie nie jesteś połączony z internetem.")

    #  Sorry for the ugly regexes!
    regex_def = r"(?<=(<p style=\"margin: .5em 0; font: medium/1.4 sans-serif; max-width: 32em; \">)).*(?=</p>)"
    regex_redirect = r"(?<=(<p style=\"margin: .5em 0; \">\<span class=\"lc\"> &rarr;</span> <a href=\"/)).*(?=\">)"
    regex_word = r"(?<=(\"lc\" href=\"/)).*?(?=\")"

    word_match = re.search(regex_word, page.text)
    def_match = re.search(regex_def, page.text)

    if word_match and def_match:
        word = urllib.parse.unquote(word_match.group()).capitalize()
        define = def_match.group().replace('<br />', '\n').replace("&quot;", "\"")

        output = bcolors.BOLD + bcolors.HEADER + \
            word + bcolors.ENDC + '\n'
        output += define
        return output

    redirect_match = re.search(regex_redirect, page.text)
    if redirect_match:
        return request_definition(redirect_match.group())
    return "Niestety www.sjp.pl nie podaje definicji tego słowa :("


#  Loop for convenience!
while True:
    string = input(bcolors.HEADER +
                   "\nWpisz słowo aby je sprawdzić!"+bcolors.ENDC+"\n>")
    print(check_word(string))
