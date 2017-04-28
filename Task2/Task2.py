#!/usr/bin/env python3
import hashlib
from Task2PartC import partitions
import binascii
import sys
import os


def main():
    # getting path to a RAW image file (requirement a)
    fileString = sys.argv[1]
    newfileString = os.path.abspath(fileString)
    path, fileName = os.path.split(newfileString)
    # now calculate checksums (requirement b)
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
    md5Filename = os.path.join(path, "MD5-" + fileName.split(".")[0] + ".txt")
    fileMD5 = open(md5Filename, "w+")
    fileMD5.write("MD5: {0}".format(md5.hexdigest()))
    sha1Filename = os.path.join(path, "SHA1-" + fileName.split(".")[0] + ".txt")
    fileSHA1 = open(sha1Filename, "w+")
    fileSHA1.write("SHA1: {0}".format(sha1.hexdigest()))
    partitions(fileString)


if __name__ == "__main__":
    main()
