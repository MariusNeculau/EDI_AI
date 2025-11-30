# 🐻 EDI AI - Eduard AI Therapeutic System

## Despre Proiect

**EDI AI** este un sistem terapeutic bazat pe inteligență artificială, conceput pentru a oferi exerciții ABA (Applied Behavior Analysis) pentru copii. Sistemul include un avatar animat - ursulețul **Aidy** - care ghidează copilul prin exerciții interactive.

### Caracteristici principale
- Avatar animat (ursulețul Aidy) cu expresii și animații
- Sinteză vocală în limba română
- Exerciții ABA structurate pe niveluri de dificultate
- Feedback pozitiv și încurajări audio
- Interfață prietenoasă pentru copii

---

## 📚 Exerciții Incluse

| Exercițiu | Descriere | Fișier |
|-----------|-----------|--------|
| **Give Me (Receptive)** | Copilul identifică și oferă obiectul cerut | `eduard_receptive.html` |
| **Give Me Simple** | Versiune simplificată pentru începători | `eduard_receptive_simple.html` |
| **Tell Me (Expressive)** | Copilul denumește obiectele afișate | `eduard_expressive.html` |
| **Learn Colors** | Învățarea și recunoașterea culorilor | `eduard_colors.html` |
| **Count Numbers** | Numărare și recunoașterea cifrelor | `eduard_numbers.html` |
| **Matching** | Potrivirea obiectelor similare | `eduard_matching.html` |
| **Pointing** | Exerciții de indicare | `eduard_pointing.html` |
| **Repeat After Me** | Repetarea cuvintelor/sunetelor | `eduard_repeat.html` |
| **Clap Your Hands** | Exercițiu cu detectare aplauze (microfon) | `clap_exercise.html` |

---

## 🚀 Cum se rulează

### Cerințe preliminare
- Python 3.8 sau mai nou
- Flask (`pip install flask`)
- Browser modern (Chrome, Firefox, Edge)

### Pași de instalare

1. **Clonează repository-ul:**
   ```bash
   git clone https://github.com/MariusNeculau/EDI_AI.git
   cd EDI_AI
   ```

2. **Instalează dependențele:**
   ```bash
   pip install flask
   ```

3. **Rulează serverul:**
   ```bash
   python eduard_web_server.py
   ```

4. **Deschide în browser:**
   ```
   http://localhost:5000
   ```

---

## 📁 Structura Proiectului

```
EDI_AI/
├── README.md                    # Documentația proiectului
├── LICENSE                      # Licența MIT
├── requirements.txt             # Dependențele Python
├── .gitignore                   # Fișiere ignorate de Git
│
├── eduard_web_server.py         # Serverul Flask principal
├── eduard_interface.html        # Interfața principală / meniu
├── dashboard.html               # Dashboard pentru progres
│
├── eduard_bear_avatar.html      # Componenta avatar Aidy
├── eduard_bear_clear.html       # Avatar versiune curată
│
├── eduard_receptive.html        # Exercițiu: Give Me
├── eduard_receptive_simple.html # Exercițiu: Give Me (simplu)
├── eduard_expressive.html       # Exercițiu: Tell Me
├── eduard_colors.html           # Exercițiu: Culori
├── eduard_numbers.html          # Exercițiu: Numere
├── eduard_matching.html         # Exercițiu: Potrivire
├── eduard_pointing.html         # Exercițiu: Pointing
├── eduard_repeat.html           # Exercițiu: Repetă
├── clap_exercise.html           # Exercițiu: Aplauze
│
├── audio/                       # Fișiere audio MP3
│   ├── welcome_*.mp3            # Mesaje de bun venit
│   ├── give_me_*.mp3            # Instrucțiuni "dă-mi"
│   ├── find_*.mp3               # Instrucțiuni "găsește"
│   ├── learn_*.mp3              # Învățare culori
│   ├── count_*.mp3              # Numărare
│   ├── correct.mp3              # Feedback corect
│   ├── try_again.mp3            # Încearcă din nou
│   └── ...                      # Alte fișiere audio
│
└── tracker.js                   # Sistem de tracking progres
```

---

## 🎨 Avatarul Aidy

Aidy este un ursuleț animat CSS care:
- Clipește și are expresii faciale
- Mișcă brațele pentru încurajări
- Oferă feedback vizual în timpul exercițiilor
- Folosește sinteză vocală (voce feminină, pitch 0.9, rate 0.7)

---

## 🛠️ Dezvoltare

### Tehnologii folosite
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Backend:** Python Flask
- **Audio:** Web Speech API + fișiere MP3 pre-generate
- **Avatar:** CSS animations

### Convenții de cod
- Fișierele HTML includ CSS și JS inline pentru portabilitate
- Numele fișierelor: `eduard_[exercițiu].html`
- Audio files: `[acțiune]_[obiect].mp3`

---

## 📄 Licență

Acest proiect este licențiat sub [MIT License](LICENSE).

---

## 👤 Autor

**Marius Neculau**  
Proiect dezvoltat ca parte din programul SDA AI Engineering.

---

## 🙏 Mulțumiri

Proiect dedicat lui Eduard (Aidy) ❤️
