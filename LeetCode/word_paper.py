with open("word_paper.txt",'r') as f:
    t = int(f.readline())
    for i in range(t):
        output = ''
        for j in range(8):
            line = f.readline().strip('\n')
            for c in line:
                if c not in ' .':
                    #print(c)
                    output += c
        print(output)