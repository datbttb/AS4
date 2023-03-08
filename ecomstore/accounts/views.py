from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderItem
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from accounts.forms import UserProfileForm, RegistrationForm


def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_account')
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    context = {'form': form, 'page_title': page_title}
    return render(request, template_name, context)

@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    context = {'page_title': page_title, 'orders': orders, 'name': name}
    return render(request, template_name, context)


@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items,
        'page_title': page_title
    }
    return render(request, template_name, context)

@login_required
def order_info(request, template_name="registration/order_info.html"):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_account'))
    else:
        form = UserProfileForm(instance=user_profile)
    page_title = 'Edit Order Information'
    return render(request, template_name, {'form': form, 'page_title': page_title})
