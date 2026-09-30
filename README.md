# rock-paper-scissor-
# ROCK PAPER SCISSORS GAME USING PYTHON AND PYGAME

## 1. Abstract

The **Rock Paper Scissors Game** is a graphical computer game developed using **Python** and the **Pygame** library. The game allows a player to compete against the computer by selecting Rock, Paper, or Scissors. The computer generates its choice randomly, and the winner is determined according to the traditional rules of the game.

The project includes a graphical user interface, mouse-based controls, countdown timer, score tracking, sound effects, button animations, game states, restart functionality, and a first-to-five scoring system. The project demonstrates important Python programming concepts such as variables, lists, conditional statements, functions, loops, random number generation, event handling, and basic object-oriented concepts of game development through Pygame.

---

# 2. Introduction

Rock Paper Scissors is a simple decision-based game played between two participants. Each participant chooses one of three options:

* Rock
* Paper
* Scissors

The rules are:

* Rock defeats Scissors.
* Scissors defeats Paper.
* Paper defeats Rock.
* If both players choose the same option, the round is a draw.

In this project, the player interacts with the computer through a graphical interface. Pygame is used to create the game window, buttons, graphics, animations, sound effects, and keyboard and mouse interactions.

The project was developed to understand how Python can be used not only for basic programming tasks but also for creating interactive graphical applications.

---

# 3. Problem Statement

The objective is to develop an interactive Rock Paper Scissors game in Python where a user can play against a computer-controlled opponent through a graphical interface.

The system should:

1. Allow the player to select Rock, Paper, or Scissors.
2. Generate a random choice for the computer.
3. Compare the player's choice with the computer's choice.
4. Determine the winner of each round.
5. Maintain the scores.
6. Provide a countdown before displaying the result.
7. Provide sound effects.
8. Allow the player to restart or return to the main menu.
9. End the match when either player reaches five points.

---

# 4. Objectives

The main objectives of this project are:

* To develop a simple graphical game using Python.
* To understand the basics of Pygame.
* To implement random choice generation.
* To practice conditional statements.
* To understand functions and modular programming.
* To implement mouse and keyboard event handling.
* To create graphical buttons and game elements.
* To implement score tracking.
* To implement a countdown timer.
* To add sound effects.
* To understand game states and game loops.
* To improve problem-solving and programming skills.

---

# 5. Technologies Used

## Programming Language

**Python**

Python is used to implement the complete game logic and application.

## Library

**Pygame**

Pygame is used for:

* Creating the game window
* Drawing graphics
* Handling keyboard and mouse events
* Rendering text
* Creating buttons
* Playing sounds
* Controlling the game loop
* Managing timing

## Development Environment

The project can be developed using:

* Visual Studio Code
* Python
* Pygame

---

# 6. Hardware Requirements

The game does not require high-end hardware.

### Minimum Requirements

* Processor: Dual-core processor or better
* RAM: 4 GB
* Storage: Approximately 100 MB free space
* Keyboard
* Mouse
* Display

---

# 7. Software Requirements

* Windows/Linux/macOS
* Python 3.x
* Pygame library
* Visual Studio Code or another Python IDE

Pygame can be installed using:

```bash
python -m pip install pygame
```

---

# 8. Game Rules

The game follows the traditional Rock Paper Scissors rules.

| Player Choice      | Computer Choice | Result        |
| ------------------ | --------------- | ------------- |
| Rock               | Scissors        | Player Wins   |
| Scissors           | Paper           | Player Wins   |
| Paper              | Rock            | Player Wins   |
| Same Choice        | Same Choice     | Draw          |
| Other combinations |                 | Computer Wins |

The match uses a **first-to-five** scoring system.

The player or computer who reaches five points first wins the match.

---

# 9. System Design

The game consists of several major components:

### 1. Main Menu

The main menu provides:

* Play button
* Quit button
* Game title

### 2. Game Screen

The game screen displays:

* Player score
* Computer score
* Rock button
* Paper button
* Scissors button
* Graphics

### 3. Countdown System

After the player selects an option, a countdown is displayed before the result.

Example:

```text
3
2
1
```

### 4. Result Screen

The result screen displays:

* Player's choice
* Computer's choice
* Round result
* Current score
* Play Again button
* Main Menu button

### 5. Game Over Screen

The game ends when either player reaches five points.

---

# 10. Game Flow

The basic flow of the game is:

```text
START
  ↓
MAIN MENU
  ↓
PLAYER CLICKS PLAY
  ↓
GAME SCREEN
  ↓
PLAYER SELECTS ROCK/PAPER/SCISSORS
  ↓
COMPUTER RANDOMLY SELECTS
  ↓
3 SECOND COUNTDOWN
  ↓
COMPARE CHOICES
  ↓
DISPLAY RESULT
  ↓
UPDATE SCORE
  ↓
HAS SOMEONE REACHED 5?
  ↓
   NO ──────────────→ PLAY AGAIN
  ↓
 YES
  ↓
GAME OVER
  ↓
RESTART / MAIN MENU
```

---

# 11. Algorithm

### Step 1

Start the program.

### Step 2

Initialize Pygame and create the game window.

### Step 3

Create the Rock, Paper, and Scissors choices.

### Step 4

Display the main menu.

### Step 5

When the player clicks Play, start the game.

### Step 6

Display the three choices.

### Step 7

Wait for the player to select an option.

### Step 8

Generate the computer's choice using random selection.

### Step 9

Start the countdown.

### Step 10

Compare the player's choice with the computer's choice.

### Step 11

Determine whether the result is:

* Player wins
* Computer wins
* Draw

### Step 12

Update the appropriate score.

### Step 13

Check whether either player has reached five points.

### Step 14

If nobody has reached five, continue playing.

### Step 15

