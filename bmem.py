import time

def readBMP(file_name):
    f = open(file_name, 'rb')
    f.seek(54)  #skip header
    data=[]    
    try:
        while(True):
            row=[]
            for i in range(16):    
                r=ord(f.read(1))
                g=ord(f.read(1))
                b=ord(f.read(1))
                row.append([b,g,r])
            data = row + data          
    except TypeError:
        pass            
    f.close()
    return data

def scaleToOne(x):
    return x/255

def to4bit(x):
    return int(scaleToOne(x)*15+0.5)

try:
    f = open('bitmap_converter.config', 'r')
    file_name = f.readline().split('bitmap=')[1]
    f.close()
except:
    file_name=input('Enter bitmap file name to convert to \'bmem.mem\' (must be type .bmp): ')
    if('.' not in file_name):   #add .bmp if they left it off
        file_name+='.bmp'            
    f = open('bitmap_converter.config', 'w')
    f.write('bitmap='+file_name)
    f.close()    
    print('\'bitmap_converter.config\' created')

data = readBMP(file_name)    
f = open('bmem.mem', 'w')
writedata = '\n'.join(['%x%x%x' % (to4bit(r),to4bit(g),to4bit(b)) for (r,g,b) in data])
f.write(writedata)         
f.close()

print('\'bmem.mem\' updated using \''+file_name+'\'')
time.sleep(0.5) #to display the message before closing automatically