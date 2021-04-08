'''
Created on May 9, 2019

@author: ganesh.bm
'''

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except:
    print("Unexpected error:")
    raise
