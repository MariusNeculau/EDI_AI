import os

print("=== LISTARE FISIERE AUDIO ===\n")

# Verifică dacă folderul audio există
if os.path.exists('audio'):
    files = os.listdir('audio')
    mp3_files = sorted([f for f in files if f.endswith('.mp3')])

    print(f"Total MP3 files: {len(mp3_files)}\n")
    print("Lista completa:\n")

    for i, f in enumerate(mp3_files, 1):
        print(f"{i}. {f}")
else:
    print("ERROR: Folderul 'audio' nu exista!")
    print("Cale curenta:", os.getcwd())