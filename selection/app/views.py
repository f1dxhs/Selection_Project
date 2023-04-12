from django.shortcuts import render
from .models import Item
from .forms import ItemSearchForm

def search(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        T_Force = request.POST.get('T_Force')
        results = Item.objects.filter(length=length, T_Force=T_Force)
        if results.exists():
            weights = [r.T_weight for r in results]
            mapcodes = [r.map_code for r in results]
            print(111111)
            return render(request, 'results.html', {'weights': weights, 'mapcodes': mapcodes})
        else:
            print(length)
            print(T_Force)
            return render(request, 'no_results.html')
    return render(request, 'search.html')


from django.shortcuts import render
from .models import Item

def show_all_data(request):
    # 从数据库中获取所有数据
    all_data = Item.objects.all()
    # 将数据传递到模板中进行渲染
    return render(request, 'all_data.html', {'data': all_data})
