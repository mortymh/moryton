03_knn

# K-Nearest Neighbors (KNN) - Handwritten Digit Classification using MNIST

---

## 📌 Project Overview

This project demonstrates how to apply the K-Nearest Neighbors (KNN) algorithm to the MNIST dataset for digit classification.  
The MNIST dataset contains 70,000 grayscale images of handwritten digits (0–9), each with a resolution of 28x28 pixels.

Our main goal is to implement a simple yet effective machine learning model that can classify digits based on pixel values using KNN.

---

## 🔧 Project Structure

- `knn_digits_classification.ipynb`  
  Complete notebook including all steps: data loading, preprocessing, model training, evaluation, and visualization.

- `requirements.txt`  
  List of Python dependencies to run this notebook.

---

## 📊 Main Steps

1. Mount Google Drive and load MNIST data (`.npz`)
2. Visualize example digits
3. Normalize pixel values to [0, 1]
4. Split data into training and test sets
5. Train a KNN classifier with `k=3`
6. Evaluate model accuracy and visualize confusion matrix
7. Show predicted vs. true labels for random samples

---

## 🎯 Results & Conclusions

- The model achieved **over 96% accuracy** on the test set with just `k=3` neighbors.
- Although KNN is not the most efficient algorithm for large-scale data, it performed surprisingly well for this clean dataset.
- Misclassifications were often due to visually ambiguous digits (e.g. 4 vs. 9).
- This project showcases the power of simple algorithms and serves as a stepping stone toward more advanced classification techniques.

---

## 📂 Dataset

The dataset used is **MNIST**, available from:
- [Official Site](http://yann.lecun.com/exdb/mnist/)
- [Kaggle Version](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)

In this project, it is assumed that the dataset has already been downloaded as a `.npz` file and placed in Google Drive.

---

## 🇮🇷 معرفی پروژه (به فارسی)

---

## 📌 هدف پروژه

در این پروژه، طبقه‌بندی تصاویر ارقام دست‌نویس با استفاده از الگوریتم K-Nearest Neighbors (KNN) روی دیتاست معروف MNIST انجام شده است.  
این دیتاست شامل ۷۰,۰۰۰ تصویر سیاه و سفید از اعداد ۰ تا ۹ است که هر تصویر اندازه ۲۸x۲۸ پیکسل دارد.

هدف، پیاده‌سازی یک مدل ساده اما مؤثر جهت شناسایی ارقام دست‌نویس با استفاده از اطلاعات پیکسل‌ها و الگوریتم KNN است.

---

## 🔧 ساختار پروژه

- `knn_digits_classification.ipynb`  
  نوت‌بوک کامل شامل بارگذاری، پردازش داده، آموزش مدل، ارزیابی و نمایش نتایج.

- `requirements.txt`  
  لیست کتابخانه‌های مورد نیاز جهت اجرای نوت‌بوک.

---

## 📊 مراحل اصلی

1. اتصال گوگل درایو و بارگذاری فایل MNIST (`.npz`)
2. نمایش چند نمونه از تصاویر ورودی
3. نرمال‌سازی داده‌ها در بازه ۰ تا ۱
4. تقسیم داده به آموزش و تست
5. آموزش مدل KNN با تعداد ۳ همسایه
6. ارزیابی مدل با گزارش دقت و رسم ماتریس درهم‌ریختگی
7. نمایش نتایج پیش‌بینی شده در مقایسه با برچسب واقعی

---

## 🎯 نتایج و نتیجه‌گیری

- مدل KNN توانست دقتی بالای ۹۶٪ روی داده‌های تست کسب کند.
- با وجود سادگی، الگوریتم KNN در این دیتاست تمیز و ساختاریافته عملکرد بسیار خوبی داشت.
- اکثر اشتباهات مدل مربوط به اعداد با شباهت بصری زیاد (مثلاً ۴ و ۹) بود.
- این پروژه نشان می‌دهد که حتی الگوریتم‌های ساده نیز در برخی سناریوها بسیار مؤثر هستند و می‌توانند پایه‌ای برای روش‌های پیچیده‌تر باشند.

---

## 📂 دیتاست

دیتاست استفاده‌شده، **MNIST** است که از منابع زیر قابل دانلود می‌باشد:

- [لینک رسمی](http://yann.lecun.com/exdb/mnist/)
- [نسخه Kaggle](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)

در این پروژه، فرض بر این است که فایل `.npz` دیتاست قبلاً در گوگل درایو ذخیره شده است.

---

## ☎️ تماس | Contact

For any questions, suggestions, or collaboration, feel free to reach out:

برای پرسش، پیشنهاد یا همکاری، با من در تماس باشید:

- ✉️ Email: [mortymh@gmail.com](mailto:mortymh@gmail.com)  
- 💼 LinkedIn: [linkedin.com/in/morteza-m-6a62888a](https://www.linkedin.com/in/morteza-m-6a62888a)  
- 🐙 GitHub: [github.com/mortymh](https://github.com/mortymh)

