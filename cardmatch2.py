import random
import time

FRUITS = ["🍎", "🍌", "🍇", "🍉", "🍓", "🍍", "🍒", "🥝"] * 2
SIZE = 4

class MemoryGame:
    def __init__(self):
        self.board = [[None] * SIZE for _ in range(SIZE)]
        self.visible = [[False] * SIZE for _ in range(SIZE)]
        self.revealed = [[None] * SIZE for _ in range(SIZE)]
        self.matched = [[False] * SIZE for _ in range(SIZE)]
        self.owners = [[None] * SIZE for _ in range(SIZE)]
        self.ai_memory = {}
        self.scores = [0, 0]  # Player, AI
        self.consecutive_misses = [0, 0]  # Player, AI
        self.current_player = 0
        self.setup_board()

    def setup_board(self):
        cards = FRUITS.copy()
        random.shuffle(cards)
        for i in range(SIZE):
            for j in range(SIZE):
                self.board[i][j] = cards.pop()

    def print_board(self):
        print("\n    " + "   ".join(map(str, range(SIZE))))
        print("  +" + "+".join(["-----"] * SIZE) + "+")
        for i in range(SIZE):
            row = f"{i} |"
            for j in range(SIZE):
                if self.visible[i][j] or self.matched[i][j]:
                    row += f" {self.board[i][j]} |"
                else:
                    row += " ■ |"
            print(row)
            print("  +" + "+".join(["-----"] * SIZE) + "+")

    def get_input(self):
        while True:
            try:
                row, col = map(int, input("Enter row and col (e.g., 0 1): ").split())
                if 0 <= row < SIZE and 0 <= col < SIZE and not self.visible[row][col] and not self.matched[row][col]:
                    return row, col
                else:
                    print("Invalid or already revealed cell. Try again.")
            except:
                print("Invalid input. Use format: row col")

    def reveal(self, row, col):
        self.visible[row][col] = True
        self.revealed[row][col] = self.board[row][col]
        self.ai_memory[(row, col)] = self.board[row][col]

    def hide(self, row1, col1, row2, col2):
        self.visible[row1][col1] = False
        self.visible[row2][col2] = False

    def mark_matched(self, row1, col1, row2, col2):
        self.matched[row1][col1] = True
        self.matched[row2][col2] = True
        self.owners[row1][col1] = self.owners[row2][col2] = self.current_player
        self.scores[self.current_player] += 1

    def ai_turn(self):
        print("🤖 AI is thinking...")
        time.sleep(1)

        for (r1, c1), fruit1 in self.ai_memory.items():
            if self.matched[r1][c1]:
                continue
            for (r2, c2), fruit2 in self.ai_memory.items():
                if (r1, c1) != (r2, c2) and fruit1 == fruit2 and not self.matched[r2][c2]:
                    return (r1, c1), (r2, c2)

        unseen = [(i, j) for i in range(SIZE) for j in range(SIZE) if not self.matched[i][j] and not self.visible[i][j]]
        random.shuffle(unseen)
        return unseen[0], unseen[1]

    def penalty_reshuffle(self):
        print("\n🔄 Penalty reshuffling: Returning one matched pair to the board.\n")

        matched_pairs = [(i, j) for i in range(SIZE) for j in range(SIZE) if self.matched[i][j] and self.owners[i][j] == self.current_player]
        fruit_to_coords = {}
        for i, j in matched_pairs:
            fruit = self.board[i][j]
            fruit_to_coords.setdefault(fruit, []).append((i, j))

        removable_pairs = [coords for coords in fruit_to_coords.values() if len(coords) == 2]
        if not removable_pairs:
            print("No matched pair to return.")
            return

        pair = random.choice(removable_pairs)
        for i, j in pair:
            self.matched[i][j] = False
            self.owners[i][j] = None

        # Collect only the non-matched positions
        reshuffle_positions = [(i, j) for i in range(SIZE) for j in range(SIZE)
                               if not self.matched[i][j]]
        cards = [self.board[i][j] for i, j in reshuffle_positions]
        random.shuffle(cards)
        for (i, j), card in zip(reshuffle_positions, cards):
            self.board[i][j] = card

        self.visible = [[False] * SIZE for _ in range(SIZE)]
        self.revealed = [[None] * SIZE for _ in range(SIZE)]
        self.ai_memory.clear()

    def play(self):
        print("\n🎉 Welcome to Purble Pairs Game: 2 Players Edition! 🍒\n")
        while any(not self.matched[i][j] for i in range(SIZE) for j in range(SIZE)):
            print(f"🎮 Player {'1' if self.current_player == 0 else '2 (AI)'}'s turn")
            self.print_board()

            if self.current_player == 0:
                r1, c1 = self.get_input()
                self.reveal(r1, c1)
                self.print_board()
                r2, c2 = self.get_input()
                self.reveal(r2, c2)
            else:
                (r1, c1), (r2, c2) = self.ai_turn()
                print(f"🤖 AI selects ({r1}, {c1}) and ({r2}, {c2})")
                self.reveal(r1, c1)
                self.reveal(r2, c2)

            self.print_board()

            if self.board[r1][c1] == self.board[r2][c2]:
                print("✅ MATCH FOUND!")
                self.mark_matched(r1, c1, r2, c2)
                self.consecutive_misses[self.current_player] = 0
            else:
                print("❌ NO MATCH! Switching Turn...")
                time.sleep(1)
                self.hide(r1, c1, r2, c2)
                self.consecutive_misses[self.current_player] += 1
                if self.consecutive_misses[self.current_player] == 3:
                    self.penalty_reshuffle()
                    self.consecutive_misses = [0, 0]
                self.current_player = 1 - self.current_player

        print("\n🏁 Game Over!")
        print(f"Final Scores => Player: {self.scores[0]}, AI: {self.scores[1]}")
        if self.scores[0] > self.scores[1]:
            print("🎉 You win!")
        elif self.scores[0] < self.scores[1]:
            print("🤖 AI wins!")
        else:
            print("🤝 It's a tie!")

if __name__ == "__main__":
    game = MemoryGame()
    game.play()

