from django.http import HttpResponse
from django.shortcuts import render
from .modules import test, batch

def index(request):
    print(test.test_ryu())
    # batch.task()
    params = {
        "message": "this is me"
    }
    if request.method == "POST":
        if "btn_ok" in request.POST:
        # ①
            params["message"]="678"
        elif "btn_cancel" in request.POST:
        # ②
            print("キャンセルボタン押下された２")

    return render(request,'App_Folder_HTML/index.html',context=params)
