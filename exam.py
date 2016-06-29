import re

def write (d):
    fw = open('written.txt','w', encoding = 'UTF-8')
    for wrd in d:
        fw.write(wrd + '\n')
    fw.close()

def words(arr):
    words = []
    i = 1
    lex = '(?:(?:(?: [А-Я]\.){1,2}) [А-Я][а-я].+?[ ,.<"-])|(?: [А-Я][а-я]+ [А-Я][а-я].+?[ ,.<"-])'
    res = re.findall(lex, arr)
    for wrd in res:
        wrd = wrd[1:-1]
        words.append(wrd)
    write (words)


def openfile (name):
    f = open(name,'r', encoding = 'UTF-8')
    s = f.read()
    f.close()
    words (s)          
    

def main():
    name = 'Герцен, Александр Иванович — Википедия.html'
    strk = openfile(name)
    
if  __name__ == '__main__':
    main()
