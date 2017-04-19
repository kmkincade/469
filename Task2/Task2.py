import hashlib

def main():
    #getting path to a RAW image file (requirement a)
    fileString = input("Enter a path to a RAW image file: ")
    newfileString = fileString.split('\\')
    fileName = newfileString[newfileString.__len__() - 1]
    #now calculate checksums (requirement b)
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(fileString, 'rb') as t:
        while True:
            data = t.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    fileMD5 = open("MD5-" + fileName.split(".")[0] + ".txt", "w+")
    fileMD5.write("MD5: {0}".format(md5.hexdigest()))
    fileSHA1 = open("SHA1-" + fileName.split(".")[0] + ".txt", "w+")
    fileSHA1.write("SHA1: {0}".format(sha1.hexdigest()))
    
if __name__ == "__main__":
    main()