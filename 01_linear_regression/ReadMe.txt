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
---

## نتیجه‌گیری و چالش‌ها | Conclusion and Challenges

در این پروژه، مدل رگرسیون خطی توانست حدود 61٪ از تغییرات قیمت خانه‌ها را پیش‌بینی کند که نتیجه قابل قبولی برای یک مدل ساده است.  
با این حال، چالش‌هایی مانند داده‌های گمشده و محدودیت در ویژگی‌های استفاده شده وجود داشت.  
برای بهبود دقیق‌تر، می‌توان از مدل‌های پیچیده‌تر، انتخاب ویژگی بهتر، و تنظیم پارامترهای مدل استفاده کرد.  
پروژه آینده می‌تواند شامل الگوریتم‌های پیشرفته‌تر مانند درخت تصمیم، شبکه‌های عصبی یا یادگیری عمیق باشد.

In this project, the linear regression model explained about 61% of the variance in house prices, which is a reasonable result for a simple model.  
However, challenges such as missing data and limited feature sets were present.  
For further improvements, more complex models, better feature selection, and hyperparameter tuning can be considered.  
Future work might include advanced algorithms like decision trees, neural networks, or deep learning.


---

## داده‌ها | Data

این پروژه از داده‌های مجموعه California Housing Dataset استفاده می‌کند.  
شما می‌توانید داده‌ها را به‌صورت رایگان از لینک‌های زیر دانلود کنید:  

- [لینک رسمی دانشگاه پرتغال (اصلی)](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)  
- [لینک Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices)  

This project uses the California Housing Dataset.  
You can download the data for free from the following links:  

- [Official University Link](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)  
- [Kaggle Link](https://www.kaggle.com/datasets/camnugent/california-housing-prices)  

---

## نحوه اجرا | How to Run

1. ابتدا محیط پایتون را آماده کنید.  
   پیشنهاد می‌شود از Google Colab یا محیط محلی با پایتون و کتابخانه‌های لازم استفاده کنید.  
   
2. نصب وابستگی‌ها:  
```
pip install -r requirements.txt
```


---

## تماس | Contact

برای هرگونه سوال، پیشنهاد یا همکاری می‌توانید از طریق راه‌های زیر با من در تماس باشید:

For any questions, suggestions, or collaborations, feel free to contact me through:

- ایمیل (Email): [mortymh@gmail.com](mailto:mortymh@gmail.com)  
- لینکدین (LinkedIn): [linkedin.com/in/morteza-m-6a62888a](https://www.linkedin.com/in/morteza-m-6a62888a)  
- گیت‌هاب (GitHub): [github.com/mortymh](https://github.com/mortymh)

