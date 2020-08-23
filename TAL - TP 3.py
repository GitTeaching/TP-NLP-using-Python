
# Arabic Transliteration based on Buckwalter
# dictionary source is buckwalter2unicode.py http://www.redhat.com/archives/fedoraextras-
# commits/2007-June/msg03617.html

buck2uni = {"'": u"\u0621", # hamza-on-the-line
            "|": u"\u0622", # madda
            ">": u"\u0623", # hamza-on-'alif
            "&": u"\u0624", # hamza-on-waaw
            "<": u"\u0625", # hamza-under-'alif
            "}": u"\u0626", # hamza-on-yaa'
            "A": u"\u0627", # bare 'alif
            "b": u"\u0628", # baa'
            "p": u"\u0629", # taa' marbuuTa
            "t": u"\u062A", # taa'
            "v": u"\u062B", # thaa'
            "j": u"\u062C", # jiim
            "H": u"\u062D", # Haa'
            "x": u"\u062E", # khaa'
            "d": u"\u062F", # daal
            "*": u"\u0630", # dhaal
            "r": u"\u0631", # raa'
            "z": u"\u0632", # zaay
            "s": u"\u0633", # siin
            "$": u"\u0634", # shiin
            "S": u"\u0635", # Saad
            "D": u"\u0636", # Daad
            "T": u"\u0637", # Taa'
            "Z": u"\u0638", # Zaa' (DHaa')
            "E": u"\u0639", # cayn
            "g": u"\u063A", # ghayn
            "_": u"\u0640", # taTwiil
            "f": u"\u0641", # faa'
            "q": u"\u0642", # qaaf
            "k": u"\u0643", # kaaf
            "l": u"\u0644", # laam
            "m": u"\u0645", # miim
            "n": u"\u0646", # nuun
            "h": u"\u0647", # haa'
            "w": u"\u0648", # waaw
            "Y": u"\u0649", # 'alif maqSuura
            "y": u"\u064A", # yaa'
            "F": u"\u064B", # fatHatayn
            "N": u"\u064C", # Dammatayn
            "K": u"\u064D", # kasratayn
            "a": u"\u064E", # fatHa
            "u": u"\u064F", # Damma
            "i": u"\u0650", # kasra
            "~": u"\u0651", # shaddah
            "o": u"\u0652", # sukuun
            "`": u"\u0670", # dagger 'alif
            "{": u"\u0671", # waSla
        }
def transString(string, reverse=0):
    '''Given a Unicode string, transliterate into Buckwalter. To go from
    Buckwalter back to Unicode, set reverse=1'''
    for k, v in buck2uni.items():
        if not reverse:
            string = string.replace(v, k)
        else:
            string = string.replace(k, v)
    return string

print(transString('mrHbA', 1))


############################################################################


# soundex.py
# Make dictionary numerics to map each letter to its group
groups = ['aehiouwy', #0
          'bfpv', #1
          'cgjkqsxz', #2
          'dt', #3
          'l', #4
          'mn', #5
          'r'] #6

numerics = {'a': '0', 'c': '2', 'b': '1', 'e': '0', 'd': '3', 'g': '2', 'f': '1',
'i': '0', 'h': '0', 'k': '2', 'j': '2', 'm': '5', 'l': '4', 'o': '0',
'n': '5', 'q': '2', 'p': '1', 's': '2', 'r': '6', 'u': '0', 't': '3',
'w': '0', 'v': '1', 'y': '0', 'x': '2', 'z': '2'}

def soundex(name):
    """ soundex module conforming to Knuth's algorithm implementation 2000-12-24 by
    Gregory Jorgensen public domain
    """
    # digits holds the soundex values for the alphabet
    sndx = ''
    firstchar = name[0].upper()
    name = name[1:] # le reste du mot
    
    # translate alpha chars in name to soundex digits
    for c in name.lower():
        d = numerics.get(c, '0')
        print(d)
        # duplicate consecutive soundex digits are skipped
        if not sndx or (d != sndx[-1]):
            sndx += d
            
    # replace first digit with first alpha character
    sndx = firstchar + sndx
    
    # remove all 0s from the soundex code
    sndx = sndx.replace('0','')
    
    # return soundex code padded to len characters
    sndx = sndx + '0000'
    print(sndx)
    return sndx[:4]


def test() :
    words =[ "mohammed", "mohamad", "mohamd", "physique", "physik", "phosphore", "fosfor", "rupert", "rubert" ]
    for word in words :
        code = soundex(word.lower())
        print("%s %s" % (code, word))
    
    
if __name__ == "__main__" :
    test()





