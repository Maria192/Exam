import re
import os

def write (d):
    fw = open('written.txt','w', encoding = 'UTF-8')
    for wrd in d:
        fw.write(wrd + '\n')
    fw.close()
    
def create(d):
    for key in d:
        os.mkdir(key)
        dire = os.getcwd()
        
        dire = dire + '\\' + key
        print (dire)
        fw = open(dire + key, 'w', encoding = 'UTF-8')

def words(arr):
    words = []
    name = ' [А-ЯЁ]\. [А-ЯЁ][а-яё].+?[ ,.<"\-&;:]'
    res = re.findall(name, arr)
    for wrd in res:
        if 'Примечания' in wrd:
            break
        else:
            wrd = wrd[1:-1]
            words.append(wrd)
    for wrd in words:
        print(wrd)
    print('\n')
   

def names (arr):
    words = []
    d = {}
    lex = '(?:(?:(?: [А-ЯЁ]\.){2,2}) [А-ЯЁ][а-яё].+?[ ,.<"\-&:;])|(?:(?: [А-ЯЁ][а-яё]+){1,2} [А-ЯЁ][а-яё].+?[ ,.<"\-&:;])'
    res = re.findall(lex, arr)
    for wrd in res:
        if 'Примечания' in wrd:
            break
        else:
            wrd = wrd[1:-1]
            words.append(wrd)
            fami = re.findall('.* ([А-ЯЁ][а-яё]+)',wrd)
            for elem in fami:
                d[elem] = 'Предложение'
    for wrd in words:
        print(wrd)
    create (d)
    

def openfile (name):
    f = open(name,'r', encoding = 'UTF-8')
    s = f.read()
    f.close()
    #print (s)
    words(s)
    names(s)
    

def main():
    name = 'Герцен, Александр Иванович — Википедия.html'
    strk = openfile(name)
    
if  __name__ == '__main__':
    main()
