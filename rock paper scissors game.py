import pygame
import random
import sys
import math
import array


# ============================================================
# INITIALIZATION
# ============================================================

pygame.init()
pygame.mixer.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

clock = pygame.time.Clock()
FPS = 60


# ============================================================
# COLORS
# ============================================================

BACKGROUND = (18, 20, 30)
PANEL = (30, 33, 48)
BUTTON = (55, 60, 85)
BUTTON_HOVER = (75, 82, 115)

WHITE = (245, 245, 250)
GRAY = (160, 165, 180)

RED = (230, 70, 80)
GREEN = (70, 210, 120)
BLUE = (70, 150, 240)
YELLOW = (245, 200, 70)


# ============================================================
# FONTS
# ============================================================

title_font = pygame.font.Font(None, 80)
large_font = pygame.font.Font(None, 60)
medium_font = pygame.font.Font(None, 42)
small_font = pygame.font.Font(None, 30)


# ============================================================
# GAME VARIABLES
# ============================================================

choices = ["rock", "paper", "scissors"]

player_choice = None
computer_choice = None

player_score = 0
computer_score = 0

result = ""

game_state = "menu"

countdown = 3
countdown_start = 0

result_start = 0


# ============================================================
# BUTTONS
# ============================================================

play_button = pygame.Rect(350, 300, 300, 70)
quit_button = pygame.Rect(350, 400, 300, 70)

rock_button = pygame.Rect(100, 500, 220, 80)
paper_button = pygame.Rect(390, 500, 220, 80)
scissors_button = pygame.Rect(680, 500, 220, 80)

again_button = pygame.Rect(280, 500, 200, 65)
menu_button = pygame.Rect(520, 500, 200, 65)


# ============================================================
# SOUND GENERATION
# ============================================================

def create_sound(frequency, duration):

    sample_rate = 44100

    number_of_samples = int(sample_rate * duration)

    buffer = array.array("h")

    for i in range(number_of_samples):

        value = int(
            16000 *
            math.sin(
                2 * math.pi *
                frequency *
                i /
                sample_rate
            )
        )

        buffer.append(value)

    return pygame.mixer.Sound(buffer=buffer)


click_sound = create_sound(600, 0.08)
win_sound = create_sound(900, 0.20)
lose_sound = create_sound(250, 0.20)
draw_sound = create_sound(500, 0.12)


# ============================================================
# DRAW TEXT FUNCTION
# ============================================================

def draw_text(text, font, color, x, y, center=True):

    surface = font.render(text, True, color)

    if center:

        rect = surface.get_rect(center=(x, y))

    else:

        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)


# ============================================================
# DRAW BUTTON FUNCTION
# ============================================================

def draw_button(rect, text, mouse_pos):

    if rect.collidepoint(mouse_pos):

        color = BUTTON_HOVER

    else:

        color = BUTTON

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        WHITE,
        rect,
        2,
        border_radius=15
    )

    draw_text(
        text,
        medium_font,
        WHITE,
        rect.centerx,
        rect.centery
    )


# ============================================================
# DRAW ROCK
# ============================================================

def draw_rock(x, y, scale=1):

    points = [
        (x - 45 * scale, y + 25 * scale),
        (x - 35 * scale, y - 30 * scale),
        (x - 5 * scale, y - 50 * scale),
        (x + 35 * scale, y - 25 * scale),
        (x + 50 * scale, y + 20 * scale),
        (x + 20 * scale, y + 45 * scale),
        (x - 25 * scale, y + 45 * scale)
    ]

    pygame.draw.polygon(
        screen,
        GRAY,
        points
    )

    pygame.draw.polygon(
        screen,
        WHITE,
        points,
        3
    )


# ============================================================
# DRAW PAPER
# ============================================================

def draw_paper(x, y, scale=1):

    rect = pygame.Rect(
        x - 40 * scale,
        y - 55 * scale,
        80 * scale,
        110 * scale
    )

    pygame.draw.rect(
        screen,
        WHITE,
        rect,
        border_radius=5
    )

    pygame.draw.rect(
        screen,
        BLUE,
        rect,
        4,
        border_radius=5
    )

    for i in range(3):

        pygame.draw.line(
            screen,
            BLUE,
            (
                x - 25 * scale,
                y - 20 * scale + i * 20 * scale
            ),
            (
                x + 25 * scale,
                y - 20 * scale + i * 20 * scale
            ),
            max(1, int(3 * scale))
        )


