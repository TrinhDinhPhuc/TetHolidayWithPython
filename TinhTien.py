# -*- coding: utf-8 -*-

import re
from pathlib import Path

# s='''
# trà xanh Olong sữa 27kg  - 200k
# trà xanh Olong Nhài 3.5kg - 100k
# trà xanh olong Sen 3.5kg   - 100k
# trà xanh olong Xoài 3.5kg  - 100k
# trà xanh olong Cúc  3.5kg  - 230k
# Trà đen             4kg  - 80k
# trà matcha 3.5kg  - 300k
# trà đen hương dâu tây 20kg - 200k
# trà đen thảo quả 14kg  - 150k
# '''

def tachkg():
    d=re.findall('\d{1,}kg|\d{1,}.?\d{1,}kg',file)
    str1 = ''.join(str(e) for e in d)
    bokg=str1.replace("kg"," ")
    convert_to_list=bokg.split()  #chuyen sang list
    results = list(map(float, convert_to_list))
    length=len(results)
    print("Do dai cua mang kg la: {}".format(length))
    return  results
def tachtien():
    d=re.findall('- \d{1,}kg|- \d{1,}.?\d{1,}k',file)
    str1 = ''.join(str(e) for e in d)
    bodau=str1.replace("-"," ")
    bok=bodau.replace("k","")
    convert_to_list=bok.split()
    results = list(map(float, convert_to_list))
    length=len(results)
    print("Do dai cua mang tien la: {}".format(length))
    return results
def congtien(lista,listb):
    return [a*b for a,b in zip(lista,listb)]
def count_line():
    line=1
    for i in file:
        if(i=="\n"):
            line+=1
    return line
if __name__ =='__main__':
    tenfile = input("Danh Ten file...: ")
    try:
        with open(tenfile, 'r',encoding='utf-8') as myfile:
            file = myfile.read()
        print("\n", file, "\n-------------------------------------\n")
        tong = congtien(tachkg(), tachtien())
        total = 0
        for i in tong:
            total += i
        print("\n Ki: {} \n Gia: {}\n tong: {}\n SoTien= {} ".format(tachkg(), tachtien(), tong, total))
        print("So line= {}".format(count_line()))
    except IOError:
        print("ERROR, ko tim thay file!!!")
