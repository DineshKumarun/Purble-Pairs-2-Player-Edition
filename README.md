# Purble Pairs: 2 Player Edition

A memory-based **2-player matching game** (Human vs AI) built using Python. This project features an intelligent adversarial AI that mimics human memory and strategy.

![Python Version](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python) ![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## Table of Contents
- [Game Overview](#game-overview)
- [Features](#features)
- [AI Strategy](#ai-strategy)
- [Penalty Reshuffle](#penalty-reshuffle)
- [Why NP-Hard?](#why-np-hard)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Files](#files)
- [License](#license)

---

## Game Overview

- **Grid**: 4x4 board with 8 fruit emoji pairs (16 cards total)
- **Players**: Human (Player 1) vs AI (Player 2)
- **Goal**: Match the most pairs before the board is cleared
- **Platform**: Command-line interface (CLI)
- **Scoring**: Each matched pair earns 1 point
- **Turn System**: Players alternate turns, but keep their turn after a successful match

---

## Features

- Turn-based gameplay with score tracking
- Intelligent AI opponent with memory capabilities
- Penalty reshuffling after 3 consecutive failed attempts
- Matched pair ownership tracking
- Clear CLI display of the board and moves
- Dynamic board reshuffling under penalty conditions
- Competitive scoring system

---

## AI Strategy

The AI mimics **Adversarial Search**, prioritizing winning moves and minimizing human gains. It implements:

- Memory-based matching:
  - Stores all previously revealed cards
  - Makes guaranteed matches if found in memory
  - Chooses randomly from unseen cards otherwise
- Avoids matched or owned cards
- Adaptive reshuffling response
- Turn retention logic

This behavior emulates **Minimax reasoning** without full tree search, making gameplay intelligent yet lightweight.

---

## Penalty Reshuffle

After a player makes 3 failed attempts in a row:
1. One of their previously matched pairs is returned to the board
2. All unmatched cards are shuffled
3. AI memory and visibility are reset
4. Both players' consecutive miss counters are reset

This adds complexity and strategic tension to the game, punishing players for poor memory while keeping the game competitive.

---

## Why NP-Hard?

Although basic matching is polynomial, this version introduces complex elements:

- **Hidden information**: Partial board visibility
- **Dynamic reshuffling**: Board state changes unpredictably
- **Constraint interactions**: 
  - Turn retention
  - Pair ownership
  - Penalty conditions
- **Optimization challenge**: Finding the best move sequence

Result: It becomes a **Constraint Optimization Problem with Incomplete Information**, exhibiting **NP-Hard** characteristics.

---

## Installation

1. Ensure you have Python 3.10 or later installed
2. Clone this repository or download the `cardmatch2.py` file
3. No additional dependencies are required

---

## How to Play

1. Run the game:
   ```bash
   python cardmatch2.py
   
2. Gameplay instructions:
    - The board will display as a 4x4 grid of hidden cards (■)
    - On your turn, enter row and column numbers (e.g., "0 1") to flip cards
    - Try to find matching pairs of fruit emojis
    - If you find a match, you keep your turn
    - If you fail to match, the AI takes its turn
    - After 3 consecutive misses, a penalty reshuffle occurs
    
3. The game ends when all pairs are matched, and the final scores are displayed.


## Files

| File | Description |
|------|-------------|
| `cardmatch2.py` | Main Python file with game logic and AI |
| `AI_report-1.pdf` | Full report explaining the AI approach, rules, NP-hardness, and code strategy |

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute this project for educational or personal purposes.

