from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle
# Create your views here.
def set_cookies(request):
    resp=HttpResponse('set cookies is ok')
    resp.set_cookie('uuname','gxn',500)
    return resp
def get_cookies(request):

    value=request.COOKIES.get('uuname')

    return HttpResponse('value is %s'%(value))

def set_session(request):
    request.session['uname']='wwc'
    return HttpResponse('set session is OK')

def get_session(request):
    value=request.session['uname']
    return HttpResponse('session value is %s'%(value))


def model(request):
    # 获取media文件夹路径
    media_path = settings.MEDIA_ROOT
    column_name = ["Sample code number",
                   "Clump Thickness",
                   "Uniformity of Cell Size",
                   "Uniformity of Cell Shape",
                   "Marginal Adhesion",
                   "Single Epithelial Cell Size",
                   "Bare Nuclei",
                   "Bland Chromatin",
                   "Normal Nucleoli",
                   "Mitoses",
                   "Class"]
    # 加载数据集
    data = pd.read_csv('F:/django项目/media/data/数据.csv',names=column_name)

    # 缺失值处理
    data = data.replace(to_replace="?", value=np.nan)

    # 删除缺失值样本
    data.dropna(inplace=True)

    x = data.iloc[:, 1:-1]
    y = data["Class"]
    x_train, x_test, y_train, y_test = train_test_split(x, y,random_state=22)

    # 标准化
    transfer = StandardScaler()
    x_trian = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 建立模型

    estimator = LogisticRegression()
    estimator.fit(x_trian, y_train)

    # 回归系数
    print(estimator.coef_)

    y_predict = estimator.predict(x_test)
    print(y_predict == y_test)

    # 准确率
    score = estimator.score(x_test, y_test)
    context = {'score': score}
    pkl_filename = "model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(estimator, file)
    with open(pkl_filename, 'rb') as f:
        response = HttpResponse(f.read(),content_type='application/octet-stream')
    response['Content-Disposition'] = f'inline; filename="model.pkl"'
    return response


if __name__ == '__main__':
    column_name = ["Sample code number",
                   "Clump Thickness",
                   "Uniformity of Cell Size",
                   "Uniformity of Cell Shape",
                   "Marginal Adhesion",
                   "Single Epithelial Cell Size",
                   "Bare Nuclei",
                   "Bland Chromatin",
                   "Normal Nucleoli",
                   "Mitoses",
                   "Class"]
    # 加载数据集
    data = pd.read_csv('F:/django项目/media/data/数据.csv', names=column_name)
    # 缺失值处理
    data = data.replace(to_replace="?", value=np.nan)
    # 删除缺失值样本
    data.dropna(inplace=True)
    # print(data.isnull().any())

    x = data.iloc[:, 1:-1]
    y = data["Class"]
    x_train, x_test, y_train, y_test = train_test_split(x, y,random_state=22)

    # 标准化
    transfer = StandardScaler()
    x_trian = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 建立模型

    estimator = LogisticRegression()
    estimator.fit(x_trian, y_train)

    # 回归系数
    print(estimator.coef_)

    y_predict = estimator.predict(x_test)
    print(y_predict == y_test)

    # 准确率
    score = estimator.score(x_test, y_test)
    print(score)






