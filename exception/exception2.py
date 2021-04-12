try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except:
    print("Unexpected error:")
    raise
