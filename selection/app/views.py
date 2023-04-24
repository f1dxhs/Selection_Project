from django.shortcuts import render
from .models import Item
from .forms import ItemSearchForm
from django.db.models import Q
def search(request):
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
    return render(request, 'search.html')



from django.shortcuts import render
from .models import Item

def show_all_data(request):
    # 从数据库中获取所有数据
    all_data = Item.objects.all()
    # 将数据传递到模板中进行渲染
    return render(request, 'all_data.html', {'data': all_data})





# 假设这样一种情况，我已经用django开发了一个网页，并且他可以对我本地的数据库的一张表单进行一些基本的筛选工作，我在我的models.py里
# 用meta函数提到了这张表，那现在如果我想换一张表应该怎么操作呢，我并不是需要简单的在models.py里更改表单，而是通过用户的要求来选择应该使用哪张表单
# 大致的情况是这样，用户在网页上选择要对a或者b进行筛选，而a和b分别对应我本地数据库的表，如果用户选择a那么就对a表进行筛选操作，此外a，b量表的数据类型是相同的 只是数值不同，所以我希望他们可以共用一个筛选函数



# 工作流程: 多app方向 字典查阅 ---> 写出父类class ---> 