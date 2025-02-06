# 🐣 Tamagotchi – Wirtualny Zwierzak na Androida  

## 📌 O Projekcie  
Tamagotchi to **prosta gra wirtualnego zwierzaka**, inspirowana klasycznymi cyfrowymi pupilami z lat 90.! 🕹️  
Twoim zadaniem jest **opieka nad małym stworzeniem**, karmienie go, zabawa, dbanie o jego zdrowie i obserwowanie, jak rośnie.  

Gra jest napisana w **Pythonie** i działa na **Androidzie** w emulatorze terminala. Wykorzystuje **wątki** do symulacji realnego upływu czasu.  

## 🎮 Funkcje  
✅ **Wybór jajka** – Wybierz jedno z czterech unikalnych jajek! 🥚  
✅ **System wzrostu** – Twój pupil ewoluuje z wiekiem! 🌱  
✅ **Zarządzanie statystykami** – Głód, energia, szczęście i zdrowie wymagają Twojej uwagi! ❤️  
✅ **Zabawy i interakcje** – Karm, baw się, pozwól odpocząć, lecz, a nawet... pomagaj w potrzebach fizjologicznych! 🚽  
✅ **System punktów** – Zdobywaj punkty i wydawaj je w sklepie! 🛍️  
✅ **Sztuka ASCII** – Proste grafiki ASCII dodają uroku grze! 🎨  
✅ **Działa na Termuxie** – Uruchomisz ją na **Androidzie**! 📱  

---

## 📥 Instalacja  

### 1️⃣ Instalacja Pythona na Androidzie  
Do uruchomienia gry na **Androidzie** potrzebujesz aplikacji **Termux** (terminal).  
📌 **Pobierz Termux**: [Google Play](https://play.google.com/store/apps/details?id=com.termux) | [F-Droid](https://f-droid.org/packages/com.termux/)  

Następnie zainstaluj **Pythona** w Termuxie:  
```bash
pkg update && pkg upgrade
pkg install python
```

### 2️⃣ Pobranie gry Tamagotchi  
Pobierz kod z **GitHuba** (lub pobierz ręcznie pliki):  
```bash
pkg install git
git clone https://github.com/qbaa134/Tamagotchi.git
cd Tamagotchi
```

### 3️⃣ Uruchomienie gry  
Aby rozpocząć zabawę, wpisz:  
```bash
python main.py
```

🎉 **Miłej zabawy!** 🎉  

---

## 📖 Jak Grać?  

1️⃣ **Wybierz Jajko** 🥚  
   - Na start wybierz jedno z czterech jajek!  

2️⃣ **Nazwij swojego Tamagotchi** ✏️  
   - Nadaj swojemu pupilowi imię!  

3️⃣ **Monitoruj jego stan** 📊  
   - Sprawdzaj **głód**, **energię**, **szczęście** i **zdrowie**.  

4️⃣ **Opiekuj się nim** 🎭  
   - **Karm** 🥕🍩  
   - **Baw się** 🎾🧩  
   - **Pozwól mu spać** 😴  
   - **Lecz go w razie choroby** 🏥🌿  
   - **Pomóż w potrzebach fizjologicznych** 🚽  

5️⃣ **Zdobywaj punkty i kupuj przedmioty** 🛒  
   - Zarabiaj **punkty** i **wydawaj je w sklepie**!  

6️⃣ **Obserwuj, jak rośnie!** 🌟  
   - Twój pupil będzie się **zmieniał**! Ale jeśli o niego nie zadbasz, może **umrzeć**! 💀  

---

## 🛠️ Mechanika Gry  

| Statystyka       | Wpływ na rozgrywkę |
|----------------|------------------|
| **Głód** 🍗 | Karmienie zapobiega śmierci z głodu. |
| **Energia** ⚡ | Sen odnawia energię; jej brak prowadzi do osłabienia. |
| **Szczęście** 😃 | Gry i zabawa zwiększają szczęście. |
| **Zdrowie** ❤️ | Jeśli spadnie do 0, zwierzak umiera. Można je odnawiać. |
| **Punkty** 🎖️ | Zdobywane za interakcje, wykorzystywane w sklepie. |
| **Wiek** 📅 | Określa etap rozwoju Tamagotchi. |

---

## 🏪 Sklep  

🔹 **Zabawka (10 pkt)** – Zwiększa szczęście. 🎾  
🔹 **Nowe jedzenie (15 pkt)** – Lepsze opcje karmienia. 🍎  
🔹 **Eliksir zdrowia (20 pkt)** – Natychmiast przywraca zdrowie. 🧪  

---

## 🖥️ Przykładowa Rozgrywka  

```
🐣 Wybierz swoje jajko!
1️⃣
     _______
    /       \
   /  O O   \
  |         |
   \_______/

Podaj numer wybranego jajka (1-4): 1

✏️ Jak nazwiesz swojego Tamagotchi? **Fluffy**
🎉 Przygarniasz Fluffy!

📊 --- Status ---
Imię: Fluffy
Głód: 100
Energia: 100
Szczęście: 100
Zdrowie: 100
Wiek: 0
Punkty: 0
-----------------

🎭 Wybierz akcję:
1. Nakarm 🍏
2. Pobaw się 🎾
3. Połóż spać 💤
4. Wylecz 🏥
5. Toaleta 🚽
6. Sklep 🛍️
7. Nic nie rób ⏳

Podaj numer akcji (1-7): **1**
🍎 Wybierz jedzenie: 1. Owoce 2. Warzywa 3. Słodycze
Podaj wybór: **2**
✅ Nakarmiłeś swojego Tamagotchi warzywami. Głód wzrósł!
```

---

## 🏆 Porady i Triki  

🔥 **Utrzymuj balans statystyk** – Nie pozwól, aby głód, szczęście lub zdrowie spadły do 0!  
💡 **Baw się z pupilem** – Zwiększa szczęście i daje dodatkowe punkty!  
💤 **Nie zapominaj o śnie** – Energia szybko się kończy!  
🛒 **Oszczędzaj punkty** – Eliksir zdrowia może uratować życie!  

---

## 🤖 Planowane Ulepszenia  

🚀 **Więcej mini-gier** – Jeszcze więcej zabawy!  
🎨 **Personalizacja zwierzaka** – Zmieniaj kolory i twarze!  
📱 **Wersja z interfejsem graficznym** – Pełnoprawna aplikacja na Androida!  
🌎 **Tryb multiplayer** – Możliwość interakcji z innymi graczami!  

---

## 🔗 Współtworzenie  

Chcesz **ulepszyć grę**? 🛠️ Możesz forknąć repozytorium i dodać swoje pomysły!  
📌 GitHub: [Tamagotchi-Android](https://github.com/qbaa134/Tamagotchi)  

---

## 📜 Licencja  

📜 MIT License – Możesz używać, modyfikować i udostępniać projekt!  

---

## 💬 Kontakt  

📧 **Autor:** [qbaa134](https://github.com/qbaa134)  
📢 Masz pomysł lub znalazłeś błąd? Zgłoś **issue** na GitHubie!  

🐣 **Miłej zabawy z Tamagotchi!** 🐣  
