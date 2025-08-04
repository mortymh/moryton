02_logistic_regression

# Titanic Survival Prediction using Logistic Regression

---

## 📌 Project Overview

This project uses the Titanic dataset to build a binary classification model that predicts whether a passenger survived or not.  
We use Logistic Regression to demonstrate a foundational approach to classification in machine learning.  
The notebook includes data cleaning, preprocessing, model training, evaluation, and visualization.

---

## 🔧 Project Structure

- `logistic_regression_titanic.ipynb`  
  Complete workflow: load data, handle missing values, encode features, train and evaluate a Logistic Regression model.

- `requirements.txt`  
  List of Python packages required to run the notebook.

---

## 📊 Main Steps

1. Load Titanic dataset from Google Drive  
2. Fill missing values (e.g., age) using mean imputation  
3. Encode categorical variables (`Sex`, `Embarked`)  
4. Select relevant features for training  
5. Split dataset into training and test sets  
6. Train Logistic Regression model with `max_iter=200`  
7. Evaluate model performance (accuracy, precision, recall, f1-score)  
8. Display confusion matrix and visualize results

---

## 🎯 Results & Conclusions

- The model achieved **about 81% accuracy** on the test data.
- It performed better in predicting non-survivors (precision = 0.83, recall = 0.86).
- For survivors, performance was slightly lower (precision = 0.79, recall = 0.74).
- Although not perfect, the model gives a reliable baseline for classification tasks.
- Further improvements could include hyperparameter tuning or using more complex models (e.g., Random Forest, SVM).

---

## 📂 Dataset

This project uses the **Titanic dataset**, which is publicly available at:

- [Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)

---

##  معرفی پروژه (به فارسی)

---

## 📌 هدف پروژه

در این پروژه، از دیتاست Titanic برای ساخت یک مدل طبقه‌بندی دودویی استفاده شده که هدف آن پیش‌بینی وضعیت نجات‌یافتن مسافران است.  
برای این منظور از الگوریتم رگرسیون لجستیک استفاده شده که یکی از ساده‌ترین و پایه‌ای‌ترین مدل‌های طبقه‌بندی در یادگیری ماشین است.

---

## 🔧 ساختار پروژه

- `logistic_regression_titanic.ipynb`  
  نوت‌بوک شامل بارگذاری داده‌ها، پاک‌سازی، انکودینگ، آموزش مدل رگرسیون لجستیک و ارزیابی عملکرد آن.

- `requirements.txt`  
  شامل لیست کتابخانه‌های پایتون مورد نیاز برای اجرای پروژه.

---

## 📊 مراحل اصلی

1. بارگذاری دیتاست Titanic از گوگل درایو  
2. پر کردن مقادیر گمشده (مانند Age) با میانگین  
3. انکود متغیرهای متنی مانند `Sex` و `Embarked`  
4. انتخاب ویژگی‌های مهم برای آموزش  
5. تقسیم داده‌ها به آموزش و تست  
6. آموزش مدل رگرسیون لجستیک با `max_iter=200`  
7. ارزیابی دقت، precision، recall و f1-score  
8. رسم ماتریس درهم‌ریختگی و تحلیل نتایج

---

## 🎯 نتایج و نتیجه‌گیری

- مدل به دقت **حدود ۸۱٪** روی داده‌های تست دست یافت.
- عملکرد مدل در شناسایی افراد نجات‌نیافته بهتر بود (precision = 0.83، recall = 0.86).
- در پیش‌بینی افراد نجات‌یافته کمی افت دقت داشت (precision = 0.79، recall = 0.74).
- این مدل ساده می‌تواند نقطه شروع خوبی برای ساخت مدل‌های پیشرفته‌تر باشد.
- برای بهبود می‌توان از مدل‌های پیچیده‌تر یا تنظیم پارامترها استفاده کرد.

---

## 📂 دیتاست

از دیتاست Titanic استفاده شده که به‌صورت عمومی در دسترس است:

- [Kaggle - Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)

---

## ☎️ تماس | Contact

For any questions, suggestions, or collaboration, feel free to reach out:

برای پرسش، پیشنهاد یا همکاری، با من در تماس باشید:

- ✉️ Email: [mortymh@gmail.com](mailto:mortymh@gmail.com)  
- 💼 LinkedIn: [linkedin.com/in/morteza-m-6a62888a](https://www.linkedin.com/in/morteza-m-6a62888a)  
- 🐙 GitHub: [github.com/mortymh](https://github.com/mortymh)