# ============================================================
# DRAW SCISSORS
# ============================================================

def draw_scissors(x, y, scale=1):

    pygame.draw.circle(
        screen,
        RED,
        (
            int(x - 20 * scale),
            int(y + 20 * scale)
        ),
        int(13 * scale)
    )

    pygame.draw.circle(
        screen,
        RED,
        (
            int(x + 20 * scale),
            int(y + 20 * scale)
        ),
        int(13 * scale)
    )

    pygame.draw.line(
        screen,
        RED,
        (x - 12 * scale, y + 10 * scale),
        (x - 45 * scale, y - 45 * scale),
        max(2, int(8 * scale))
    )

    pygame.draw.line(
        screen,
        RED,
        (x + 12 * scale, y + 10 * scale),
        (x + 45 * scale, y - 45 * scale),
        max(2, int(8 * scale))
    )


# ============================================================
# DRAW CHOICE GRAPHIC
# ============================================================

def draw_choice(choice, x, y, scale=1):

    if choice == "rock":

        draw_rock(x, y, scale)

    elif choice == "paper":

        draw_paper(x, y, scale)

    elif choice == "scissors":

        draw_scissors(x, y, scale)


# ============================================================
# WINNER LOGIC
# ============================================================

def get_winner(player, computer):

    if player == computer:

        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or
        (player == "paper" and computer == "rock")
        or
        (player == "scissors" and computer == "paper")
    ):

        return "player"

    return "computer"


# ============================================================
# RESET GAME
# ============================================================

def reset_game():

    global player_choice
    global computer_choice
    global player_score
    global computer_score
    global result
    global game_state

    player_choice = None
    computer_choice = None

    player_score = 0
    computer_score = 0

    result = ""

    game_state = "playing"


# ============================================================
# START ROUND
# ============================================================

def start_round(choice):

    global player_choice
    global computer_choice
    global result
    global countdown
    global countdown_start
    global game_state

    player_choice = choice

    computer_choice = random.choice(choices)

    countdown = 3

    countdown_start = pygame.time.get_ticks()

    result = ""

    game_state = "countdown"

    click_sound.play()


# ============================================================
# FINISH ROUND
# ============================================================

def finish_round():

    global player_score
    global computer_score
    global result
    global game_state
    global result_start

    winner = get_winner(
        player_choice,
        computer_choice
    )

    if winner == "player":

        player_score += 1

        result = "YOU WIN!"

        win_sound.play()

    elif winner == "computer":

        computer_score += 1

        result = "COMPUTER WINS!"

        lose_sound.play()

    else:

        result = "DRAW!"

        draw_sound.play()

    result_start = pygame.time.get_ticks()

    game_state = "result"


# ============================================================
# DRAW SCORE
# ============================================================

def draw_score():

    draw_text(
        f"You: {player_score}",
        medium_font,
        GREEN,
        200,
        80
    )

    draw_text(
        f"Computer: {computer_score}",
        medium_font,
        RED,
        800,
        80
    )


# ============================================================
# MAIN LOOP
# ============================================================

