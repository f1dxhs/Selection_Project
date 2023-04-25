from django.shortcuts import render
from django.shortcuts import redirect

def choose_app(request):
    # 处理用户选择 app 的逻辑
    if request.method == 'POST':
        app = request.POST.get('app')  # 获取用户选择的 app
        if app == 'app':
            return redirect('/drive/')  # 重定向到 drive_app 的 URL
        elif app == 'alter_pulley':
            return redirect('/alter/')  # 重定向到 alter_app 的 URL
        elif app == 'roller':
            return redirect('/roller')
    return render(request, 'userpage.html')  # 渲染选择 app 的页面

