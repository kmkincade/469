import binascii

partition_types = {
    0x01: "DOS 12-bit FAT",
    0x04: "DOS 16-bit FAT for partitions smaller than 32MB",
    0x05: "Extended Partition",
    0x06: "DOS 16-bit FAT for partitions larger than 32MB",
    0x07: "NTFS",
    0x08: "AIX bootable partition",
    0x09: "AIX data partition",
    0x0b: "DOS 32-bit FAT",
    0x0c: "DOS 32-bit FAT for interrupt 13 support",
    0x17: "Hidden NTFS partition (XP and earlier)",
    0x1b: "Hidden FAT32 partition",
    0x1e: "Hidden VFAT partition",
    0x3c: "Partition magic recovery partition",
    0x66: "Novell partition",
    0x67: "Novell partition",
    0x68: "Novell partition",
    0x69: "Novell partition",
    0x81: "Linux",
    0x82: "Linux swap partition",
    0x83: "Linux native file system",
    0x86: "FAT16 volume/stripe set",
    0x87: "High Performance File system (HPFS) fault-tolerant mirrored partition or NTFS volume/stripe set",
    0xA5: "Free BSD and BSD/386",
    0xA6: "OpenBSD",
    0xA9: "NetBSD",
    0xC7: "Corrupt NTFS volume/stripe set",
    0xEB: "BeOS",

}

byte = 1
word = 2
double_word = 4

def get_partition_tables(f):
    f.seek(446)
    partition_tables = f.read(128)
    partition_tables = binascii.hexlify(partition_tables) # this is formatting the tables in an easy to use manner
    partition_tables = [partition_tables[i*32:i*32+32] for i in range(4)]
    partition_tables = map(lambda x: hex(int(x, 16))[2:].replace('L', ''), partition_tables)
    partition_tables = map(lambda x: '0'*(32-len(x)) + x, partition_tables)
    partition_tables = map(lambda x: [x[i*2:i*2+2] for i in range(16)], partition_tables) # Now looks like [['00', '20', '21', '00', '0b', '55', '11', '04', '00', '08', '00', '00', '00', '08', '01', '00']]
    return partition_tables

def print_partition_info(f):
    ps = get_partition_tables(f)
    print_string = "({hex}) {name} {start_sector} {size}"
    for partition in ps:
        hex_val = partition[4]
        try:
            name = partition_types[int(hex_val, 16)]
        except KeyError:
            name = "Unknown"
        start_sector = int(''.join(reversed(partition[8:12])), 16)
        size = int(''.join(reversed(partition[12:])), 16)

        print(print_string.format(hex=hex_val, name=name, start_sector=start_sector, size=size))
        if name.__contains__("FAT"):
                # 512 bytes in a sector
                f.seek(start_sector * 512)
                vbr = f.read(128)
                vbr = binascii.hexlify(vbr)  # this is formatting the tables in an easy to use manner
                vbr = [vbr[i * 32:i * 32 + 32] for i in range(4)]
                vbr = map(lambda x: hex(int(x, 16))[2:].replace('L', ''), vbr)
                vbr = map(lambda x: '0' * (32 - len(x)) + x, vbr)
                vbr = map(lambda x: [x[i * 2:i * 2 + 2] for i in range(16)], vbr)
                i = 0
                reserved_start = 0
                reserved_end = 0
                fat_count = 0
                fat_size = 0
                ending_sector = 0
                cluster_2_start = 0
                for information in vbr:
                    #print(information)
                    i+=1
                    if i==1:
                        reserved_start += start_sector
                        reserved_end += reserved_start + int(''.join(reversed(information[14:16])), 16)
                        print("Reserved Area: Start Sector: " + str(reserved_start) + " Ending Sector: " + str(reserved_end) + " " + str(reserved_end - reserved_start) + " sectors")
                        sectors_per_cluster = int(''.join(information[13:14]), 16)
                        print("Sectors per cluster: " + str(sectors_per_cluster) + " sectors")
                    elif i == 2:
                        fat_count += int(''.join(information[0:1]), 16)
                        if (name.__contains__("16-bit") | name.__contains__("12-bit")):
                            fat_size += int(''.join(reversed(information[6:8])), 16)
                            cluster_2_start += int(''.join(reversed(information[1:3])), 16)
                    elif i == 3:
                        if name.__contains__("32-bit"):
                            fat_size += int(''.join(reversed(information[4:8])), 16)
                        ending_sector += fat_count*fat_size + reserved_end + 1
                        print("FAT area: Start sector: " + str(reserved_end + 1) + " Ending sector: " + str(ending_sector))
                        print("# of FATs: " + str(fat_count))
                        print("Size of each FAT: " + str(fat_size))
                        if name.__contains__("32-bit"):
                            print("The first sector of cluster 2: " + str(ending_sector + 1) + "\n")
                        else:
                            cluster_2_start += ending_sector + 1
                            print("The first sector of cluster 2: "+ str(cluster_2_start) + "\n")




def get_filesystem_info(f, start_sector):
    f.seek(start_sector)

def partitions(filename):
    with open(filename, "rb") as f:
        print_partition_info(f)


