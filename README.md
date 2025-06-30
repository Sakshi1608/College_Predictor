# College_Predictor

*This was a beginner-level project built during my college days while learning Flask, HTML/CSS, and basic machine learning.*

*Helps you predict the college you might land in.* 
*It takes parameters such as Your rank, category, city etc. and predicts the best suitable college for you.*

## 📖 Overview

The **College Predictor** is a web application that estimates the best possible engineering college a student might land in, based on:
- 🎯 COMEDK Rank
- 🏷️ Category
- 🏙️ City
- 🧠 Preferred Branch

It uses a trained Random Forest classifier on real historical data and serves predictions through a simple web form.

## Tech-Stack
- Backend : Python Flask
- Frontend : HTML CSS
- ML Model: Random Forest

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
    git clone https://github.com/Sakshi1608/College_Predictor.git
    cd College_Predictor
```

### 2. Install requirements
```bash 
pip install flask pandas numpy scikit-learn
```
### 3. Train the Model
```bash
python model.py
```
This generates model.pkl using the provided dataset.

### 4. Run the Flask App
```bash
python app.py
```
Visit http://127.0.0.1:5000 in your browser to use the predictor.
    
