"""Module providing functions to translate from english to french and vice-versa."""
from deep_translator import MyMemoryTranslator

def english_french(english_text):
    '''Takes in an english word, returns the equivalent word in french'''
    french_text = english_text.translate(MyMemoryTranslator)
    return french_text

def french_english(french_text):
    '''Takes in a french word, returns the equivalent word in english'''
    english_text = french_text.translate(MyMemoryTranslator)
    return english_text