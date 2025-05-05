from django.shortcuts  import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'USA_Housing.csv')
data = pd.read_csv(csv_path)



# آموزش مدل فقط یک بار در ابتدای اجرای برنامه
data = data.drop(['Address'], axis=1)
x = data.drop(['Price'], axis=1)
y = data['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
model = LinearRegression()
model.fit(x_train, y_train)



def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')

def index(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team.html')

def about(request):
    return render(request, 'about.html')



def result(request):

    try:
        var1 = float(request.GET['n1'])
        var2 = float(request.GET['n2'])
        var3 = float(request.GET['n3'])
        var4 = float(request.GET['n4'])
        var5 = float(request.GET['n5'])
    except (ValueError, KeyError):
        return render(request, 'predict.html', {"result": "Please fill all fields correctly."})



    pred = model.predict(np.array([[var1, var2, var3, var4, var5]]))
    pred = round(pred[0])

    price = "the predicted price is $" + str(pred)

    # predictions = model.predict(x_test)
    return render(request, 'predict.html', {"result":price})

# def result(request):
#         try:
#             # دریافت مقادیر و بررسی اولیه
#             inputs = []
#             for i in range(1, 6):
#                 var = request.GET(f'n{i}', '').strip()
#                 if not var or not is_number(var):
#                     raise ValueError("Invalid input")
#                 inputs.append(float(var))
#
#             # پیش‌بینی
#             pred = model.predict(np.array([[inputs]]))
#             pred = round(pred[0])
#             price = "قیمت پیش‌بینی‌شده: $" + str(pred)
#
#             return render(request, 'predict.html', {"result": price})
#
#         except:
#             return render(request, 'predict.html', {"result": "لطفاً همه فیلدها را با عدد صحیح پر کنید."})
#
#     # تابع کمکی برای چک کردن عدد بودن
#     def is_number(s):
#         try:
#             float(s)
#             return True
#         except ValueError:
#             return False
