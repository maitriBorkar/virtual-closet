from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import LayerForm
from .models import WardrobeItem  
from .forms import WardrobeItemForm
from django.shortcuts import render, get_object_or_404

def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def closet(request):
    items = {
        'tops': WardrobeItem.objects.filter(user=request.user, category='top'),
        'pants': WardrobeItem.objects.filter(user=request.user, category='pants'),
        'shoes': WardrobeItem.objects.filter(user=request.user, category='shoes'),
    }
    return render(request, 'closet.html', {'items': items})

@login_required
def upload(request):
    form = WardrobeItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('closet')
    return render(request, 'upload.html', {'form': form})

@login_required
def layer_clothes(request):
    user_items = WardrobeItem.objects.filter(user=request.user)
    tops = user_items.filter(category='top')
    pants = user_items.filter(category='pants')
    shoes = user_items.filter(category='shoes')

    selected_top = selected_pants = selected_shoes = None

    if request.method == 'POST':
        top_id = request.POST.get('top')
        pants_id = request.POST.get('pants')
        shoes_id = request.POST.get('shoes')

        if top_id:
            selected_top = WardrobeItem.objects.get(id=top_id, user=request.user)
        if pants_id:
            selected_pants = WardrobeItem.objects.get(id=pants_id, user=request.user)
        if shoes_id:
            selected_shoes = WardrobeItem.objects.get(id=shoes_id, user=request.user)

    return render(request, 'layer.html', {
        'tops': tops,
        'pants': pants,
        'shoes': shoes,
        'top': selected_top,
        'pants_selected': selected_pants,
        'shoes_selected': selected_shoes,
    })