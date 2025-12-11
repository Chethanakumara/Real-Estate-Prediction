# 🏠 Real Estate Price Predictor

A **Django + Machine Learning web app** that predicts real estate prices using features like:

- 🏗️ Site Size (sq ft)
- 🏙️ City Range (km)
- 🚗 Road Distance (m)
<img width="1045" height="796" alt="Screenshot 2025-12-11 111103" src="https://github.com/user-attachments/assets/e25ef426-29ca-46f4-9586-c22e6ca75de9" />
  price prediction result
  <img width="1156" height="888" alt="Screenshot 2025-12-11 111021" src="https://github.com/user-attachments/assets/51fbba39-33e7-4b77-8735-5d46f4a56dc7" />

  <img width="981" height="746" alt="Screenshot 2025-12-11 111044" src="https://github.com/user-attachments/assets/de62ec3d-0d45-4b6b-89c2-fd6804b5643a" />


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
