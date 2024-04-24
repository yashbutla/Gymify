from django.shortcuts import render,redirect
from .models import Member
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings    
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def members(request):
    members = Member.objects.all().order_by('-id') 
    total_members = Member.objects.count()
    paid_members_count = Member.objects.filter(payment=True).count()
    unpaid_members_count = Member.objects.filter(payment=False).count()       
    context = {
     'members': members,
     'total_members': total_members,
     'paid_members_count': paid_members_count,
     'unpaid_members_count': unpaid_members_count,}
    return render(request, 'members.html',context)

def products(request):
    return render(request, 'products.html')

def mailing(request):
    return render(request, 'mailing.html')

def analytics(request):
    return render(request, 'analytics.html')

def attendance(request):
    return render(request, 'attendance.html')

def create_member(request):
    if request.method == 'POST':
        name          = request.POST.get('name')
        email         = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        height        = request.POST.get('height')
        weight        = request.POST.get('weight')
        start_date    = request.POST.get('start_date')
        end_date      = request.POST.get('end_date')
        fees          = request.POST.get('fees')
        training_type = request.POST.get('training_type')
       
        member = Member.objects.create(
            name=name,
            email=email,
            mobile_number=mobile_number,
            height=height,
            weight=weight,
            start_date=start_date,
            end_date=end_date,
            fees=fees,
            training_type=training_type
        )
        
        return redirect('member_info')

    return render(request, 'createmember.html')

def member_info(request):
    return render(request, 'memberinfo.html')

def store(request):
    return render(request, 'store.html')

def export_all(request):
    members   = Member.objects.all().order_by('-id') 
    workbook  = openpyxl.Workbook()
    worksheet = workbook.active
    headers   = ['ID', 'NAME', 'EMAIL','MOBILE','HEIGHT','WEIGHT' ,'START-DATE', 'END-DATE','FEES','TRAINING','PAYMENT-PAID']
    worksheet.append(headers)

    for member in members:
        row = [
            member.id,
            member.name,
            member.email,
            member.mobile_number,
            member.height,
            member.weight,
            member.start_date.strftime('%Y-%m-%d') if member.start_date else '',  # Format start date
            member.end_date.strftime('%Y-%m-%d') if member.end_date else '',      # Format end date
            member.fees,
            member.training_type,
            member.payment
        ]
        worksheet.append(row)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="gymify-members.xlsx"'
    workbook.save(response)
    return response

def email(request):
    email_address = request.GET.get('email')
    if email_address:
        e_message = "Hello, this is a test email."
        subject   = "Test Email"
        send_to   = [email_address]

        send_mail(
            subject,  
            e_message,    
            settings.EMAIL_HOST_USER, 
            send_to,   
            fail_silently=False,
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponse("Email address is missing", status=400)

def search_data(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            if query.isdigit():
                members = Member.objects.filter(Q(id=query))
            else:
                members = Member.objects.filter(Q(name__icontains=query))

            total_members = Member.objects.count()
            paid_members_count = Member.objects.filter(payment=True).count()
            unpaid_members_count = Member.objects.filter(payment=False).count()    
            context = {
            'members': members,
            'total_members': total_members,
            'paid_members_count': paid_members_count,
            'unpaid_members_count': unpaid_members_count,
            }
            return render(request, 'members.html', context)
        else:
            return render(request, 'members.html', {'members': None})
    else:
        return render(request, 'members.html', {'members': None})        

def sort_data(request):
    print("in........")
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == 'new':
            members = Member.objects.all().order_by('-id')[:10]
        elif query == 'unpaid':
            members = Member.objects.filter(payment=False)
        elif query == 'paid':
            members = Member.objects.filter(payment=True)
        elif query == 'personal_training':
            members = Member.objects.filter(training_type='Personal Training')
        else:
            members = None

        total_members = Member.objects.count()
        paid_members_count = Member.objects.filter(payment=True).count()
        unpaid_members_count = Member.objects.filter(payment=False).count()

        context = {
            'members': members,
            'total_members': total_members,
            'paid_members_count': paid_members_count,
            'unpaid_members_count': unpaid_members_count,
        }
        return render(request, 'members.html', context)