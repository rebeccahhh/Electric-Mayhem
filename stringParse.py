import sys
import os

'''
Feature
E# (estimate)
A# (actual)
Summary
'''

def stringParse (gitString):
    feat = ''
    est = ''
    act = ''
    summ = ''
    return feat, est, act, summ;
    
def beforeAfter (bef, aft, s):
    start = s.find(bef)
    start = start + len(bef)
    stop = s.find(aft)
    result = s[start:stop]
    return result;
    
def main ():
    print (sys.argv[0])
    
    return;
    
