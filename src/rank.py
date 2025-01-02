from enum import Enum

class Rank(Enum):
    BRONZE_3 =          (0, 3099,    "B3", "Bronze 3")
    BRONZE_2 =          (3100, 3199,  "B2", "Bronze 2")
    BRONZE_1 =          (3200, 3299,  "B1", "Bronze 1")
    SILVER_3 =          (3300, 3399,  "S3", "Silver 3")
    SILVER_2 =          (3400, 3499,  "S2", "Silver 2")
    SILVER_1 =          (3500, 3599,  "S1", "Silver 1")
    GOLD_3 =            (3600, 3699,  "G3", "Gold 3")
    GOLD_2 =            (3700, 3799,  "G2", "Gold 2")
    GOLD_1 =            (3800, 3899,  "G1", "Gold 1")
    PLAT_3 =            (3900, 3999,  "P3", "Platinum 3")
    PLAT_2 =            (4000, 4099, "P2", "Platinum 2")
    PLAT_1 =            (4100, 4199, "P1", "Platinum 1")
    DIAMOND_3 =         (4200, 4299, "D3", "Diamond 3")
    DIAMOND_2 =         (4300, 4399, "D2", "Diamond 2")
    DIAMOND_1 =         (4400, 4499, "D1", "Diamond 1")
    GRANDMASTER_3 =     (4500, 4599, "GM3", "Grandmaster 3")
    GRANDMASTER_2 =     (4600, 4699, "GM2", "Grandmaster 2")
    GRANDMASTER_1 =     (4700, 4799, "GM1", "Grandmaster 1")
    ETERNAL =           (4800, 4899, "E", "Eternal")

    @staticmethod
    def from_sr(sr):
        for rank in Rank:
            if sr >= rank.value[0] and sr <= rank.value[1]:
                return rank
            
        return Rank.ETERNAL
    
    @property
    def rank(self):
        return self.value[2]
    
    @property
    def name(self):
        return self.value[3]
    
    def __str__(self):
        return self.value[1]
    
