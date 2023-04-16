from django.shortcuts import render, redirect
from .models import Navbar, Meeting, Category, Course, Strongest, AboutUniversity, AboutMe, Message
from .forms import MessageForm

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    navbar = Navbar.objects.filter(is_published=True).order_by('-created_at')[0]
    courses = Course.objects.all()
    categories = Category.objects.all()
    try:
        meetings = Meeting.objects.all().order_by('-pk')[:4]
    except:
        meetings = Meeting.objects.all()
    strongests = Strongest.objects.all()
    about_university = AboutUniversity.objects.all().order_by('-pk')[0]
    about_me = AboutMe.objects.all().order_by('-pk')[0]
    form = MessageForm()
    context = {
        'navbar': navbar,
        'courses': courses,
        'categories': categories,
        'meetings': meetings,
        'strongests': strongests,
        'about_university': about_university,
        'about_me': about_me,

        'form': form,
        'title': "Education Meeting",
    }
    return render(request, 'meetting/index.html', context)


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            message = request.POST['message']
            email = request.POST['mail']
            name = request.POST['name']
            subject = request.POST['subject']

            send_mail(
                subject,
                message,
                email,
                ['madrahimovq@gmail.com'],
                fail_silently=False
            )



    return redirect('index')


def meeting_list(request):
    meetings = Meeting.objects.all()
    context = {
        'meetings': meetings,
        "title": "Meetings"
    }
    return render(request, 'meetting/meetings.html', context)


def meeting_detail(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    context = {
        'meeting': meeting,
        'title': meeting.title
    }
    return render(request, 'meetting/meeting_detail.html', context)