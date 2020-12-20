from django.shortcuts import render,redirect
from .models import Inword,Issue,Stock,Collages
import json as simplejson
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.core.management import call_command
from django.contrib import messages
import time
# Create your views here.



def admin(request):
    """
    docstring
    """
    pass


def backuprestore(request):
    if request.method == 'POST':
        if 'LocalBack' in request.POST:
            try:
                print('try')
                call_command('dbbackup')
                return redirect('backuprestore')
            except:
                print('exectute')
                return redirect('backuprestore')
        if 'restorefile' in request.POST:
            try:
                print('try')
                call_command('dbrestore','--noinput')
                return redirect('backuprestore')
            except:
                print('exectute')
                return redirect('backuprestore')

       
    else:
        return render(request,'root/backup.html')


def dbbackup():
    conn = sqlite3.connect('db.sqlite3')
    newtime = time.time()
    local_time = time.ctime(newtime)
    returnt = 'backup/clientes_dump '+str(local_time.replace(':','T'))+'.sql'
    with io.open(returnt, 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    print('Backup performed successfully.')
    conn.close()
    return returnt



def dashboard(request):
    return render(request, 'root/dashboard/desktop.html')
    

# issue code started

def getBatchData(request):
    
    stockdata = Stock.objects.filter(particulars = request.GET['particulars'])
    tmpJson = serializers.serialize("json",stockdata)
    tmpObj = simplejson.loads(tmpJson)
    return JsonResponse(simplejson.dumps(tmpObj) , safe=False)

def issue(request):
    
    if request.method == 'POST':
        data = Stock.objects.get(u_id=request.POST['u_id'])
        if data.qty =='0':
            messages.error(request, 'The Quantity of '+request.POST['particulars']+' is zero')
            print('sussess')
            return redirect('issue')
        else:
            data = Issue()
            data.department = request.POST['department']
            data.name_of_reciver =request.POST['name_of_rec']
            data.particulars =request.POST['particulars']
            data.qty =request.POST['qty']
            data.u_id =request.POST['u_id']
            data.unit =request.POST['unit']
            data.issue_by =request.POST['issue_by']
            data.issue_date =request.POST['date']
            data.remark =request.POST['remark']
            data.save()

            abc = Stock.objects.get(u_id=request.POST['u_id'])
            abc.qty = int(abc.qty) - int(request.POST['qty'])
            abc.save()
        

            return redirect('issue_list')
       
    else:
        stock= Stock.objects.all()
        name = Collages.objects.all()
        return render(request,'root/outword/issue.html',{'stocks':stock,"name":name})

def issue_list(request):
    data = Issue.objects.all()
    return render(request,'root/outword/issue_list.html',{'stocks':data})





# purchase code started
def inword(request):
    if request.method== "POST":
        if Stock.objects.filter(u_id=request.POST['id']).exists():        
            messages.error(request, 'The Batch No already Exist Try new one')
            return redirect('inword')
        else:
            inw = Inword()
            stocks = Stock()
            inw.name = request.POST['name']
            inw.particulars= request.POST['particulars']
            inw.qty= request.POST['qty']
            inw.unit = request.POST['unit']
            inw.u_id = request.POST['id']
            inw.delivery_date= request.POST['date']
            inw.remark= request.POST['remark']
            inw.total= request.POST['total']
            inw.paid= request.POST['paid']
            inw.remaining= request.POST['remaining']
            inw.price= request.POST['price']
            
            
            stocks.particulars= request.POST['particulars']
            stocks.qty= request.POST['qty']
            stocks.u_id = request.POST['id']
            stocks.unit = request.POST['unit']
            stocks.delivery_date= request.POST['date']
            stocks.remark= request.POST['remark']
            stocks.total= request.POST['total']
            stocks.price= request.POST['price']
            inw.save()
            stocks.save()
            return redirect('inword')
       
    else:
        inword= Inword.objects.all()
        return render(request,'root/inword/inword.html',{'stocks':inword})
    
def stock(request):
    st=Stock.objects.all()
    return render(request,'root/stock/stock.html',{'stocks':st})

def report(request):
    return render(request,'root/report/report.html',{})

def inwordreport(request):
    if request.method =="POST":
            fromdate= request.POST['fromdate']
            todate = request.POST['todate']
            
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Inwordreport.csv"'
            writer = csv.writer(response)
        
            writer.writerow([
              
               'delivery_date',
                'u_id',
                'name',
                'particulars',
                'qty',
                'unit',
                'total',
                'paid',
                'remaining',
                'price',
        
            ])
        
            users = Inword.objects.filter(Q(delivery_date__gte=fromdate) & Q(delivery_date__lte=todate)).values_list(
                'delivery_date',
                'u_id',
                'name',
                'particulars',
                'qty',
                'unit',
                'total',
                'paid',
                'remaining',
                'price',
                )
            
           
            for user in users: 
                writer.writerow(user)
                

            writer.writerow([])
            writer.writerow([])

            
          
            return response
    else:
        return render(request,"root/report/inwordreport.html")
  

def issuereport(request):
    if request.method =="POST":
            fromdate= request.POST['fromdate']
            todate = request.POST['todate']
            
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="issuereport.csv"'
            writer = csv.writer(response)
        
            writer.writerow([
              
               'department',
                'name_of_reciver',
                'particulars',
                'qty',
                'unit',
                'u_id',
                'issue_by',
                'issue_date',
                'remark',
                
        
            ])
        
            users = Issue.objects.filter(Q(issue_date__gte=fromdate) & Q(issue_date__lte=todate)).values_list(
                'department',
                'name_of_reciver',
                'particulars',
                'qty',
                'unit',
                'u_id',
                'issue_by',
                'issue_date',
                'remark',
                )
            
           
            for user in users: 
                writer.writerow(user)
                

            writer.writerow([])
            writer.writerow([])

            
          
            return response
    else:
        return render(request,"root/report/issuereport.html")


def stockreport(request):
    if request.method =="POST":
            fromdate= request.POST['fromdate']
            todate = request.POST['todate']
            
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="stockreport.csv"'
            writer = csv.writer(response)
        
            writer.writerow([
              
               'delivery_date',
                'u_id',
                'particulars',
                'qty',
                'unit',
                'remark',
                'total',
                'price',
              
                
        
            ])
        
            users = Stock.objects.filter(Q(delivery_date__gte=fromdate) & Q(delivery_date__lte=todate)).values_list(
                'delivery_date',
                'u_id',
                'particulars',
                'qty',
                'unit',
                'remark',
                'total',
                'price',
                )
            
           
            for user in users: 
                writer.writerow(user)
                

            writer.writerow([])
            writer.writerow([])

            
          
            return response
    else:
        return render(request,"root/report/stockreport.html")
    


