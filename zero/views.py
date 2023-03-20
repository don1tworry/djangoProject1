from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View





def index(request):
    context={
        'city':'成都',
        'adict':{
        'name':'chen',
        'address':'yuan'
    },
        'alist':[1,2,3]
    }
    return render(request, 'index.html', context)








def QAQ(request):

    return HttpResponse("hello world")


def _qaq(request):
    return render(request, '1.html')



def indexview(request):
    if request.method == 'GET':
        return HttpResponse('indexview get func')
    else:
        return HttpResponse('indexview post func')


class index1(View):
    def get(self,request):
        return render(request,'get.html')
    def post(self,request):
        return HttpResponse('这里实现注册逻辑')


#  定义一个装饰器
#  func = my_decorator(func)
def my_decorator(func):
    # wrapper函数必然会接收一个request对象,因为传入进来的func这个函数肯定会带这个参数
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper
# 我们定义的类视图
class DemoView1(View):
    # 我们给get方法添加上装饰器, 然后执行.
    @my_decorator
    def get(self, request):
        print('get方法')
        return HttpResponse('ok')

    # 类视图里面的对象方法: post方法
    def post(self, request):
        print('post方法')
        return HttpResponse('ok')










