import sys
import os

'''
Returns list of strings: [Feature, Estimate, Actual, Summary]
'''

def stringParse (gitString):
    gitString = " " + gitString.replace("\n","  ")
    feat, start, stop = beforeAfter(["F:","Feature:","Feat:"],[' '],gitString)
    if (feat == "SNP"):
        feat = ''
    else:
        if (start == 0):
            gitString = gitString[stop:]
        else:
            gitString = gitString[:start] + gitString[stop:]
    est, start, stop = beforeAfter(["E:","Estimate:","Est:"],[' '],gitString)
    if (est == "SNP"):
        est = ''
    else:
        gitString = gitString[:start] + gitString[stop:]
    act, start, stop = beforeAfter(["A:","Actual:","Act:"],[' '],gitString)
    if (act == "SNP"):
        act = ''
    else:
        gitString = gitString[:start] + gitString[stop:]
    return feat.strip(), est.strip(), act.strip(), gitString.strip();
        
def beforeAfter (bef, aft, s):
    start, stop, begin = -1, -1, 0
    for keyword in bef:
        if (s.lower().find(keyword.lower()) == 0 or s.lower().find(" " + keyword.lower()) != -1):
            begin = s.lower().find(" " + keyword.lower())
            if(begin == -1):
                begin = 0
            start = begin + len(keyword) + 1
            if (s[start] == " "):
                start = start + 1
    for keyword in aft:
        if (s[start:].find(keyword) != -1):
            stop = s[start:].find(keyword) + start
            break
    if (stop == -1):
        stop = len(s)
    if (start == -1):
        result = "SNP"
    else:
        result = s[start:stop].strip()
    return result, begin, stop;
    
if __name__ == '__main__':
    s = "E:5 \nA:\nF:Merge-Rules \nSummary: This is the Summary text."
    print ("Input 1: \n" + s)
    print("\nOutput List 1: ")
    print (stringParse(s))
    print("-------------------------------------------------")
    s = "Summary: This is the Summary text.\nEst:5 \nActual: 9000+\nFeature:Merge-Rules"
    print ("Input 2: \n" + s)
    print("\nOutput List 2: ")
    print (stringParse(s))
    print("-------------------------------------------------")
    s = "Summary: Title:This is the Summary text.\nE:5\nActual: 9000+\nFeature:Merge-Rules"
    print ("Input 3: \n" + s)
    print("\nOutput List 3: ")
    print (stringParse(s))
    
