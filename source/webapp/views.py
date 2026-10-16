from django.shortcuts import render
from webapp.cat import Cat

def index_view(request):
    return render(request, 'index.html')

def cat_stats_view(request):
    if 'action' not in request.POST:
        cat = Cat(request.POST.get('name'))
        return render(request, 'cat_stats.html', {'cat': cat})
    else:
        cat = Cat(request.POST.get('name'))

        cat.happiness = int(request.POST.get('happiness'))
        cat.fullness = int(request.POST.get('fullness'))
        cat.is_sleeping = request.POST.get('is_sleeping') == 'True'


        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()

        return render(request, 'cat_stats.html', {'cat': cat})


