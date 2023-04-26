from django.shortcuts import render
from .models import Table, Roller_TableData
from .forms import ItemSearchForm
from django.db.models import Q
def search_roller_35dt(request):
    if request.method == 'POST':
        try:
            
            Length = request.POST.get('length')
            Di = request.POST.get('Dia_dr')

            results = Item.objects.filter(length=Length, Dia_dr = Di)
            print(results)
        except ValueError:
            return render(request, 'error.html')
        
        if results.exists():
            mapcodes = [r.map_code for r in results]
            weights = [r.T_Weight for r in results]
            

            return render(request, 'results.html', {'weights': weights, 'mapcodes': mapcodes})
        else:
            # print(length)
            # print(T_Force)
            return render(request, 'no_results.html')
    return render(request, 'search_roller_35dt.html')


def search_roller(request):

    tables = Roller_TableData.objects.all()

    if request.method == 'POST':
        # 用户提交表格选择
        try:
            table_name = request.POST.get('tablename')  # 获取用户选择的表格标识符
            length_value = request.POST.get('length_value')  # 获取用户输入的 column_b 值
            Dia_value = request.POST.get('Dia_dr')  # 获取用户输入的 column_d 值  
        except ValueError:
            return render(request, 'error.html')
        # 根据用户选择的表格标识符从数据库中查询表格对象
        table = Roller_TableData.objects.get(id=table_name)

        # 根据用户输入的 column_b 和 column_d 值从数据库中查询对应的 TableData 对象
        table_data = Roller_TableData.objects.get(table=table, Belt_Width=length_value, Dia=Dia_value)
        if table_data.exists():
            # 获取 TableData 对象的 column_w 值，这是筛选结果
            weight_value = table_data.T_Weight
            mapcode = table_data.mapcode_2
            return render(request, 'result.html', {'weights': weight_value, 'mapcodes': mapcode})
        else:
            return render(request, 'no_results.html')
    return render(request, 'search_roller_35dt.html')
