#Epic Rock Paper Scissors Battle:

Description:
This is a command-line based Rock Paper Scissors game for two players. Players take turns to input their moves in secret, and the game determines the winner based on traditional Rock Paper Scissors rules. The game continues until one player reaches three wins.

Features:
1. Secret input for both players using getpass to ensure fair play.
2. Keeps score and announces the winner after a player wins three rounds.
3. Input validation to ensure moves are either 'R', 'P', or 'S'.

How It Works:
- Both players are prompted to enter their moves ('R' for Rock, 'P' for Paper, 'S' for Scissors) in secret.
- The game checks the moves and determines the winner of each round based on the rules:
   * Rock beats Scissors
   * Scissors beats Paper
   * Paper beats Rock
- The game continues until one player wins three rounds.
- The game announces the overall winner and exits.
