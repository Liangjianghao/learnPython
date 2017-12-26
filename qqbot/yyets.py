# coding:utf-8

import urllib.request  
import re  
  
  
def get_links(url, name='yyets'):  
    data = urllib.request.urlopen(url).read().decode()  
    pattern = '"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'  
    linksfind = set(re.findall(pattern, data))  
    linksdict = {}  
    total = len(linksfind)  
    for i in linksfind:  
        linksdict[int(i[1][1:3]) * 100 + int(i[2][1:3])] = i  
    with open(name + '.txt', 'w') as f:  
        for i in sorted(list(linksdict.keys())):  
            f.write(linksdict[i][0] + '\n')  
            print(linksdict[i][0])  
    print("Get download links of: ", name, str(total))  
  
  
if __name__ == '__main__':  
    #---------- 越狱、无耻之徒、权力的游戏---------------------------  
    get_links('http://www.yyets.com/resource/10004', 'prision_break')  
    get_links('http://www.yyets.com/resource/10760', 'shameless')  
    get_links('http://www.yyets.com/resource/d10733','Game_of_Thrones')  
    print('All is okay!') 