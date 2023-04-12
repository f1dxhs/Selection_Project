from django.shortcuts import render
from .models import Item
from .forms import ItemSearchForm

def search(request):
    if request.method == 'POST':
        try:
            length = request.POST.get('length')
            T_Force = request.POST.get('T_Force')
            Dia_dr = request.POST.get('T_Force')
            T_Torque = request.POST.get('T_Torque')
            results = Item.objects.filter(length=length, T_Force__gt=T_Force, Dia_dr = Dia_dr, T_Torque__gt= T_Torque).first()
        except ValueError:
            return render(request, 'error.html')
        
        if results.exists():
            weights = [r.T_weight for r in results]
            mapcodes = [r.map_code for r in results]

            return render(request, 'results.html', {'weights': weights, 'mapcodes': mapcodes})
        else:
            print(length)
            print(T_Force)
            return render(request, 'no_results.html')
    return render(request, 'search.html')


# filtered_data = Item.objects.filter(
# Q(length=length) & Q(dia_dr=dia_dr) & Q(T_Force__gte=t_force) & Q(T_Torque__gte=t_torque)
#         ).order_by('-T_Force','-T_Torque','-weight')[:1]


# from django.http import JsonResponse
# import mysql.connector

# def filter_data(request):
#     # 从 GET 请求参数中获取筛选参数
#     length = request.GET.get('length', None)
#     t_force = request.GET.get('t_force', None)

#     # 连接到本地 MySQL 数据库
#     cnx = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='roller_selection_test'
#     )

#     # 创建一个查询游标
#     cursor = cnx.cursor()

#     # 构造查询语句
#     query = "SELECT t_weight, map_code FROM a WHERE length=%s AND T_Force=%s"
#     params = (length, t_force)

#     # 执行查询语句
#     cursor.execute(query, params)

#     # 获取查询结果
#     results = cursor.fetchall()

#     # 关闭游标和连接
#     cursor.close()
#     cnx.close()

#     # 将查询结果以 JSON 格式返回给 Web 客户端
#     data = [{'t_weight': row[0], 'map_code': row[1]} for row in results]
#     return JsonResponse({'data': data})
 



from django.shortcuts import render
from .models import Item

def show_all_data(request):
    # 从数据库中获取所有数据
    all_data = Item.objects.all()
    # 将数据传递到模板中进行渲染
    return render(request, 'all_data.html', {'data': all_data})
