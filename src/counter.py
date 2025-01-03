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
            return f'Wins: {self._wins}\nLosses: {self._losses}\n'
        
        return f'Wins: {self._wins}\nLosses: {self._losses}\nDraws: {self._draws}\n'
    