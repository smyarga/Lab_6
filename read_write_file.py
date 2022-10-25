"""
Lab 6 #4
"""
from typing import List, TextIO
from io import StringIO
import urllib.request

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    Return list of strings lists from url
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], \
['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    output = []
    i = 1
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip().decode('utf-8')
            line = line.replace('До наказу', '+')
            line = line.replace('Рекомендовано (контракт)', '+')
            line = line.split('\t')
            if line[0].isdigit():
                output.append(line[:4])
            if line[0].startswith('Середній'):
                output[i-1].append(line[0].split()[-1])
                i +=1
            if i == number+1:
                break
    return output



def write_csv_file(url: str, text_file: TextIO) -> None:
    """
    Adding info to csv file
    >>> outfile = StringIO()
    >>> write_csv_file('https://gist.githubusercontent.com/\
smyarga/11f19a39d62fabd2a2e15d54803d82c9/raw/\
483ebe78bbd53cbb4918d67c5f8273edcee2353d/total.txt', outfile)
    >>> outfile.getvalue()
    '№,ПІБ,Д,Заг.бал,С.б.док.осв.\\n1,Мацюк М. І.,+,197.859,10.80\\n'
    """
    counter = 0
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip().decode('utf-8')
            line = line.split('\t')
            if line[0].isdigit():
                counter += 1
    text_file.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
    for item in read_input_file(url, counter):
        string = ','.join(item) + '\n'
        text_file.write(string)

if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())
    with open('total.csv', 'w', encoding = 'utf-8') as output_file:
        write_csv_file('https://gist.githubusercontent.com/\
smyarga/11f19a39d62fabd2a2e15d54803d82c9/raw/\
483ebe78bbd53cbb4918d67c5f8273edcee2353d/total.txt', output_file)
