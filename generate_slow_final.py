"""
SCRIPT SIMPLU - Generare audio SLOW cu gTTS
DOAR gTTS - FĂRĂ pydub!
"""

from gtts import gTTS
import os

audio_folder = "audio"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

phrases = {
    "welcome_give_me": "Hi Aidy! Let's play Give Me!",
    "welcome_tell_me": "Hi Aidy! Let's play Tell Me!",
    "welcome_colors": "Hi Aidy! Let's learn colors!",
    "welcome_numbers": "Hi Aidy! Let's count together!",
    "welcome_pointing": "Hi Aidy! Let's play Show Me!",
    "welcome_matching": "Hi Aidy! Let's match things!",

    "level1_intro": "Level 1: Let's start easy!",
    "level2_intro": "Level 2: Getting better!",
    "level3_intro": "Level 3: You're a star!",

    "correct": "Yes! Great job Aidy!",
    "excellent": "Excellent work Aidy!",
    "amazing": "Amazing Aidy!",
    "try_again": "Try again, you can do it!",
    "so_close": "So close! Try once more!",
    "level_complete": "Amazing! Level complete!",
    "game_complete": "Fantastic! You did it all!",

    "give_me_ball": "Give me the ball",
    "give_me_car": "Give me the car",
    "give_me_book": "Give me the book",
    "give_me_cup": "Give me the cup",
    "give_me_shoe": "Give me the shoe",
    "give_me_apple": "Give me the apple",
    "give_me_hat": "Give me the hat",
    "give_me_spoon": "Give me the spoon",

    "tell_me_what": "What is this Aidy?",
    "tell_me_name": "Can you name this?",
    "listen_carefully": "Listen carefully and repeat",
    "show_answer": "The answer is",

    "learn_red": "This is red",
    "learn_blue": "This is blue",
    "learn_green": "This is green",
    "learn_yellow": "This is yellow",
    "learn_orange": "This is orange",
    "learn_purple": "This is purple",
    "learn_pink": "This is pink",
    "learn_brown": "This is brown",
    "learn_black": "This is black",
    "learn_white": "This is white",

    "find_red": "Find the red color",
    "find_blue": "Find the blue color",
    "find_green": "Find the green color",
    "find_yellow": "Find the yellow color",
    "find_orange": "Find the orange color",
    "find_purple": "Find the purple color",
    "find_pink": "Find the pink color",
    "find_brown": "Find the brown color",

    "count_1": "One",
    "count_2": "Two",
    "count_3": "Three",
    "count_4": "Four",
    "count_5": "Five",
    "count_6": "Six",
    "count_7": "Seven",
    "count_8": "Eight",
    "count_9": "Nine",
    "count_10": "Ten",

    "how_many": "How many do you see?",
    "count_with_me": "Let's count together!",
    "count_objects": "Count the objects",

    "show_me_ball": "Show me the ball",
    "show_me_car": "Show me the car",
    "show_me_book": "Show me the book",
    "show_me_cup": "Show me the cup",
    "point_to": "Point to the",
    "where_is": "Where is the",

    "find_same": "Find the same one",
    "match_this": "Match this picture",
    "find_pair": "Find the matching pair",
    "good_matching": "Great matching Aidy!",

    "name_dog": "Dog",
    "name_cat": "Cat",
    "name_bird": "Bird",
    "name_fish": "Fish",
    "name_banana": "Banana",
    "name_orange": "Orange",
    "name_grapes": "Grapes",
    "name_star": "Star",
    "name_heart": "Heart",
    "name_circle": "Circle",
    "name_square": "Square",
    "name_triangle": "Triangle"
}

print("\n🎙️ GENERARE AUDIO - VOCE LENTĂ")
print("=" * 70)
print(f"🎯 Total: {len(phrases)} fraze")
print("🐢 Viteza: SLOW (slow=True)")
print("=" * 70)

success = 0

for filename, text in phrases.items():
    try:
        tts = gTTS(text=text, lang='en', slow=True)
        filepath = os.path.join(audio_folder, f"{filename}.mp3")
        tts.save(filepath)
        success += 1
        print(f"✅ {filename:30s} → \"{text}\"")
    except Exception as e:
        print(f"❌ {filename}: {e}")

print("=" * 70)
print(f"\n✨ GATA! {success} fișiere în '{audio_folder}/'")
print("🐢 Vocea ar trebui să fie MAI LENTĂ acum!")
print("=" * 70)

input("\n▶️ Apasă ENTER...")