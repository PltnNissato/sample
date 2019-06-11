from django.shortcuts import render
from django.http import  HttpResponse
from .form import HelloForm

# Create your views here.
def index(request):
    # 1個目
    # return HttpResponse("Hello Django!!"),

    # 2個目
    # msg = request.GET['msg']
    # return HttpResponse('you typed:"' + msg +'".')

    # 3個目
    # if 'msg' in request.GET:
    #     msg = request.GET['msg']
    #     result = 'you typed:"' + msg +'".'
    # else:
    #     result = 'please send msgparameter!'
    # return HttpResponse(result)

    # 4個目
    # return render(request,'hello/index.html')

    # 4個目派生(一括管理できないのか確認) →できた
    # settings.pyのデフォルトで読みに行く場所の指定を変えてあげれば、一元管理できそう。
    # プロジェクトと同列位置にあるtemplatesフォルダを参照するようにしてみた。
    # return render(request,'hello01.html')

    # #5個目
    # params = {
    #     'title':'Hello/Index 変数版',
    #     'msg': 'サンプルで作ったページ。　変数で表示中。',
    # }
    # return render(request,'hello01.html',params)

    # 6個目
    # params = {
    #     'title':'Hello/Index 複数版',
    #     'msg': 'サンプルで作ったページ。　リンクタグありで表示中。',
    #     'goto':'next'
    # }
    # return render(request,'hello01.html',params)

    # 7個目
    #     params = {
    #         'title':'Hello/Index フォーム送信',
    #         'msg': 'お名前は？',
    #     }
    #     return render(request,'hello01.html',params)
    #
    #
    # def form(request):
    #     msg = request.POST['msg']
    #     params = {
    #         'title':'Hello/Form　受け取り側',
    #         'msg': 'こんにちは、' + msg + 'さん',
    #     }
    #     return render(request,'hello01.html',params)

    # 8個目
    params = {
        'title':'Hello Form関数',
        'msg': 'your data:',
        'form': HelloForm()

    }

    if (request.method == 'POST'):
        params['message'] = '名前' + request.POST['name'] + \
            '<br>メール' + request.POST['mail'] + \
            '<br>年齢' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request,'hello01.html',params)