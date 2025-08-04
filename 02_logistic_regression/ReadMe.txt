
Titanic Survival Prediction with Logistic Regression
پروژه پیش‌بینی نجات‌یافتگان کشتی تایتانیک با مدل رگرسیون لجستیک
Project Description
توضیح پروژه
The goal of this project is to provide a practical, step-by-step introduction to machine learning models using the Titanic dataset.
This exercise uses a Logistic Regression model and covers data preprocessing, model training, and evaluation.

هدف این پروژه آموزش عملی و گام به گام مدل‌های یادگیری ماشین با استفاده از داده‌های Titanic است.
این تمرین با استفاده از مدل رگرسیون لجستیک انجام شده و مراحل پیش‌پردازش داده‌ها، آموزش مدل و ارزیابی آن را شامل می‌شود.

Main Steps of the Project
مراحل اصلی پروژه
Data Loading
The Titanic dataset CSV file is loaded from Google Drive so you don't need to download it every time you run the code.

بارگذاری داده‌ها
داده‌های Titanic به صورت CSV از گوگل درایو خوانده می‌شود تا در هر بار اجرای کد نیازی به دانلود مجدد نباشد.

Data Cleaning
Missing values in the Age column are filled with the column’s mean using SimpleImputer.

پاک‌سازی داده‌ها
پر کردن مقادیر گمشده ستون Age با میانگین آن ستون با استفاده از SimpleImputer انجام شده است.

Model Building
A Logistic Regression model is created with max_iter=200 to allow up to 200 iterations for optimization.

ساخت مدل
مدل رگرسیون لجستیک با تنظیم max_iter=200 ساخته شده تا الگوریتم تا ۲۰۰ بار تلاش کند ضرایب را بهینه کند.

Model Training
The model is trained on the training data (X_train and y_train).

آموزش مدل
مدل با داده‌های آموزش (X_train و y_train) آموزش داده می‌شود.

Model Evaluation
The model is evaluated on the test data, calculating precision, recall, f1-score, and accuracy.
The confusion matrix is also displayed.

ارزیابی مدل
مدل روی داده تست ارزیابی شده و معیارهای precision، recall، f1-score و accuracy محاسبه شده‌اند.
ماتریس درهم‌ریختگی نیز نمایش داده شده است.

Results
نتایج
The overall accuracy of the model is 81%.

The model performs better in identifying non-survivors (precision=0.83, recall=0.86).

For survivors, the precision and recall are slightly lower (precision=0.79, recall=0.74).

Some errors remain, but the model shows acceptable performance.

دقت کلی مدل (accuracy) برابر با 81٪ است.

مدل در تشخیص افراد نجات نیافته عملکرد بهتری دارد (precision=0.83، recall=0.86).

برای افراد نجات‌یافته، دقت کمی کمتر است (precision=0.79، recall=0.74).

تعداد خطاها در تشخیص وجود دارد اما مدل عملکرد قابل قبولی دارد.