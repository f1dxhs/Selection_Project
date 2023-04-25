from django.shortcuts import render
from .models import Item
from .forms import ItemSearchForm
from django.db.models import Q
def search_drive(request):
    if request.method == 'POST':
        try:
            
            Length = request.POST.get('length')
            Force = request.POST.get('T_Force')
            Dia = request.POST.get('Dia_dr')
            Torque = request.POST.get('T_Torque')

            print(Length, Force, Dia, Torque)
            results = Item.objects.filter(length=Length, Dia_dr = Dia, T_Force__gt=Force\
                                          ,T_Torque__gt= Torque)
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
    return render(request, 'search_drive.html')



from django.shortcuts import render
from .models import Item

def show_all_data(request):
    # 从数据库中获取所有数据
    all_data = Item.objects.all()
    # 将数据传递到模板中进行渲染
    return render(request, 'all_data.html', {'data': all_data})






# 工作流程: 多app方向 字典查阅 ---> 写出父类class ---> 