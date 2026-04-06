# Rulette
Python-based European Roulette Simulator with persistent data storage and complex bet-matching logic. Features include multi-type betting (colors, sectors, lines, ranges), user balance management via file I/O, and a custom probability engine.

## 🎰 Roulette Simulator Engine

A functional simulation of a European Roulette game developed to demonstrate core Python proficiency, file handling, and complex conditional logic.

### 🛠 Key Technical Features:
*   **Persistent User Sessions:** Implemented a file-based database (`users.txt`) to save and load user balances, ensuring data persistence between game sessions.
*   **Complex Bet Matching Logic:** Developed an extensible engine that processes multiple bet types simultaneously:
    *   **Inside Bets:** Straight numbers (0-36).
    *   **Outside Bets:** Colors (Red/Black/Green), Even/Odd, Dozens (1-12, etc.), and Columns/Lines[cite: 3].
*   **Dynamic State Management:** Real-time balance updates, bet validation, and payout calculations (up to 36x for "Green" bets)[cite: 3].
*   **Input Validation:** Robust error handling for invalid bets and insufficient funds to ensure a smooth UX[cite: 3].

### 💻 Tech Stack:
- **Language:** Python 3.x
- **Modules:** `random` (for probability generation), `file I/O` (for data storage)[cite: 3, 4, 5].

### 📈 Future Improvements:
- Transition from file-based storage to a SQL database (PostgreSQL/SQLite).
- Integration with a FastAPI/Flask web interface.
