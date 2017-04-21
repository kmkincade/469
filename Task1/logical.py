class logical:
    def __init__(self):
        self.partition_start = 0
        self.byte_address = 0
        self.sector_size = 512
        self.logical_known = 0
        self.cluster_size = 0
        self.reserved = 0
        self.fat_tables = 2
        self.fat_length = 0
        self.result = 0
    def logical_to_physical(self):
        self.result = self.logical_known + self.partition_start
        return self.result

    def logical_to_cluster(self):
        self.result = ((self.logical_known - (self.fat_tables*self.fat_length) - self.reserved)/self.cluster_size) + 2
        return self.result

