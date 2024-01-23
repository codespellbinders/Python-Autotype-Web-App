from django.shortcuts import render, HttpResponse
import pyautogui as pg
import time
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        limit = request.POST.get('limit')
        limit = int(limit)
        time.sleep(10)
        for i in range(limit):
            i = str(i)
            pg.write(i)
            pg.write(name)
            pg.press('Enter')
    return render(request, 'index.html')
