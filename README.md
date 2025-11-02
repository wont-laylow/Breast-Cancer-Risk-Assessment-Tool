# 🇬🇭 Breast Cancer Risk Prediction API

A **ml web app** that predicts breast cancer risk based on demographic, reproductive, and lifestyle factors.  

---

## Research Background

This project is inspired by the study  
> **“A Population-Based Study of Breast Cancer in Ghana: Methods and Study Descriptive Characteristics”**  
>  https://pmc.ncbi.nlm.nih.gov/articles/PMC5926189/
The research analyzed **over 4,000 women** in Accra and Kumasi to identify key risk factors such as education level, family history, parity, menarche/menopause age, and body size.  
The patterns discovered were used to train a machine learning model that predicts breast cancer likelihood.
---

This project will be **expanded in the future** by integrating data and insights from **additional epidemiological studies** across Africa and beyond, to improve accuracy and generalizability.
---

## ⚙️ Features

- **Inputs:** Age, Education, Family History, Parity, Menarche Age, Menopause Age, Body Size  
- **Outputs:**  
  - `prediction`: 1 = High risk, 0 = Low risk  
  - `positivity_score` and `negativity_score` (probabilities)  
  - `interpretation`: “High risk” or “Low risk”

---

## 🧠 Example Output

```json
{
  "prediction": 0,
  "positivity_score": 17.26,
  "negativity_score": 82.74,
  "interpretation": "Low risk"
}



