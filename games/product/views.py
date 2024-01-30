from django.shortcuts import render, redirect
from .models import Review, Order, Product
from datetime import datetime

context = {'product': '', }


def product_info(request, pk):
    global context
    try:
        product = Product.objects.get(pk=int(pk))
        reviews = Review.objects.filter(product=int(pk))
        context = {
            'product': product,
            'reviews': reviews,
        }
    except:
        context = {
            'product': '',
            'message': 'Упс.. Данные не найдены',
        }
    finally:
        return render(request, 'product_info.html', context)


def news(request):
    global context
    products = Product.objects.order_by("-id")
    news_ = Product.objects.order_by("-datetime")[:3]
    context = {
        'products': products,
        'news': news_,
    }
    return render(request, 'news.html', context)


def catalog(request):
    global context
    products = Product.objects.order_by("-id")
    context = {
        'products': products,
    }
    return render(request, 'catalog.html', context)


def search(request):
    global context
    products = ''

    sear = request.POST.get("search"),
    products = Product.objects.filter(name__icontains=sear[0].strip())
    context = {
        'products': products,
    }
    return render(request, 'search.html', context)


# добавление нового отзыва
def newreview(request, pk):
    global context
    try:
        product = Product.objects.get(pk=int(pk))
        rating = request.POST.get("rating"),
        rating_add = 0
        for r in rating:
            if r:
                rating_add = int(r)

        text = request.POST.get("text"),
        new = Review(
            rating=rating_add,
            text=text[0],
            product=product,
            datetime=datetime.now())
        new.save()
        product_rating_update(product, rating_add)
        response = redirect('/catalog/' + str(product.pk) + '/')
        return response

    except:
        context = {
            'product': '',
            'message': 'Упс.. Данные не найдены',
        }
        # finally:
        return render(request, 'product_info.html', context)


def product_rating_update(product, add_rating):
    product_reviews = product.reviews + 1
    product_rating = round(((product.rating + int(add_rating)) / product_reviews), 2)
    Product.objects.filter(pk=product.pk).update(reviews=product_reviews, rating=product_rating)


def order_n(request, pk):
    global context
    try:
        product = Product.objects.get(pk=int(pk))
        context = {
            'product': product,
        }
    except:
        context = {
            'product': '',
            'message': 'Упс.. Данные не найдены',
        }
    finally:
        return render(request, 'order_n.html', context)


mess = 'ok'


def order_add(request, pk):
    global context
    global mess
    try:
        product = Product.objects.get(pk=int(pk))

        l_name = request.POST.get("l_name"),
        f_name = request.POST.get("f_name"),
        s_name = request.POST.get("s_name"),
        address = request.POST.get("address"),
        phone = request.POST.get("phone"),
        order = ''

        if (len(l_name[0]) == 0 or len(f_name[0]) == 0 or len(s_name[0]) == 0
                or len(phone[0]) == 0 or len(address[0]) == 0):
            mess = 'Не все поля заполнены!'
        if mess == 'ok':
            if l_name[0].strip().isalpha() and f_name[0].strip().isalpha() and s_name[0].strip().isalpha():
                pass
            else:
                mess = 'Данные введены не корректно. Проверьте введенные данные!'
        if mess == 'ok':
            if phone[0].strip().replace('+', '').isdigit():
                pass
            else:
                mess = 'Данные введены не корректно. Проверьте введенные данные! 2'

        if mess == 'ok':
            order = Order.objects.create(
                product=product,
                name=l_name[0].strip() + ' ' + f_name[0].strip() + ' ' + s_name[0].strip(),
                mobile=phone[0].strip(),
                address=address[0],
                state=2,
                datetime=datetime.now())

        context = {
            'product': product,
            'order': order,
            'message': mess,
        }
    except:
        mess = 'товар не найден'
        context = {
            'product': '',
            'order': '',
            'message': mess,
        }
    finally:
        return render(request, 'order_add.html', context)
