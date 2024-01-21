

class Symbol:
    def __init__(self, name):
        self.name = name

class And:
    def __init__(self, *args):
        self.args = args

class Or:
    def __init__(self, *args):
        self.args = args

class Not:
    def __init__(self, arg):
        self.arg = arg

class Biconditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right


# Puzzle 0
# A says "I am both a knight and a knave."
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

knowledge0 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A cannot be both a knight and a knave
    Biconditional(AKnight, Not(AKnave)), # If A is a knight then A is not a knave
    Biconditional(AKnave, Not(AKnight)), # If A is a knave then A is not a knight
    Biconditional(AKnight, And(AKnight, AKnave)) # A says "I am both a knight and a knave."
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
BKnave = Symbol("B is a Knave")
BKnight = Symbol("B is a Knight")

knowledge1 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A cannot be both a knight and a knave
    Biconditional(AKnight, Not(AKnave)), # If A is a knight then A is not a knave
    Biconditional(AKnave, Not(AKnight)), # If A is a knave then A is not a knight
    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B cannot be both a knight and a knave
    Biconditional(BKnight, Not(BKnave)), # If B is a knight then B is not a knave
    Biconditional(BKnave, Not(BKnight)), # If B is a knave then B is not a knight
    Biconditional(AKnight, And(AKnave, BKnave)) # A says "We are both knaves."
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A cannot be both a knight and a knave
    Biconditional(AKnight, Not(AKnave)), # If A is a knight then A is not a knave
    Biconditional(AKnave, Not(AKnight)), # If A is a knave then A is not a knight
    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B cannot be both a knight and a knave
    Biconditional(BKnight, Not(BKnave)), # If B is a knight then B is not a knave
    Biconditional(BKnave, Not(BKnight)), # If B is a knave then B is not a knight
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))), # A says "We are the same kind."
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))) # B says "We are of different kinds."
)

# Puzzle 3
# A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
# B says “A said ‘I am a knave.’”
# B then says “C is a knave.”
# C says “A is a knight.”
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge3 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A cannot be both a knight and a knave
    Biconditional(AKnight, Not(AKnave)), # If A is a knight then A is not a knave
    Biconditional(AKnave, Not(AKnight)), # If A is a knave then A is not a knight
    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B cannot be both a knight and a knave
    Biconditional(BKnight, Not(BKnave)), # If B is a knight then B is not a knave
    Biconditional(BKnave, Not(BKnight)), # If B is a knave then B is not a knight
    Or(BKnight, BKnave), # C is either a knight or a knave
    Not(And(BKnight, BKnave)), # C cannot be both a knight and a knave
    Biconditional(BKnight, Not(BKnave)), # If C is a knight then C is not a knave
    Biconditional(BKnave, Not(BKnight)), # If C is a knave then C is not a knight
    Biconditional(AKnight, AKnight), # A says “I am a knight.”
    Biconditional(AKnave, AKnave), # A says “I am a knave.”
    Biconditional(BKnight, And(Biconditional(AKnight, AKnave), CKnave)), # B says “A said ‘I am a knave.’” and “C is a knave.”
    Biconditional(CKnight, AKnight) # C says “A is a knight.”
)
