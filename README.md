# 🏠 Real Estate Price Predictor

A **Django + Machine Learning web app** that predicts real estate prices using features like:

- 🏗️ Site Size (sq ft)
- <img width="1045" height="796" alt="Screenshot 2025-12-11 111103" src="https://github.com/user-attachments/assets/23b7c126-8396-4f0f-a9c5-7ca805693d9a" />

- 🏙️ City Range (km)
- 🚗 Road Distance (m)

---

## 🚀 Features
✅ Clean web interface using HTML + CSS  
✅ Machine Learning model built with scikit-learn  
✅ Containerized with Docker (easy deployment)  
✅ Ready for Railway, Render, or AWS

---

## 🧩 Project Setup (Local)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/chethankiruvaase/real-estate-app.git
cd real-estate-app

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run Django app
python manage.py runserver
