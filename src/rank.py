from enum import Enum

class Rank(Enum):
    BRONZE_3 = (0, "B3")
    BRONZE_2 = (100, "B2")
    BRONZE_1 = (200, "B1")
    SILVER_3 = (300, "S3")
    SILVER_2 = (400, "S2")
    SILVER_1 = (500, "S1")
    GOLD_3 = (600, "G3")
    GOLD_2 = (700, "G2")
    GOLD_1 = (800, "G1")
    PLAT_3 = (900, "P3")
    PLAT_2 = (1000, "P2")
    PLAT_1 = (1100, "P1")
    DIAMOND_3 = (1200, "D3")
    DIAMOND_2 = (1300, "D2")
    DIAMOND_1 = (1400, "D1")
    GRANDMASTER_3 = (1500, "G3")
    GRANDMASTER_2 = (1600, "G2")
    GRANDMASTER_1 = (1700, "G1")
    ETERNAL = (1800, "E")

    @staticmethod
    def from_sr(sr):
        for rank in Rank:
            if sr < rank.value[0]:
                return rank
            
        return Rank.ETERNAL
    
    def __str__(self):
        return self.value[1]
