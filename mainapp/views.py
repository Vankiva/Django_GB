from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog_red.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
