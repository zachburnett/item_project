from django.shortcuts import render, redirect
from django.contrib import messages
from models import Item
from ..login_app.models import User
# Create your views here.
def index(request):
    context ={
        'items': Item.objects.all(),
        # 'items_made': User.objects.get(id = request.session.user_username),
        'user': User.objects.all()
    }
    return render(request,'item_app/index.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

def add(request):
    return render(request,'item_app/add.html')

def add_item(request):
    results = Item.objects.itemVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/item/add')
    
    return redirect('/item')

def remove(request, item_id, user_id):
    User.objects.get(id = user_id).items_made.remove(Item.objects.get(id = item_id))
    return redirect('/items')

def add_to(request,user_id):
    User.objects.get(id = user_id).items_made.add(table1)
    return redirect('/items')
def delete(request):
    pass
def show(request, item):
    Item.objects.get(id = item)
    return redirect('/item/show')
