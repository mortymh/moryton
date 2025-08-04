# پروژه پیش‌بینی قیمت خانه در کالیفرنیا  
California House Price Prediction Project

---

## معرفی | Introduction

این پروژه شامل مراحل مختلفی برای پیش‌بینی قیمت خانه در کالیفرنیا است که از داده‌های خام شروع شده و به مدل‌سازی و بهبود مدل می‌رسد.  
This project covers multiple stages for predicting house prices in California, starting from raw data to modeling and model improvement.

---

## ساختار پروژه | Project Structure

- **01_data_exploration.ipynb**  
بررسی اولیه داده‌ها، بارگذاری و تحلیل مقدماتی.  
Initial data loading, exploration, and preliminary analysis.

- **02_preprocessing_and_split.ipynb**  
پیش‌پردازش داده‌ها، جایگزینی مقادیر گمشده، انکودینگ و تقسیم داده‌ها به مجموعه آموزش و تست.  
Data preprocessing, missing value imputation, encoding, and train-test split.

- **03_linear_regression.ipynb**  
آموزش مدل رگرسیون خطی و ارزیابی آن.  
Training and evaluating a linear regression model.

- **04_model_improvement.ipynb**  
بهبود مدل با استفاده از رگرسیون Ridge و Lasso.  
Improving the model with Ridge and Lasso regression.

---

## نتایج و تحلیل | Results and Analysis

- مدل رگرسیون خطی توانست حدود 61٪ از تغییرات قیمت خانه را توضیح دهد (R² = 0.61).  
- خطای میانگین قدر مطلق (MAE) حدود 51,846 دلار است.  
- مدل Ridge کمی بهتر عمل کرده اما تفاوت چشمگیری ندارد.  
- برای بهبود بیشتر، استفاده از مدل‌های پیچیده‌تر و ویژگی‌های جدید پیشنهاد می‌شود.  

The linear regression model explained about 61% of the variance in house prices (R² = 0.61).  
The mean absolute error (MAE) is around $51,846.  
Ridge regression performed slightly better but not significantly different.  
For further improvement, more complex models and new features are recommended.

---

## داده‌ها | Data

این پروژه از داده‌های مجموعه California Housing Dataset استفاده می‌کند.  
شما می‌توانید داده‌ها را به‌صورت رایگان از لینک زیر دانلود کنید:  

This project uses the California Housing Dataset.  
You can download the data for free from the following link:  

[California Housing Dataset](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)

---

## نحوه اجرا | How to Run

1. ابتدا محیط پایتون را آماده کنید.  
   پیشنهاد می‌شود از Google Colab یا محیط محلی با پایتون و کتابخانه‌های لازم استفاده کنید.  
   
2. نصب وابستگی‌ها:  
```
pip install -r requirements.txt
```


تماس | Contact
برای هرگونه سوال، پیشنهاد یا همکاری می‌توانید از طریق راه‌های زیر با من در تماس باشید:

For any questions, suggestions, or collaborations, feel free to contact me through:

ایمیل (Email): mortymh@example.com

لینکدین (LinkedIn): linkedin.com/in/mortymh

گیت‌هاب (GitHub): github.com/mortymh