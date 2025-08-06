# game.py
class HanoiGame:
    def __init__(self, num_discs):
        self.num_discs = num_discs
        self.pegs = [list(range(num_discs, 0, -1)), [], []]  # [origen, aux, destino]
        self.moves = 0
        self.start_time = None
        self.is_running = False

    def move(self, from_peg, to_peg):
        if self.is_valid_move(from_peg, to_peg):
            disk = self.pegs[from_peg].pop()
            self.pegs[to_peg].append(disk)
            self.moves += 1
            return True
        return False

    def is_valid_move(self, from_peg, to_peg):
        if len(self.pegs[from_peg]) == 0:
            return False
        if len(self.pegs[to_peg]) == 0:
            return True
        return self.pegs[from_peg][-1] < self.pegs[to_peg][-1]

    def is_solved(self):
        return (len(self.pegs[1]) == self.num_discs or len(self.pegs[2]) == self.num_discs)

    def reset(self, num_discs):
        self.num_discs = num_discs
        self.pegs = [list(range(num_discs, 0, -1)), [], []]
        self.moves = 0
        self.start_time = None
        self.is_running = False