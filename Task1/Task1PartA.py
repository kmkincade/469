from logical import logical
from physical import physical
from cluster import cluster


def main():
    i = 0
    commandString = input('Enter your command: ')
    inputValues = commandString.replace('=', ' ').split()
    if inputValues[0] != "address4forensics":
        print("Incorrect format")
        return
    else:
        if ("-l" in inputValues) | ("--logical-known" in inputValues):
            logic = logical()
            i += 1
            if (inputValues[2] != "-b") | (inputValues[2] != "--partition-start"):
                i += 1
                if (inputValues[2] != "-B") & (inputValues[2] != "--byte-address"):
                    if (inputValues[2] == "-l") | (inputValues[2] == "--logical-known"):
                        i += 1
                        logic.logical_known = int(inputValues[3])
                    elif (inputValues[2] == "-s") | (inputValues[2] == "--sector-size"):
                        logic.sector_size = inputValues[3]
                        i += 1
                        if (inputValues[4] == "-l") | (inputValues[4] == "--logical-known"):
                            i += 1
                            logic.logical_known = int(inputValues[5])
                else:
                    i += 1
                    if (inputValues[3] == "-s") | (inputValues[3] == "--sector-size"):
                        logic.sector_size = int(inputValues[4])

            else:
                i += 1
                logic.partition_start = int(inputValues[3])
                i += 1
                if (inputValues[4] != "-B") & (inputValues[4] != "--byte-address"):
                    if (inputValues[4] == "-l") | (inputValues[4] == "--logical-known"):
                        i += 3
                        logic.logical_known = int(inputValues[5])
                else:
                    i += 1
                    if (inputValues[4] == "-s") | (inputValues[4] == "--sector-size"):
                        logic.sector_size = int(inputValues[5])

            if (inputValues[1] == "-C") | (inputValues[1] == "--cluster"):
                if (inputValues[i] == "-k") | (inputValues[i] == "--cluster-size"):
                    logic.cluster_size = int(inputValues[i + 1])
                    i += 1
                    if (inputValues[i + 1] == "-r") | (inputValues[i+1] == "--reserved"):
                        i+=2
                        logic.reserved = int(inputValues[i])
                        if (inputValues[i + 1] == "-t") | (inputValues[i+1] == "--fat-tables"):
                            i += 2
                            logic.fat_tables = int(inputValues[i])
                            if (inputValues[i+1] == "-f") | (inputValues[i+1] == "--fat-length"):
                                i+=2
                                logic.fat_length = int(inputValues[i])
                logic.logical_to_cluster()
            else:

                logic.logical_to_physical()
        if ("-p" in inputValues) | ("--physical-known" in inputValues):
            p = physical()
            i += 1
            if (inputValues[2] != "-b") & (inputValues[2] != "--partition-start"):
                i += 1
                if (inputValues[2] != "-B") & (inputValues[2] != "--byte-address"):
                    if (inputValues[2] == "-p") | (inputValues[2] == "--physical-known"):
                        i += 1
                        p.physical_known = int(inputValues[3])
                    elif (inputValues[2] == "-s") | (inputValues[2] == "--sector-size"):

                        i+=1
                        p.sector_size = int(inputValues[3])
                        if (inputValues[4] == "-p") | (inputValues[4]== "--physical-known"):
                            p.physical_known = int(inputValues[5])
                            i+=1
                else:
                    i += 1
                    if (inputValues[3] == "-s")| (inputValues[3] == "--sector-size"):
                        p.sector_size = int(inputValues[4])

            else:
                i += 1
                p.partition_start = int(inputValues[3])
                i += 1
                if (inputValues[4] != "-B") & (inputValues[4] != "--byte-address"):
                    if (inputValues[4] == "-p") | (inputValues[4] == "--physical-known"):
                        i += 3
                        p.physical_known = int(inputValues[5])
                    elif (inputValues[4] == "-s") | (inputValues[4] == "--sector-size"):
                        i+= 1
                        p.sector_size = int(inputValues[5])
                        if (inputValues[6] == "-p") | (inputValues[6] == "--physical-known"):
                            i+= 1
                            p.physical_known = int(inputValues[7])
                else:
                    i += 1
                    if (inputValues[4] == "-s") | (inputValues[4] == "--sector-size"):
                        p.sector_size = int(inputValues[5])

            if (inputValues[1] == "-C") | (inputValues[1] == "--cluster"):
                if (inputValues[i] == "-k") | (inputValues[i] == "--cluster-size"):
                    p.cluster_size = int(inputValues[i + 1])
                    i += 1
                    if (inputValues[i + 1] == "-r") | (inputValues[i+1] == "--reserved"):
                        i += 2
                        p.reserved = int(inputValues[i])
                        if (inputValues[i + 1] == "-t") | (inputValues[i + 1] == "--fat-tables"):
                            i += 2
                            p.fat_tables = int(inputValues[i])
                            if (inputValues[i + 1] == "-f") | (inputValues[i + 1] == "--fat-length"):
                                i += 2
                                p.fat_length = int(inputValues[i])
                p.physical_to_cluster()
            else:

                p.physical_to_logical()
        if ("-c" in inputValues) | ("--cluster-known" in inputValues):
            c = cluster()
            i += 1
            if (inputValues[2] != "-b") & (inputValues[2] != "--partition-start"):
                i += 1
                if (inputValues[2] != "-B") & (inputValues[2] != "--byte-address"):
                    if (inputValues[2] == "-c") | (inputValues[2] == "--cluster-known"):
                        i += 1
                        c.cluster_known = int(inputValues[3])
                    elif (inputValues[2] == "-s") | (inputValues[2] == "--sector-size"):
                        i+=1
                        c.sector_size = int(inputValues[3])
                        if (inputValues[4] == "-c") | (inputValues[4] == "--cluster-known"):
                            i+=1
                            c.cluster_known = int(inputValues[5])
                else:
                    i += 1
                    if (inputValues[3] == "-s") | (inputValues[3] == "--sector-size"):
                        c.sector_size = int(inputValues[4])

            else:
                i += 1
                c.partition_start = int(inputValues[3])
                i += 1
                if (inputValues[4] != "-B") & (inputValues[4] != "--byte-address"):
                    if (inputValues[4] == "-c") | (inputValues[4] == "--cluster-known"):
                        i += 3
                        c.cluster_known = int(inputValues[5])
                    elif inputValues[4] == "-s":
                        i+=1
                        c.sector_size = int(inputValues[5])
                        if inputValues[6] == "-c":
                            c.cluster_known = int(inputValues[7])
                            i+=4
                else:
                    i += 1
                    if inputValues[4] == "-s":
                        c.sector_size = int(inputValues[5])

            if (inputValues[1] == "-P") | (inputValues[1]== "--physical"):
                if inputValues[i] == "-k":
                    c.cluster_size = int(inputValues[i + 1])
                    i += 1
                    if inputValues[i + 1] == "-r":
                        i += 2
                        c.reserved = int(inputValues[i])
                        if inputValues[i + 1] == "-t":
                            i += 2
                            c.fat_tables = int(inputValues[i])
                            if inputValues[i + 1] == "-f":
                                i += 2
                                c.fat_length = int(inputValues[i])
                c.cluster_to_physical()
            else:
                if inputValues[i] == "-k":
                    c.cluster_size = int(inputValues[i + 1])
                    i += 1
                    if inputValues[i + 1] == "-r":
                        i += 2
                        c.reserved = int(inputValues[i])
                        if inputValues[i + 1] == "-t":
                            i += 2
                            c.fat_tables = int(inputValues[i])
                            if inputValues[i + 1] == "-f":
                                i += 2
                                c.fat_length = int(inputValues[i])
                c.cluster_to_logical()
if __name__ == "__main__":
    main()


