"""
MASTER SCRIPT - Generare audio files pentru TOATE exercițiile Aidy AI
Folosește gTTS (Google Text-to-Speech) - 100% gratuit

INSTRUCȚIUNI:
1. Salvează acest fișier ca: generate_audio_files.py
2. În PyCharm: Right-click → Run 'generate_audio_files'
3. SAU în CMD: python generate_audio_files.py
"""

from gtts import gTTS
import os

# Creează folder pentru audio files
audio_folder = "audio"
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)
    print(f"✅ Folder '{audio_folder}' creat\n")

# ============================================
# DICȚIONAR COMPLET - TOATE EXERCIȚIILE
# ============================================

phrases = {
    # ===== FRAZE GENERALE (folosite în mai multe exerciții) =====
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

print("\n🎙️ GENERARE AUDIO FILES - TOATE EXERCIȚIILE AIDY AI")
print("=" * 70)
print(f"📁 Folder output: '{audio_folder}/'")
print(f"🎯 Total fraze: {len(phrases)}")
print("=" * 70)

# Contoare pentru statistici
success_count = 0
error_count = 0
categories = {
    "General": 0,
    "Give Me": 0,
    "Tell Me": 0,
    "Colors": 0,
    "Numbers": 0,
    "Pointing": 0,
    "Matching": 0,
    "Objects": 0
}

# Generează fiecare fișier audio
for filename, text in phrases.items():
    try:
        # Identifică categoria
        if filename.startswith("welcome") or filename.startswith("level") or filename in ["correct", "excellent",
                                                                                          "amazing", "try_again",
                                                                                          "so_close", "level_complete",
                                                                                          "game_complete"]:
            category = "General"
        elif filename.startswith("give_me"):
            category = "Give Me"
        elif filename.startswith("tell_me") or filename in ["listen_carefully", "show_answer"]:
            category = "Tell Me"
        elif filename.startswith("learn_") or filename.startswith("find_"):
            category = "Colors"
        elif filename.startswith("count_") or filename in ["how_many", "count_with_me", "count_objects"]:
            category = "Numbers"
        elif filename.startswith("show_me") or filename in ["point_to", "where_is"]:
            category = "Pointing"
        elif "match" in filename or "find_same" in filename or "find_pair" in filename:
            category = "Matching"
        elif filename.startswith("name_"):
            category = "Objects"
        else:
            category = "General"

        # Creează obiect gTTS cu voce feminină
        tts = gTTS(text=text, lang='en', slow=False)

        # Salvează ca MP3
        filepath = os.path.join(audio_folder, f"{filename}.mp3")
        tts.save(filepath)

        # Update contoare
        success_count += 1
        categories[category] += 1

        print(f"✅ [{category:10s}] {filename:25s} → \"{text}\"")

    except Exception as e:
        error_count += 1
        print(f"❌ EROARE la {filename}: {e}")

# STATISTICI FINALE
print("=" * 70)
print("\n📊 STATISTICI GENERARE:")
print(f"   ✅ Succese: {success_count}")
print(f"   ❌ Erori: {error_count}")
print(f"   📁 Total fișiere: {success_count} MP3\n")

print("📋 BREAKDOWN PE CATEGORII:")
for cat, count in categories.items():
    if count > 0:
        print(f"   {cat:15s}: {count} fișiere")

print("\n" + "=" * 70)
print(f"✨ GATA! Toate fișierele audio sunt în '{audio_folder}/'")
print("\n📋 NEXT STEPS:")
print("   1. ✅ Verifică calitatea audio în folder")
print("   2. ✅ Testează un exercițiu cu audio")
print("   3. ✅ Dacă vocea e OK → aplicăm pe toate exercițiile")
print("   4. ⏳ Dacă vocea NU e OK → ajustăm pitch-ul")
print("=" * 70)

# Ține fereastra deschisă pentru a citi output-ul
input("\n\n▶️ Apasă ENTER pentru a închide...")