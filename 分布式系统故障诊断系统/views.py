import os,django

from django.http import HttpResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '分布式系统故障诊断系统.settings')
django.setup()
from django.shortcuts import render,redirect
from upload_app.models import Content
from django.conf import settings
import pandas as pd
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'ws.html')
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        dataframes = []
        similar_format = True

        for file in files:
            # 读取文件内容为DataFrame对象
            df = pd.read_csv(file)
            dataframes.append(df)

        # 检查文件内容格式是否相似
        first_df = dataframes[0]
        for df in dataframes[1:]:
            if not first_df.equals(df):
                similar_format = False
                break

        if similar_format and len(files) > 1:
            # 合并所有DataFrame对象
            merged_df = pd.concat(dataframes)

            # 生成合并后的文件名
            merged_file_name = files[0].name
            merged_file_path = os.path.join(settings.MEDIA_ROOT, 'data', merged_file_name)

            # 保存合并后的DataFrame为CSV文件
            merged_df.to_csv(merged_file_path, index=False)

            # 创建Content对象保存合并后的文件
            Content.objects.create(title=merged_file_name, data=merged_file_path)
            return HttpResponse('文件上传成功', content_type='text/plain', status=200)
        else:
            # 如果只上传了一个文件或文件格式不相似，继续处理单个文件
            for file in files:
                Content.objects.create(title=file.name, data=file)

            return render(request, '文件检验界面.html')

def my_view(request):
    # 执行某些逻辑...
    # 重定向到另一个URL
    return redirect("/test_upload")

def xd(request):
    return render(request,'index.html')

def jj(request):
    return render(request,'加载线条.html')

def my_view_01(request):
    # 执行某些逻辑...
    # 重定向到另一个URL
    return redirect("/jj")
def my_view_02(request):
    # 执行某些逻辑...
    # 重定向到另一个URL
    return redirect("/upload_app/model")
def my_view_03(request):
    # 执行某些逻辑...
    # 重定向到另一个URL
    return redirect("/guzhang")

def my_view_04(request):
    # 执行某些逻辑...
    # 重定向到另一个URL
    return redirect("/test_load")

def gz(request):

    return render(request,'故障.html')
def yx(request):
    return render(request,'预测线条.html')
#多表
def re(requset):
    return redirect('/yx')
def my_view_05(request):

    return redirect("/test_load")
def db(request):

    return render(request,'文件检验界面.html')



def peie(request):

    return render(request,'配额.html')


def gr(request):

    return render(request,'个人.html')
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        # 保存文件到 media 目录
        file_path = os.path.join(settings.MEDIA_ROOT,)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return render(request, '多文件上传2.html')  # 返回前端页面
    else:
        return render(request, '多文件上传2.html')

def xz(request):

    return render(request,"模型下载弹窗.html")
def redic(request):

    return redirect("/login")

def qipao2(request):

    return render(request,"qipao2.html")

def houtai(request):

    return render(request,"table.html")
def fff(request):

    return render(request,"训练多表.html")

def ks(request):

    return render(request,"ks.html")
def rr(request):
    return redirect('/upload_app/model')
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
import os

def bg(request):
    # 获取最新上传的CSV文件路径
    data_dir = os.path.join(settings.MEDIA_ROOT, 'data')
    csv_files = [f for f in default_storage.listdir(data_dir)[1] if f.endswith('.csv')]
    if csv_files:
        csv_files.sort(key=lambda x: os.path.getmtime(os.path.join(data_dir, x)), reverse=True)
        csv_file_path = default_storage.url(os.path.join('data', csv_files[0]))
    else:
        csv_file_path = ''
    return render(request, '文件检验界面.html', {'csv_file_path': csv_file_path})




if __name__ == '__main__':
    print(settings.MEDIA_ROOT)
    print(settings.MEDIA_URL)


