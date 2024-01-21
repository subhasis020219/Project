import random

class MinesweeperAI():
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.mines = set()
        self.safes = set()
        self.moves_made = set()
        self.knowledge = []

    def mark_mine(self, cell):
        self.mines.add(cell)

    def mark_safe(self, cell):
        self.safes.add(cell)

    def add_knowledge(self, cell, count):
        self.moves_made.add(tuple(cell))

        # Mark the cell as safe
        self.mark_safe(tuple(cell))

        # Add a new sentence to the AI's knowledge base
        self.knowledge.append(Sentence(cell, count))

        # Mark any additional cells as safe or as mines
        # if it can be concluded based on the AI's knowledge base
        self.update_knowledge()

    def make_safe_move(self):
        safe_moves = self.safes - self.moves_made
        if safe_moves:
            move = random.choice(list(safe_moves))
            return tuple(move)
        else:
            return None

    def make_random_move(self):
        possible_moves = set((i, j) for i in range(self.height) for j in range(self.width))
        random_moves = possible_moves - self.moves_made - self.mines
        if random_moves:
            move = random.choice(list(random_moves))
            return tuple(move)
        else:
            return None

    def update_knowledge(self):
        # TODO: Update the AI's knowledge base
        pass

class Sentence():
    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def known_mines(self):
        if self.count == len(self.cells):
            return set(self.cells)
        else:
            return set()

    def known_safes(self):
        if self.count == 0:
            return set(self.cells)
        else:
            return set()