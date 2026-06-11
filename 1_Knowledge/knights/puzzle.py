from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

common_knowledge = And(
    Or(AKnight, AKnave), 
    Not(And(AKnight, AKnave))
)
# print(common_knowledge.formula())

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    common_knowledge, 
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

query0 = And(
    AKnight, AKnave
)

model_check(knowledge0, query0)

print(knowledge0.formula())

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
common_knowledge.add(And(
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
))

knowledge1 = And(
    common_knowledge,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

query1 = And(
    AKnave, BKnave
)

model_check(knowledge1, query1)

# Puzzle 2
# A says "We are the same kind.",
# B says "We are of different kinds."

knowledge2 = And(
    common_knowledge,
    Implication(AKnight, Or(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave))),
    Implication(AKnave, Not(Or(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave)))),
    Implication(BKnight, Or(Biconditional(AKnight, BKnave), Biconditional(AKnave, BKnight))),
    Implication(BKnave, Not(Or(Biconditional(AKnight, BKnave), Biconditional(AKnave, BKnight))))
)

query2 = And(
    Or(And(AKnight, BKnight), And(AKnave, BKnave)),
    Or(And(AKnight, BKnave), And(AKnave, BKnight))
)

model_check(knowledge2, query2)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
common_knowledge.add(And(
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
))

knowledge3 = And(
    common_knowledge,
    Implication(AKnight, BKnave),
    Implication(AKnave, Not(BKnave)),
    Implication(BKnight, And(CKnight, Not(AKnight))),
    Implication(BKnave, Not(And(CKnight, Not(AKnight)))),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

query3 = And(
    Or(AKnight, AKnave),
    BKnave,
    CKnave
)

model_check(knowledge3, query3)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