If someone reaches five, display the Game Over screen.

### Step 16

Allow the player to restart or return to the main menu.

### Step 17

Exit the program when Quit or ESC is selected.

---

# 12. Important Python Concepts Used

## Variables

Variables store information such as:

```python
player_score = 0
computer_score = 0
```

These variables keep track of the scores.

---

## Lists

The available choices are stored in a list:

```python
choices = ["rock", "paper", "scissors"]
```

---

## Random Selection

The computer selects a random choice:

```python
computer_choice = random.choice(choices)
```

This prevents the computer from always selecting the same option.

---

## Conditional Statements

The winner is determined using `if`, `elif`, and `else`.

For example:

```python
if player == computer:
    return "draw"
```

The program checks different combinations and determines the winner.

---

# 13. Functions

The project uses functions to divide the program into smaller components.

Examples include:

```python
create_sound()
draw_text()
draw_button()
draw_rock()
draw_paper()
draw_scissors()
get_winner()
reset_game()
start_round()
finish_round()
```

Functions make the program easier to understand, maintain, and modify.

---

# 14. Pygame Game Loop

The game uses a continuous loop:

```python
while running:
```

The game loop repeatedly performs three main tasks:

1. Check events.
2. Update the game.
3. Draw the game.

The screen is then updated using:

```python
pygame.display.update()
```

The game loop is one of the most important concepts in Pygame development.

---

# 15. Event Handling

Pygame events allow the program to respond to user actions.

For example:

```python
if event.type == pygame.MOUSEBUTTONDOWN:
```

detects mouse clicks.

Keyboard events can also be detected:

```python
if event.type == pygame.KEYDOWN:
```

This allows the game to respond to keyboard input.

---

# 16. Graphical Elements

The project creates its graphics programmatically using Pygame.

### Rock

A polygon is used to create the Rock shape.

### Paper

A rectangle is used to represent Paper.

### Scissors

Lines and circles are combined to create the Scissors graphic.

Buttons are created using:

```python
pygame.Rect()
```

and drawn using:

```python
pygame.draw.rect()
```

---

# 17. Sound Effects

The project includes sound effects for different actions.

Examples include:

* Button click
* Countdown
* Winning a round
* Losing a round
* Drawing a round

The sounds are generated using Python and Pygame's mixer functionality.

This allows the game to provide audio feedback without requiring external audio files.

---

# 18. Game States

The game uses different states to control which screen is displayed.

Examples:

```text
menu
playing
countdown
result
game_over
```

The state determines what the player can do and what the program should display.

For example:

```python
if game_state == "menu":
```

displays the main menu.

Similarly:

```python
elif game_state == "playing":
```

displays the gameplay screen.

This approach makes the game easier to organize.

---

# 19. Testing

The game was tested using different possible combinations.

| Test Case            | Expected Result |
| -------------------- | --------------- |
| Rock vs Rock         | Draw            |
| Rock vs Paper        | Computer Wins   |
| Rock vs Scissors     | Player Wins     |
| Paper vs Rock        | Player Wins     |
| Paper vs Paper       | Draw            |
| Paper vs Scissors    | Computer Wins   |
| Scissors vs Rock     | Computer Wins   |
| Scissors vs Paper    | Player Wins     |
| Scissors vs Scissors | Draw            |
| Player reaches 5     | Game Over       |
| Computer reaches 5   | Game Over       |
| Quit button          | Program closes  |
| Restart button       | New game starts |

---

# 20. Features

The final project provides the following features:

* Graphical user interface
* Mouse-controlled buttons
* Rock, Paper, and Scissors graphics
* Random computer selection
* Score tracking
* First-to-five game system
* Countdown timer
* Sound effects
* Button hover effects
* Main menu
* Game Over screen
* Restart functionality
* Main Menu functionality
* Keyboard controls
* Programmatically generated graphics
* Programmatically generated sound effects

---

# 21. Advantages

* Simple and easy to understand.
* Interactive graphical interface.
* Helps beginners understand game development.
* Demonstrates Python programming concepts.
* Uses randomization.
* Provides immediate feedback.
* Does not require complex hardware.
* Can be extended with additional features.

---

# 22. Limitations

* The game currently supports only a single player against the computer.
* The computer does not use advanced decision-making strategies.
* Graphics are basic and programmatically generated.
* There is no online multiplayer mode.
* The game does not save player statistics permanently.

---

# 23. Future Enhancements

The project can be improved by adding:

* Online multiplayer.
* Local two-player mode.
* More advanced animations.
* Background music.
* Improved graphical assets.
* Difficulty levels.
* Persistent high scores.
* Player profiles.
* Tournament mode.
* Additional game modes.
* Mobile or web version.

---

# 24. Learning Outcomes

After completing this project, the following concepts were understood:

* Python programming fundamentals.
* Variables and data types.
* Lists.
* Conditional statements.
* Loops.
* Functions.
* Random number generation.
* Pygame initialization.
* Pygame game loops.
* Mouse event handling.
* Keyboard event handling.
* Graphics rendering.
* Text rendering.
* Timers.
* Sound generation and playback.
* Game state management.
* Basic game design.

---

# 25. Conclusion

The **Rock Paper Scissors Game using Python and Pygame** successfully demonstrates how Python can be used to develop an interactive graphical game.

The project combines programming logic with graphical design, user interaction, randomization, scoring, timing, and sound effects. It provides practical experience with Pygame and demonstrates how a simple command-line game can be transformed into a complete graphical application.

The project also provides a foundation for developing more advanced games and interactive applications using Python.

---

# 26. References

1. Python Documentation
2. Pygame Documentation
3. Python Random Module Documentation
4. Python Math Module Documentation
5. Pygame Mixer Documentation
6. Pygame Drawing and Event Handling Documentation
