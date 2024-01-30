from django.shortcuts import render


def main(request):
    return render(request, 'news.html', {})


def news():
    return None