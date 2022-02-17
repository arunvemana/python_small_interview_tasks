from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.

def test(request):
    template = loader.get_template('stocks/index.html')
    stock_list = [{'id':1},{'id':2}]
    context = {'name': 'hello', 'stock_list': stock_list}
    # return render(request,'stocks/index.html')
    return render(request,'stocks/index.html',context)


def form(request):
    try:
        id = request.POST.get('stockid',None)
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        print(id,name,email)
        return HttpResponse(status=200)
    except Exception as e:
        print(e)