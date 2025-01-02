from rank import Rank

class Counter:
    def __init__(
            self, 
            wins: int, 
            lossses: int, 
            draws: int,
            rs: int
    ):
        self._wins = wins
        self._losses = lossses
        self._draws = draws
        self._rs = rs
        self._rank = Rank().from_sr(rs)

    @property
    def wins(self) -> int:
        return self._wins
    
    @wins.setter
    def wins(self, wins: int) -> None:
        self._wins = wins

    @property
    def losses(self) -> int:
        return self._losses
    
    @losses.setter
    def losses(self, losses: int) -> None:
        self._losses = losses

    @property
    def draws(self) -> int:
        return self._draws
    
    @draws.setter
    def draws(self, draws: int) -> None:
        self._draws = draws

    @property
    def rs(self) -> int:
        return self._rs
    
    @rs.setter
    def rs(self, rs: int) -> None:
        self._rs = rs

    @property
    def rank(self) -> str:
        return self._rank.rank
    
    @rank.setter
    def rank(self, rs: int) -> None:
        self._rank

    def add_win(self) -> None:
        self._wins += 1

    def add_loss(self) -> None:
        self._losses += 1

    def add_draw(self) -> None:
        self._draws += 1

    def reset_counter(self) -> None:
        self._wins = 0
        self._losses = 0
        self._draws = 0

    def to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as file:
            file.write(str(self))

    def __str__(self) -> str:
        if self._draws == 0:
            return f'Rank: {self._rank.name}\nWins: {self._wins}\nLosses: {self._losses}\n'
        
        return f'Wins: {self._wins}\nLosses: {self._losses}\nDraws: {self._draws}\n'
    
if __name__ == '__main__':
    counter = Counter(0, 0, 0, 3451)
    print(counter)
    counter.add_win()
    counter.add_loss()
    counter.add_draw()
    print(counter)
    counter.reset_counter()
    print(counter)
    