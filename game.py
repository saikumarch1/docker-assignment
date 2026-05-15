import random
from collections import deque


class Minesweeper:

    def __init__(self, size, mines):

        self.size = size
        self.mines = mines

        self.board = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]

        self.visible = [
            [False for _ in range(size)]
            for _ in range(size)
        ]

        self.flags = [
            [False for _ in range(size)]
            for _ in range(size)
        ]

        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):

        placed = 0

        while placed < self.mines:

            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if self.board[row][col] != "M":

                self.board[row][col] = "M"
                placed += 1

    def calculate_numbers(self):

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for row in range(self.size):

            for col in range(self.size):

                if self.board[row][col] == "M":
                    continue

                count = 0

                for dr, dc in directions:

                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < self.size and 0 <= nc < self.size:

                        if self.board[nr][nc] == "M":
                            count += 1

                self.board[row][col] = count

    def reveal(self, row, col):

        if self.board[row][col] == "M":

            self.visible[row][col] = True
            return "lost"

        self.dfs_reveal(row, col)

        return "continue"

    def dfs_reveal(self, row, col):

        if row < 0 or col < 0:
            return

        if row >= self.size or col >= self.size:
            return

        if self.visible[row][col]:
            return

        if self.board[row][col] == "M":
            return

        self.visible[row][col] = True

        if self.board[row][col] != 0:
            return

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dr, dc in directions:

            self.dfs_reveal(
                row + dr,
                col + dc
            )

    def toggle_flag(self, row, col):

        self.flags[row][col] = (
            not self.flags[row][col]
        )

    def get_visible_board(self):

        display = []

        for row in range(self.size):

            current = []

            for col in range(self.size):

                if self.flags[row][col]:

                    current.append("F")

                elif self.visible[row][col]:

                    current.append(
                        str(self.board[row][col])
                    )

                else:

                    current.append("X")

            display.append(current)

        return display

    def find_safe_hint(self):

        queue = deque()

        for row in range(self.size):

            for col in range(self.size):

                queue.append((row, col))

        while queue:

            row, col = queue.popleft()

            if (
                self.board[row][col] != "M"
                and not self.visible[row][col]
            ):

                return [row, col]

        return None