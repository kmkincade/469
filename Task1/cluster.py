class cluster:
    def __init__(self):
        self.partition_start = 0
        self.byte_address = 0
        self.sector_size = 512
        self.cluster_known = 0
        self.cluster_size = 0
        self.reserved = 0
        self.fat_tables = 2
        self.fat_length = 0
        self.result = 0
    def cluster_to_logical(self):
        self.result = (self.cluster_known - 2)*self.cluster_size + (self.fat_length*self.fat_tables) + self.reserved
        return self.result
    def cluster_to_physical(self):
        self.result =(self.cluster_known - 2)*self.cluster_size + (self.fat_length*self.fat_tables) + self.reserved + self.partition_start
        return self.result