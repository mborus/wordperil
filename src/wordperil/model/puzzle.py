from wordperil.common.constants import TILES_HORIZONTAL, TILES_VERTICAL


class Puzzle:

    @staticmethod
    def extract_row(string):
        length = 0
        line = ""
        unused = ""
        for word in string.split():
            length += len(word) + 1
            if length > TILES_HORIZONTAL:
                unused = f"{unused} {word}"
            else:
                line = f"{line} {word}"

        line = line.strip().center(TILES_HORIZONTAL - 1)
        return (line, unused)

    def __init__(self, puzzle, clue=""):
        self.clue = clue

        # Break the puzzle down into rows to fit on puzzle board
        puzzle = puzzle.upper()

        self.rows = []
        while puzzle:
            line, puzzle = self.extract_row(puzzle)
            self.rows.append(line)

        empty_rows = TILES_VERTICAL - len(self.rows)
        if empty_rows < 0:
            raise ValueError("Cannot fit puzzle.")
        elif empty_rows <= TILES_VERTICAL // 2:
            for row in range(empty_rows // 2):
                self.rows.insert(0, "")

    def __iter__(self):
        return iter(self.rows)