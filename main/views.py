from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Phantom Mask',
        'image' : 'https://imgur.com/a/U0fYFir',
        'price': '700000',
        'description': 'A mysterious Mask found in the depth of mountains, legend said that this mask once belong the the monkey king itself'
    }

    return render(request, "main.html", context)