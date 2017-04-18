class physical:
    def __init__(self):
        self.partition_start = 0
        self.byte_address = 0
        self.sector_size = 512
        self.physical_known = 0
        self.cluster_size = 0
        self.reserved = 0
        self.fat_tables = 2
        self.fat_length = 0
        self.result = 0
    def physical_to_logical(self):
        self.result = self.physical_known - self.partition_start
        print(self.result)

    def physical_to_cluster(self):
        self.result = ((self.physical_known - self.partition_start -(self.fat_tables*self.fat_length) - self.reserved)/self.cluster_size) + 2
        print(self.result)