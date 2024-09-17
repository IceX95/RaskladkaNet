from dictionary import *

def translate(text):
    output = ""
    for symbol in text:
        if symbol.isupper(): viewable = big_let_dictionary
        else: viewable = small_let_dictionary

        try:
            output += viewable[symbol]
        except KeyError:

            if symbol in viewable.values():
                output += list(viewable.keys())[list(viewable.values()).index(symbol)]
            else:
                output += symbol
    return output
