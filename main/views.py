from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Phantom Mask',
        'price': '700000',
        'description': 'A mysterious Mask found in the depth of mountains, legend said that this mask once belong the the monkey king itself'
    }

    return render(request, "main.html", context)