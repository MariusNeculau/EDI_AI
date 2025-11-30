from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__,
            static_folder='.',
            template_folder='.')


# === RUTĂ PENTRU AUDIO FILES ===
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    """Servește fișierele audio din folderul audio/"""
    audio_folder = os.path.join(os.path.dirname(__file__), 'audio')
    return send_from_directory(audio_folder, filename)


# === RUTĂ PENTRU HTML FILES ===
@app.route('/')
def home():
    return send_from_directory('.', 'eduard_interface.html')


@app.route('/<path:filename>')
def serve_file(filename):
    """Servește orice fișier HTML/CSS/JS din folderul curent"""
    return send_from_directory('.', filename)


# === RUTĂ PENTRU AI BACKEND (dacă ai nevoie) ===
@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint pentru chat cu AI (opțional)"""
    try:
        data = request.json
        user_message = data.get('message', '')

        # Aici poți adăuga logica AI cu Ollama
        # Pentru moment returnăm un răspuns simplu
        response = {
            'status': 'success',
            'message': 'AI response here'
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    print("=" * 50)
    print("🐻 AIDY AI SERVER - STARTING")
    print("=" * 50)
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🎵 Audio folder: {os.path.join(os.getcwd(), 'audio')}")
    print("🌐 Server running at: http://localhost:5000")
    print("=" * 50)

    # Verifică dacă folderul audio există
    audio_path = os.path.join(os.getcwd(), 'audio')
    if os.path.exists(audio_path):
        mp3_count = len([f for f in os.listdir(audio_path) if f.endswith('.mp3')])
        print(f"✅ Audio folder found: {mp3_count} MP3 files")
    else:
        print("⚠️  WARNING: Audio folder not found!")

    print("=" * 50)

    app.run(debug=True, host='0.0.0.0', port=5000)