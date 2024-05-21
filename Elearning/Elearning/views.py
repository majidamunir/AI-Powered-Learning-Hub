from django.shortcuts import redirect,render
from app.models import Categories,Course,Level,Video,UserCourse
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
from django.http import Http404



def INDEX(request):
    return render(request,'index.html')

def CHATBOT(request):
    return render(request,'chatbot/bot.html')


def HOME(request):
    category= Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'category':category,
        'course':course,
    }

    
    return render(request,'main/home.html',context)

def COURSES(request):
    category= Categories.get_all_category(Categories)
    level =Level.objects.all()
    course =Course.objects.all()
    FreeCourse_count=Course.objects.filter(price=0).count()
    PaidCourse_count=Course.objects.filter(price__gte=1).count()

    

    context ={
        'category': category,
        'level' : level,
        'course' : course,
        'FreeCourse_count' : FreeCourse_count,
        'PaidCourse_count' : PaidCourse_count,

    }
    return render(request,'main/course.html',context)


def filter_data(request):
    category=request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
       course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
       course = Course.objects.all()
    elif category:
        course=Course.objects.filter(category__id__in=category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
        course=Course.objects.all().order_by('-id')
        
    context={
        'course': course
    }

    t = render_to_string('ajax/course.html',context)
    return JsonResponse({'data': t})

def CONTACT(request):
    category= Categories.get_all_category(Categories)

    context={
        'category':category,
    }
    return render(request,'main/contact.html',context)

def ABOUT(request):
    category= Categories.get_all_category(Categories)

    context={
        'category':category,
    }
    return render(request,'main/about.html',context)

def SEARCH_COURSE(request):
    category= Categories.get_all_category(Categories)
    query=request.GET['query']
    course=Course.objects.filter(title__icontains=query)

    context = {
        'category':category,
        'course' :course,
    }
    return render(request,'search/search.html',context)


def COURSE_DETAILS(request,slug):
    category= Categories.get_all_category(Categories)
    time_duration=Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    course=Course.objects.filter(slug=slug)
    course_id=Course.objects.get(slug=slug)

    try:
        check_enroll=UserCourse.objects.get(user=request.user,course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll=None


    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context={
        'category':category,
        'course': course,
        'time_duration':time_duration,
        'check_enroll':check_enroll,
        
    }
    return render(request,'SingleCourse/coursedetail.html',context)

def PAGE_NOT_FOUND(request):
    category= Categories.get_all_category(Categories)

    context={
        'category':category,
    }
    return render(request,'Error/404.html',context)

def CHECKOUT(request,slug):
    course=Course.objects.get(slug=slug)
   

    if course.price == 0:
        usercourse=UserCourse(
            user=request.user,
            course=course
        )
        usercourse.save()
        messages.success(request,'Course Are Successfully Enrolled')
        return redirect('my_course')
    context={
        'course':course,
    }
    return render(request,'checkout/checkout.html',context)


def MY_COURSE(request):
    course=UserCourse.objects.filter(user=request.user)
    context={
        'course': course,
    }
    return render(request,'SingleCourse/mycourses.html',context)



def WATCH_COURSE(request, slug):
    lecture = request.GET.get('lecture')
    course = Course.objects.get(slug=slug)
    
    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course)
        video = Video.objects.get(id=lecture)
        
        # Get the previous video
        previous_video = Video.objects.filter(course=course, id__lt=video.id).order_by('-id').first()
        
        # Get the next video
        next_video = Video.objects.filter(course=course, id__gt=video.id).order_by('id').first()
        
        if course:
            context = {
                'course': course,
                'video': video,
                'lecture': lecture,
                'check_enroll': check_enroll,
                'previous_video': previous_video,
                'next_video': next_video
            }
            return render(request, 'SingleCourse/watch-course.html', context)
        else:
            return redirect('404')
    except UserCourse.DoesNotExist:
        return redirect('404')



