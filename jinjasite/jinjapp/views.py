from django.shortcuts import render

# Create your views here.
def friends(request):
    friends = ['lavon', 'pit', 'ales`']

    context = {'my_friends' : friends}
    return render(request, 'friends.html', context)
