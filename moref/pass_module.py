import random as r

def generate_password(username):
    
    password = ""
    for i in range(4):
        ran = r.randint(0,len(username)-1)
        char = username[ran]
        convert = r.randint(0,1)
        if convert == 1:
            char.upper()
        password += char
    
    for j in range(4):
        n = r.randint(0,9)
        password += str(n)

    return password

def write_passwords(infile, outfile):

    in_file = open(infile, 'r')
    out_file = open(outfile, 'w')

    for line in in_file:
        password = generate_password(line.strip())
        out_file.write(line.strip()+':'+password+'\n')
    in_file.close()
    out_file.close()