running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # ----------------------------------------------------
        # MENU EVENTS
        # ----------------------------------------------------

        if game_state == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(event.pos):

                    reset_game()

                    click_sound.play()

                elif quit_button.collidepoint(event.pos):

                    running = False


        # ----------------------------------------------------
        # PLAYING EVENTS
        # ----------------------------------------------------

        elif game_state == "playing":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if rock_button.collidepoint(event.pos):

                    start_round("rock")

                elif paper_button.collidepoint(event.pos):

                    start_round("paper")

                elif scissors_button.collidepoint(event.pos):

                    start_round("scissors")


        # ----------------------------------------------------
        # RESULT EVENTS
        # ----------------------------------------------------

        elif game_state == "result":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if again_button.collidepoint(event.pos):

                    game_state = "playing"

                    click_sound.play()

                elif menu_button.collidepoint(event.pos):

                    game_state = "menu"

                    player_score = 0
                    computer_score = 0

                    click_sound.play()


        # ----------------------------------------------------
        # GAME OVER EVENTS
        # ----------------------------------------------------

        elif game_state == "game_over":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if again_button.collidepoint(event.pos):

                    reset_game()

                    click_sound.play()

                elif menu_button.collidepoint(event.pos):

                    game_state = "menu"

                    click_sound.play()


    # ========================================================
    # GAME LOGIC
    # ========================================================

    if game_state == "countdown":

        current_time = pygame.time.get_ticks()

        elapsed = (
            current_time -
            countdown_start
        ) / 1000

        countdown = 3 - int(elapsed)

        if elapsed >= 3:

            finish_round()


    # Check first-to-five condition

    if player_score >= 5:

        game_state = "game_over"

        result = "YOU ARE THE CHAMPION!"

    elif computer_score >= 5:

        game_state = "game_over"

        result = "COMPUTER WINS THE MATCH!"


    # ========================================================
    # DRAW BACKGROUND
    # ========================================================

    screen.fill(BACKGROUND)

    # ========================================================
    # MENU SCREEN
    # ========================================================

    if game_state == "menu":

        draw_text(
            "ROCK PAPER SCISSORS",
            title_font,
            WHITE,
            WIDTH // 2,
            150
        )

        draw_text(
            "FIRST TO 5 WINS",
            medium_font,
            GRAY,
            WIDTH // 2,
            220
        )

        draw_button(
            play_button,
            "PLAY",
            mouse_pos
        )

        draw_button(
            quit_button,
            "QUIT",
            mouse_pos
        )


    # ========================================================
    # PLAYING SCREEN
    # ========================================================

    elif game_state == "playing":

        draw_text(
            "CHOOSE YOUR MOVE",
            title_font,
            WHITE,
            WIDTH // 2,
            120
        )

        draw_score()

        draw_button(
            rock_button,
            "ROCK",
            mouse_pos
        )

        draw_button(
            paper_button,
            "PAPER",
            mouse_pos
        )

        draw_button(
            scissors_button,
            "SCISSORS",
            mouse_pos
        )

        draw_rock(
            250,
            350,
            1.3
        )

        draw_paper(
            500,
            350,
            1.3
        )

        draw_scissors(
            750,
            350,
            1.3
        )


    # ========================================================
    # COUNTDOWN SCREEN
    # ========================================================

    elif game_state == "countdown":

        draw_score()

        draw_text(
            "YOUR CHOICE",
            medium_font,
            GREEN,
            250,
            150
        )

        draw_text(
            "COMPUTER",
            medium_font,
            RED,
            750,
            150
        )

        draw_choice(
            player_choice,
            250,
            300,
            1.5
        )

        draw_text(
            "?",
            title_font,
            YELLOW,
            750,
            300
        )

        draw_text(
            str(max(countdown, 1)),
            title_font,
            YELLOW,
            WIDTH // 2,
            500
        )


    # ========================================================
    # RESULT SCREEN
    # ========================================================

    elif game_state == "result":

        draw_score()

        draw_text(
            "YOUR CHOICE",
            medium_font,
            GREEN,
            250,
            150
        )

        draw_text(
            "COMPUTER",
            medium_font,
            RED,
            750,
            150
        )

        draw_choice(
            player_choice,
            250,
            300,
            1.5
        )

        draw_choice(
            computer_choice,
            750,
            300,
            1.5
        )

        result_color = WHITE

        if result == "YOU WIN!":

            result_color = GREEN

        elif result == "COMPUTER WINS!":

            result_color = RED

        elif result == "DRAW!":

            result_color = YELLOW

        draw_text(
            result,
            large_font,
            result_color,
            WIDTH // 2,
            420
        )

        draw_button(
            again_button,
            "PLAY AGAIN",
            mouse_pos
        )

        draw_button(
            menu_button,
            "MAIN MENU",
            mouse_pos
        )


    # ========================================================
    # GAME OVER SCREEN
    # ========================================================

    elif game_state == "game_over":

        draw_text(
            "MATCH OVER",
            title_font,
            WHITE,
            WIDTH // 2,
            150
        )

        if player_score >= 5:

            draw_text(
                "YOU ARE THE CHAMPION!",
                large_font,
                GREEN,
                WIDTH // 2,
                250
            )

        else:

            draw_text(
                "COMPUTER WINS THE MATCH!",
                large_font,
                RED,
                WIDTH // 2,
                250
            )

        draw_text(
            f"{player_score}  -  {computer_score}",
            title_font,
            YELLOW,
            WIDTH // 2,
            350
        )

        draw_button(
            again_button,
            "PLAY AGAIN",
            mouse_pos
        )

        draw_button(
            menu_button,
            "MAIN MENU",
            mouse_pos
        )


    # ========================================================
    # UPDATE DISPLAY
    # ========================================================

    pygame.display.update()

    clock.tick(FPS)


# ============================================================
# QUIT
# ============================================================

pygame.quit()
sys.exit()
