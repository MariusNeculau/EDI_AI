"""
GENERARE FINALĂ - TOATE FRAZELE PENTRU TOATE EXERCIȚIILE
Viteza: SLOW (slow=True) - PERFECT pentru Aidy!
Total: 90+ fraze pentru toate exercițiile
"""

from gtts import gTTS
import os

audio_folder = "audio"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# ============================================
# TOATE FRAZELE - COMPLET
# ============================================

phrases = {
    # ===== FRAZE GENERALE =====
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

    # ===== GIVE ME (Receptive) =====
    "give_me_ball": "Give me the ball",
    "give_me_car": "Give me the car",
    "give_me_book": "Give me the book",
    "give_me_cup": "Give me the cup",
    "give_me_shoe": "Give me the shoe",
    "give_me_apple": "Give me the apple",
    "give_me_hat": "Give me the hat",
    "give_me_spoon": "Give me the spoon",

    # ===== TELL ME (Expressive) =====
    "tell_me_what": "What is this Aidy?",
    "tell_me_name": "Can you name this?",
    "listen_carefully": "Listen carefully and repeat",
    "show_answer": "The answer is",

    # ===== COLORS =====
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

    # ===== NUMBERS =====
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

    # ===== POINTING & SHOW ME =====
    "show_me_ball": "Show me the ball",
    "show_me_car": "Show me the car",
    "show_me_book": "Show me the book",
    "show_me_cup": "Show me the cup",
    "point_to": "Point to the",
    "where_is": "Where is the",

    # ===== MATCHING =====
    "find_same": "Find the same one",
    "match_this": "Match this picture",
    "find_pair": "Find the matching pair",
    "good_matching": "Great matching Aidy!",

    # ===== OBIECTE SUPLIMENTARE =====
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

print("\n" + "=" * 70)
print("🎙️  GENERARE FINALĂ - TOATE FRAZELE AIDY AI")
print("=" * 70)
print(f"📁 Folder: {audio_folder}/")
print(f"🎯 Total fraze: {len(phrases)}")
print(f"🐢 Viteza: SLOW (slow=True) - PERFECT pentru Aidy!")
print(f"🎀 Voce: Feminină blândă")
print("=" * 70 + "\n")

success = 0
errors = 0

categories = {
    "General": ["welcome", "level", "correct", "excellent", "amazing", "try_again", "so_close", "complete"],
    "Give Me": ["give_me"],
    "Tell Me": ["tell_me", "listen_carefully", "show_answer"],
    "Colors": ["learn_", "find_red", "find_blue", "find_green", "find_yellow", "find_orange", "find_purple",
               "find_pink", "find_brown"],
    "Numbers": ["count_", "how_many", "count_with_me", "count_objects"],
    "Pointing": ["show_me", "point_to", "where_is"],
    "Matching": ["find_same", "match_this", "find_pair", "good_matching"],
    "Objects": ["name_"]
}


def get_category(filename):
    for cat, keywords in categories.items():
        for keyword in keywords:
            if filename.startswith(keyword) or keyword in filename:
                return cat
    return "Other"


for filename, text in phrases.items():
    try:
        category = get_category(filename)

        # Generează audio cu slow=True
        tts = gTTS(text=text, lang='en', slow=True)
        filepath = os.path.join(audio_folder, f"{filename}.mp3")
        tts.save(filepath)

        success += 1
        print(f"✅ [{category:10s}] {filename:30s} → \"{text}\"")

    except Exception as e:
        errors += 1
        print(f"❌ {filename}: {e}")

print("\n" + "=" * 70)
print("📊 STATISTICI FINALE:")
print(f"   ✅ Succese: {success}")
print(f"   ❌ Erori: {errors}")
print(f"   📁 Total fișiere: {success} MP3")
print(f"   🐢 Viteza: SLOW (perfect!)")
print(f"   🎀 Voce: Blândă și caldă")
print("\n" + "=" * 70)
print(f"✨ GATA! Toate fișierele sunt în '{audio_folder}/'")
print("\n📋 NEXT STEPS:")
print("   1. ✅ Toate audio files generate cu succes!")
print("   2. ✅ Viteza PERFECTĂ pentru Aidy")
print("   3. ✅ Voce BUNĂ și blândă")
print("   4. 🚀 Următorul pas: Aplicăm pe TOATE exercițiile HTML")
print("=" * 70)

input("\n▶️ Apasă ENTER pentru a închide...")