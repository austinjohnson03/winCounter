from enum import Enum

class Rank(Enum):
    BRONZE_3 =          (3000,    "B3")
    BRONZE_2 =          (3100,  "B2")
    BRONZE_1 =          (3200,  "B1")
    SILVER_3 =          (3300,  "S3")
    SILVER_2 =          (3400,  "S2")
    SILVER_1 =          (3500,  "S1")
    GOLD_3 =            (3600,  "G3")
    GOLD_2 =            (3700,  "G2")
    GOLD_1 =            (3800,  "G1")
    PLAT_3 =            (3900,  "P3")
    PLAT_2 =            (4000, "P2")
    PLAT_1 =            (4100, "P1")
    DIAMOND_3 =         (4200, "D3")
    DIAMOND_2 =         (4300, "D2")
    DIAMOND_1 =         (4400, "D1")
    GRANDMASTER_3 =     (4500, "GM3")
    GRANDMASTER_2 =     (4600, "GM2")
    GRANDMASTER_1 =     (4700, "GM1")
    ETERNAL =           (4800, "E")

    @staticmethod
    def from_sr(sr):
        for rank in Rank:
            if sr < rank.value[0]:
                return rank
            
        return Rank.ETERNAL
    
    def __str__(self):
        return self.value[1]
