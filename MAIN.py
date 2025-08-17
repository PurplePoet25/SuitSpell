import os
import random
import tkinter as tk
import sys
from PIL import Image, ImageTk

# === HELPER ===
def resource_path(relative_path):
    """ Get absolute path to resource (for PyInstaller .exe builds) """
    try:
        base_path = sys._MEIPASS  # temp folder for PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# === CONFIG ===
CARD_SHEET_PATH = resource_path("playing_cards.png")
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400 


RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

# === QUOTES ===
card_quotes = {
    # ♠ Spades
    "A of Spades": "The edge of ambition cuts cleanest in silence.",
    "2 of Spades": "One spark splits loyalty from defiance.",
    "3 of Spades": "Every plan is a triangle: sharp, simple, risky.",
    "4 of Spades": "Stability is a sword stabbed into the ground.",
    "5 of Spades": "Control is louder when whispered, not shouted.",
    "6 of Spades": "Discipline grows in even-numbered steps.",
    "7 of Spades": "A lone force sharpens itself through resistance.",
    "8 of Spades": "Power layered is power protected.",
    "9 of Spades": "A storm prepares long before the first wind.",
    "10 of Spades": "Dominance is a habit, not a flare.",
    "J of Spades": "Charm is just strategy with a smile.",
    "Q of Spades": "She commands not by fear, but by certainty.",
    "K of Spades": "Every throne is balanced on a blade.",
    "Joker1": "Chaos is a coin flip in clown shoes — and it always lands sideways.",

    # ♥ Hearts
    "A of Hearts": "Love starts soft — and ends loud.",
    "2 of Hearts": "Two beats in sync can shake the sky.",
    "3 of Hearts": "Harmony is messier than you’d think.",
    "4 of Hearts": "Safety is a song you hum to yourself.",
    "5 of Hearts": "Even peace picks favorites.",
    "6 of Hearts": "Kindness is a pattern, not an impulse.",
    "7 of Hearts": "Empathy grows best in the cracks.",
    "8 of Hearts": "Emotion needs rhythm to breathe.",
    "9 of Hearts": "Hope lingers even after the candles die.",
    "10 of Hearts": "Love doesn’t win — it overwhelms.",
    "J of Hearts": "He flirts with the world and means every word.",
    "Q of Hearts": "She sees through wounds like windows.",
    "K of Hearts": "A king who feels deeply rules gently.",
    "Joker2": "The fool dances where logic won’t go — and somehow gets it right.",

    # ♣ Clubs
    "A of Clubs": "The first detail matters most.",
    "2 of Clubs": "Binary minds split everything — perfectly.",
    "3 of Clubs": "Patterns hide in threes and in silence.",
    "4 of Clubs": "Precision is peace arranged in squares.",
    "5 of Clubs": "Chaos fears the consistent.",
    "6 of Clubs": "Order walks in pairs of three.",
    "7 of Clubs": "A sharp mind bends odd numbers to its will.",
    "8 of Clubs": "Even logic spirals into beauty.",
    "9 of Clubs": "Every answer is a maze pretending to be a door.",
    "10 of Clubs": "Mastery counts every click, every tick, every breath.",
    "J of Clubs": "He plans ten steps ahead — and only tells you five.",
    "Q of Clubs": "She edits the universe with a smirk.",
    "K of Clubs": "His throne is made of bullet points and blueprints.",

    # ♦ Diamonds
    "A of Diamonds": "Even alone, a gem still gleams.",
    "2 of Diamonds": "Spotlight’s better when it’s shared.",
    "3 of Diamonds": "Drama loves company — and applause.",
    "4 of Diamonds": "Glamour needs grounding to truly shine.",
    "5 of Diamonds": "Not all sparkle is shallow — but some is deliciously so.",
    "6 of Diamonds": "Beauty builds in repetition.",
    "7 of Diamonds": "Dazzle them, confuse them, win anyway.",
    "8 of Diamonds": "Shine stacked on shine becomes unstoppable.",
    "9 of Diamonds": "They’ll remember the shimmer long after you leave.",
    "10 of Diamonds": "Too much? Exactly.",
    "J of Diamonds": "He sells the dream with a wink and glitter on his shoes.",
    "Q of Diamonds": "She doesn’t follow trends — she *is* the trend.",
    "K of Diamonds": "Every spotlight bends toward him eventually."
}


# === FUNCTIONS ===

def extract_card_image(sheet_img, row, col):
    sheet_width, sheet_height = sheet_img.size
    card_width = sheet_width // 14
    card_height = sheet_height // 4

    box = (
        col * card_width,
        row * card_height,
        (col + 1) * card_width,
        (row + 1) * card_height
    )

    return sheet_img.crop(box)


def pick_random_card():
    row = random.randint(0, 3)
    col = random.randint(0, 13)

    # Joker handling (column 13)
    if col == 13:
        if row == 0:
            card_name = "Joker1"
        elif row == 1:
            card_name = "Joker2"
        else:
            return pick_random_card()  # skip blank tiles
    else:
        rank = RANKS[col]
        suit = SUITS[row]
        card_name = f"{rank} of {suit}"

    return row, col, card_name


def get_card_quote(card_name):
    return card_quotes.get(card_name, "The silence between shuffles hides forgotten truths.")


def show_card_popup(card_img, quote):
    root = tk.Tk()
    root.title("Your Daily Card")

    # Size and position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = (screen_width // 2) - (WINDOW_WIDTH // 2)
    y_pos = (screen_height // 2) - (WINDOW_HEIGHT // 2)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")
    root.configure(bg="#1a1a1a")  # dark gray instead of pure black

    # Resize card image to look cleaner
    card_img = card_img.resize((180, 270), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(card_img)

    # === IMAGE FRAME ===
    img_frame = tk.Frame(root, bg="#1a1a1a")
    img_frame.pack(pady=(15, 5))

    label_img = tk.Label(img_frame, image=photo, bg="#1a1a1a")
    label_img.image = photo
    label_img.pack()

    # === QUOTE FRAME ===
    text_frame = tk.Frame(root, bg="black")
    text_frame.pack(pady=(5, 15), padx=15, fill="x")

    label_text = tk.Label(
        text_frame,
        text=quote,
        wraplength=250,
        fg="white",
        bg="black",
        font=("Helvetica", 11, "italic"),
        justify="center",
        padx=10,
        pady=10
    )
    label_text.pack()

    # Exit button if you want one (optional)
    btn_close = tk.Button(root, text="Close", command=root.destroy, bg="#333", fg="white")
    btn_close.pack(pady=(0, 10))

    root.mainloop()



def main():
    try:
        sheet_img = Image.open(CARD_SHEET_PATH)
    except FileNotFoundError:
        print(f"[Error] File not found: {CARD_SHEET_PATH}")
        return

    row, col, card_name = pick_random_card()
    print(f"[INFO] Drawn: {card_name}")

    card_img = extract_card_image(sheet_img, row, col)
    quote = get_card_quote(card_name)

    print(f"[INFO] Quote: {quote}")
    show_card_popup(card_img, quote)


if __name__ == "__main__":
    main()

