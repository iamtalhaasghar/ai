for i in open('volume.csv').readlines():
    if i.strip().endswith(','):
        print(i[:-2])
    else:
        print(i,end='')