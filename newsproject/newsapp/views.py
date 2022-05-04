from django.shortcuts import render

# Create your views here.


def moviesinfo(request):
    my_dict = {'head_msg': 'Movies Information', 'sub_msg1': 'new movie',
               'sub_msg2': 'Hollywood Movies', 'sub_msg3': 'KGF2 Start with bumper', }
    return render(request, 'news.html', context=my_dict)


def sportsinfo(request):
    my_dict = {'head_msg': 'Sports Information', 'sub_msg1': 'msd retire from csk captionacy',
               'sub_msg2': 'MI loses First 5 matches', 'sub_msg3': 'RR on top of the ipl table', }
    return render(request, 'sports.html', context=my_dict)

def politicalinfo(request):
    my_dict = {'head_msg': 'Politics Information', 'sub_msg1': 'PETrol cross 120',
               'sub_msg2': 'russia attack on ukrain', 'sub_msg3': 'BJP won 4th time'}
    return render(request, 'political.html', context=my_dict)

def home(request):
    return render(request,'home.html')