import dis

def loop():
    i = 1
    while i <= 255:
        print(i,"=", "{0:b}".format(i))        
        i = i * 2
        if i >= 2048:
            print("Operation Done")
            break

loop()
print("\n")
dis.dis(loop)
