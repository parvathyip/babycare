from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def users_login(request):
    if request.POST:
        uname=request.POST['uname']
        print(uname,'uname')
        password=request.POST['pwd']
        user=authenticate(username=uname,password=password)
        print(user,'authenticae')
        if user is not None:
            if user.user_type=='admin':
                print('yes inside admin')
                messages.success(request,'Welcome to admin dashboard')
                return redirect('/admin-dashboard')
            elif user.user_type=='panchayat':
                plogid=user.id
                user=Panchayat.objects.get(panchayat_login=plogid)
                request.session['pid']=user.id
                messages.success(request,'Welcome to panchayat dashboard')
                return redirect('/panchayat-dashboard')
            elif user.user_type=='worker':
                wlogid=user.id
                worker=Worker.objects.get(worker_login=wlogid)
                request.session['wid']=worker.id
                messages.success(request,'Welcome to worker dashboard')
                return redirect('/worker-dashboard')
            elif user.user_type=='mother':
                mlogid=user.id
                mother=Mother.objects.get(mother_login=mlogid)
                request.session['mid']=mother.id
                messages.success(request,'Welcome to mother dashboard')
                return redirect('/mother-dashboard')
            elif user.user_type=='health':
                hlogid=user.id
                health=Healthcentre.objects.get(health_login=hlogid)
                request.session['hid']=health.id
                messages.success(request,'Welcome to healthcenter dashboard')
                return redirect('/healthcenter-dashboard')
        else:
            messages.success(request,'Login Credentials Invalid, Login again')
            return redirect('/users-login')
    return render(request,'users_login.html')

#admin
def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')

def admin_addpanchayat(request):
    if request.POST:
        name=request.POST['pname']
        district=request.POST['district']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        phone=request.POST['phone']
        email=request.POST['email']
        wardno=request.POST['wardno']
        pin=request.POST['pin']
        address=request.POST['address']
        print(name,district,uname,pwd,phone,email,pin,address)
        if Login.objects.filter(username=uname).exists():
            messages.success(request,'username already exists')
            return redirect('/admin-addpanchayat')
        else:
            panchayatlog=Login.objects.create_user(user_type='panchayat',view_password=pwd,username=uname,password=pwd)
            panchayatlog.save()
            addpanchayat=Panchayat.objects.create(panchayat_login=panchayatlog,panchayat_name=name,wardno=wardno,district=district,phone=phone,email=email,pin=pin,address=address)
            addpanchayat.save()
            messages.success(request,'Panchayat added sucessfully')
            return redirect('/admin-viewpanchayat')
    return render(request,'admin/admin_addpanchayat.html')

def admin_viewpanchayat(request):
    panchayats=Panchayat.objects.all().order_by('district')
    for panchayat in panchayats:
        if panchayat.wardno is not None:
            panchayat.wards = range(1, int(panchayat.wardno) + 1)
        else:
            panchayat.wards = []
    # wards=Ward.objects.all().order_by('panchayat__id'),"wards":wards

    return render(request,'admin/admin_viewpanchayat.html',{"panchayats":panchayats})

def admin_viewwarddetails(request):
    wardid=request.GET.get('wid')
    # warddata=Ward.objects.get(id=wardid)
    # warddata=Ward.objects.get(id=wardid)
    motherdata=Mother.objects.filter(worker__ward=wardid).order_by('first_name')
    print(motherdata)
    return render(request,'admin/admin_viewwarddetails.html',{"warddata":wardid,"motherdata":motherdata})

def admin_viewmotherfood(request):
    wardid=request.GET.get('wardid')
    print(wardid)
    foods=Food.objects.filter(worker__ward=wardid)
    return render(request,'admin/admin_viewmotherfood.html',{"foods":foods})

def admin_viewworkers(request):
    wardid=request.GET.get('wardid')
    workers=Worker.objects.filter(ward=wardid)
    return render(request,'admin/admin_viewworkers.html',{"workers":workers})

def admin_updatepanchayat(request):
    pid=request.GET.get('pid')
    panchayat=Panchayat.objects.get(id=pid)
    if request.POST:
        name=request.POST['pname']
        if 'district' in request.POST:
            district=request.POST['district']
        else:
            district=panchayat.district
        phone=request.POST['phone']
        email=request.POST['email']
        pin=request.POST['pin']
        address=request.POST['address']
        updatepanchayat=Panchayat.objects.filter(id=panchayat.id).update(panchayat_name=name,district=district,phone=phone,email=email,pin=pin,address=address)
        messages.success(request,'Panchayat updated sucessfully')
        return redirect('/admin-viewpanchayat')
    return render(request,'admin/admin_updatepanchayat.html',{"panchayat":panchayat})

def admin_deletepanchayat(request):
    pid=request.GET.get('pid')
    panchayat=Panchayat.objects.get(id=pid).panchayat_login.id
    print(panchayat)
    pdelete=Login.objects.filter(id=panchayat).delete()
    messages.success(request,'Panchayat deleted sucessfully')
    return redirect('/admin-viewpanchayat')

def admin_addscheme(request):
    if request.POST:
        name=request.POST['name']
        desc=request.POST['desc']
        eligibility=request.POST['eligibility']
        procedure=request.POST['procedure']
        if Scheme.objects.filter(scheme_name=name).exists():
            messages.success(request,'already exists')
            return redirect('/admin-addscheme')
        else:
            scheme=Scheme.objects.create(scheme_name=name,scheme_desc=desc,scheme_eligibility=eligibility,scheme_procedure=procedure)
            scheme.save()
            messages.success(request,'Scheme added sucessfully')
            return redirect('/admin-addscheme')
    schemes=Scheme.objects.all().order_by('published_on')
    return render(request,'admin/admin_addscheme.html',{"schemes":schemes})

def admin_deletescheme(request):
    schemeid=request.GET.get('sid')
    scheme=Scheme.objects.filter(id=schemeid).delete()
    messages.success(request,'Scheme deleted sucessfully')
    return redirect('/admin-addscheme')

def admin_updatescheme(request):
    schemeid=request.GET.get('sid')
    scheme=Scheme.objects.get(id=schemeid)
    if request.POST:
        name=request.POST['name']
        desc=request.POST['desc']
        eligibility=request.POST['eligibility']
        procedure=request.POST['procedure']
        scheme=Scheme.objects.filter(id=schemeid).update(scheme_name=name,scheme_desc=desc,scheme_eligibility=eligibility,scheme_procedure=procedure)
        messages.success(request,'Scheme updated sucessfully')
        return redirect('/admin-addscheme')
    return render(request,'admin/admin_updatescheme.html',{"scheme":scheme})

def admin_viewcaretips(request):
    tips=Tips.objects.all()
    return render(request,'admin/admin_viewcaretips.html',{'tips':tips})

def admin_viewvaccinations(request):
    vaccines=VaccinationInfo.objects.all()
    print(vaccines,'/')
    return render(request,'admin/admin_viewvaccinations.html',{"vaccines":vaccines})

#panchayat
def panchayat_dashboard(request):
    return render(request,'panchayat/panchayat_dashboard.html')

# def panchayat_addward(request):
#     pid=request.session['pid']
#     panchayat=Panchayat.objects.get(id=pid)
#     if request.POST:
#         ward=request.POST['ward']
#         if Ward.objects.filter(ward_name=ward).exists():
#             messages.success(request,'already exists')
#             return redirect('/panchayat-addward')
#         else:
#             addward=Ward.objects.create(panchayat=panchayat,ward_name=ward)
#             addward.save()
#             messages.success(request,'Ward added sucessfully')
#             return redirect('/panchayat-addward')
#     wards=Ward.objects.filter(panchayat=panchayat).order_by('ward_name')
#     print(wards,'///')
#     return render(request,'panchayat/panchayat_addward.html',{"wards":wards})

# def panchayat_updateward(request):
#     wid=request.GET.get('wid')
#     ward=Ward.objects.get(id=wid)
#     if request.POST:
#         ward=request.POST['ward']
#         updateward=Ward.objects.filter(id=wid).update(ward_name=ward)
#         messages.success(request,'Ward updated sucessfully')
#         return redirect('/panchayat-addward')
#     return render(request,'panchayat/panchayat_updateward.html',{"ward":ward})

# def panchayat_deleteward(request):
#     wid=request.GET.get('wid')
#     deleteward=Ward.objects.filter(id=wid).delete()
#     messages.success(request,'Ward deleted sucessfully')
#     return redirect('/panchayat-addward')

def panchayat_addworker(request):
    pid=request.session['pid']
    wardcount=Panchayat.objects.get(id=pid).wardno
    print(wardcount)
    wardrange=range(1,int(wardcount)+1)
    # wards=Ward.objects.filter(panchayat=pid)
    # print(wards)
    # workerwards=Worker.objects.filter(ward__panchayat__id=pid)[0].ward.id
    # print(workerwards)
    if request.POST:
        wardid=request.POST['wardid']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        age=request.POST['age']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        address=request.POST['address']
        if Login.objects.filter(username=uname).exists():
            messages.success(request,'username already exists')
            return redirect('/panchayat-addworker')
        elif Worker.objects.filter(ward=wardid,panchayat_id=pid).exists():
            messages.success(request,'Wardname already taken')
            return redirect('/panchayat-addworker')
        else:
            workerlog=Login.objects.create_user(user_type='worker',view_password=pwd,username=uname,password=pwd)
            workerlog.save()
            addworker=Worker.objects.create(worker_login=workerlog,panchayat_id=pid,ward=wardid,first_name=fname,last_name=lname,age=age,phone=phone,email=email,address=address)
            addworker.save()
            messages.success(request,'Worker added sucessfully')
            return redirect('/panchayat-viewworker')
    return render(request,'panchayat/panchayat_addworker.html',{"wards":wardrange})

def panchayat_viewworker(request):
    pid=request.session['pid']
    panchayat=Panchayat.objects.get(id=pid)
    workers=Worker.objects.filter(panchayat=panchayat).order_by('ward')
    print(workers)
    return render(request,'panchayat/panchayat_viewworker.html',{"workers":workers})

def panchayat_updateworker(request):
    workerid=request.GET.get('wid')
    pid=request.session['pid']
    worker=Worker.objects.get(id=workerid)
    # wards=Ward.objects.filter(panchayat=pid),"wards":wards
    if request.POST:
        # if 'wardid' in request.POST:
        #     wardid=request.POST['wardid']
        # else:
        #     wardid=worker.ward
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        age=request.POST['age']
        address=request.POST['address']
        updateworker=Worker.objects.filter(id=workerid).update(first_name=fname,last_name=lname,age=age,phone=phone,email=email,address=address)
        messages.success(request,'Worker updated sucessfully')
        return redirect('/panchayat-viewworker')
    return render(request,'panchayat/panchayat_updateworker.html',{"worker":worker})

def panchayat_deleteworker(request):
    workerid=request.GET.get('wid')
    worker=Worker.objects.get(id=workerid).worker_login.id
    workerdelete=Login.objects.filter(id=worker).delete()
    messages.success(request,'Worker deleted sucessfully')
    return redirect('/panchayat-viewworker')

def panchayat_addhealthcenter(request):
    pid=request.session['pid']
    if request.POST:
        hname=request.POST['hname']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        if Login.objects.filter(username=uname).exists():
            messages.success(request,'username already exists')
            return redirect('/panchayat-addhealthcenter')
        else:
            healthcenterlog=Login.objects.create_user(user_type='health',view_password=pwd,username=uname,password=pwd)
            healthcenterlog.save()
            addworker=Healthcentre.objects.create(health_login=healthcenterlog,panchayat_id=pid,health_name=hname,health_phone=phone,email=email,health_address=address)
            addworker.save()
            messages.success(request,'Health Center added sucessfully')
            return redirect('/panchayat-viewhealthcenter')
    return render(request,'panchayat/panchayat_addhealthcenter.html')

def panchayat_viewhealthcenter(request):
    pid=request.session['pid']
    healths=Healthcentre.objects.filter(panchayat_id=pid)
    return render(request,'panchayat/panchayat_viewhealthcenter.html',{"healths":healths})

def panchayat_deletehealthcenter(request):
    healthid=request.GET.get('hid')
    health=Healthcentre.objects.get(id=healthid).health_login.id
    workerdelete=Login.objects.filter(id=health).delete()
    messages.success(request,'Health Center deleted sucessfully')
    return redirect('/panchayat-viewhealthcenter')

def panchayat_updatehealthcenter(request):
    healthid=request.GET.get('hid')
    pid=request.session['pid']
    health=Healthcentre.objects.get(id=healthid)
    if request.POST:
        hname=request.POST['hname']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        updatehealthcenter=Healthcentre.objects.filter(id=healthid).update(health_name=hname,health_phone=phone,email=email,health_address=address)
        messages.success(request,'Healthcenter updated sucessfully')
        return redirect('/panchayat-viewhealthcenter')
    return render(request,'panchayat/panchayat_updatehealthcenter.html',{"health":health})

#worker
def worker_dashboard(request):
    return render(request,'worker/worker_dashboard.html')

def worker_addmother(request):
    wid=request.session['wid']
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        age=request.POST['age']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        childbool=request.POST['flexRadioDefault']
        cfname=request.POST.getlist('cfirstname')
        clname=request.POST.getlist('clastname')
        cage=request.POST.getlist('cage')
        cweight=request.POST.getlist('cweight')
        pregnant=request.POST['pregnentMonth']
        pmonth=request.POST['pmonth']
        pweight=request.POST['pweight']
        print('fname=', fname, '\nlname=', lname, '\nuname=' , uname,'\npwd=',pwd,'\nage=',age,'\nphone=',phone,'\nemail=',email,
              '\naddress=',address,'\nchildbool=',childbool,'\ncfname=',cfname,'\nclname=',clname,'\ncage=',cage,'\ncweight=',cweight,
              '\npregnent=',pregnant,'\npmonth=',pmonth,'\npweight=',pweight)
        if Login.objects.filter(username=uname).exists():
            messages.success(request,'username already exists')
            return redirect('/worker-addmother')
        else:
            motherlog=Login.objects.create_user(user_type='mother',view_password=pwd,username=uname,password=pwd)
            motherlog.save()
            addmother=Mother.objects.create(mother_login=motherlog,worker_id=wid,first_name=fname,last_name=lname,age=age,
                                            phone=phone,email=email,address=address,is_child=childbool,is_pregnant=pregnant,
                                            pregnancy_month=pmonth,pregnancy_weight=pweight)
            addmother.save()
            if childbool == 'yes':
                for f,l,a,w in zip(cfname,clname,cage,cweight):
                    addchild=Child.objects.create(mother=addmother,first_name=f,last_name=l,age=a,weight=w)
                    addchild.save()
                    print(f,l,a,w)
            messages.success(request,'Mother added sucessfully')
            return redirect('/worker-viewmother')
    return render(request,'worker/worker_addmother.html')

def worker_viewmother(request):
    wid=request.session['wid']
    mothers=Mother.objects.filter(worker_id=wid)
    childs=Child.objects.filter(mother__in=mothers).order_by('mother__id')
    return render(request,'worker/worker_viewmother.html',{"mothers":mothers,"childs":childs})

def worker_addmotherfood(request):
    # motherid=request.GET.get('mid')
    wid=request.session['wid']
    print(wid)
    if request.POST:
        foodname=request.POST['foodname']
        foodunits=request.POST['unit']
        person=request.POST['person']
        fooddesc=request.POST['fooddesc']
        addfood=Food.objects.create(worker_id=wid,food_list=foodname,unit=foodunits,food_for=person,detail_desc=fooddesc)
        addfood.save()
        messages.success(request,'Food details sucessfully added')
    foods=Food.objects.filter(worker_id=wid).order_by('given_on') 
    return render(request,'worker/worker_addmotherfood.html',{"foods":foods})

def worker_deletemotherfood(request):
    foodid=request.GET.get('fid')
    fooddelete=Food.objects.filter(id=foodid).delete()
    messages.success(request,'Food details sucessfully deleted')
    return redirect('/worker-addmotherfood')

def worker_addcaretips(request):
    wid=request.session['wid']
    # ward=Worker.objects.get(id=wid).ward.id
    if request.POST:
        tip=request.POST['tipname']
        tipdesc=request.POST['tipdesc']
        tipadd=Tips.objects.create(worker_id=wid,tip_name=tip,tip_desc=tipdesc)
        tipadd.save()
        messages.success(request,'Healthcare tips added sucessfully')
        return redirect('/worker-addcaretips')
    tips=Tips.objects.filter(worker__id=wid)
    return render(request,'worker/worker_addcaretips.html',{"tips":tips})

def worker_deletecaretip(request):
    tipid=request.GET.get('tipid')
    tipdelete=Tips.objects.filter(id=tipid).delete()
    messages.success(request,'Healthcare tips deleted sucessfully')
    return redirect('/worker-addcaretips')

def worker_updatecaretip(request):
    tipid=request.GET.get('tipid')
    tipdata=Tips.objects.get(id=tipid)
    if request.POST:
        tip=request.POST['tipname']
        tipdesc=request.POST['tipdesc']
        tipadd=Tips.objects.filter(id=tipid).update(tip_name=tip,tip_desc=tipdesc)
        messages.success(request,'Healthcare tips updated sucessfully')
        return redirect('/worker-addcaretips')
    return render(request,'worker/worker_updatecaretip.html',{'tipdata':tipdata})

def worker_viewschemes(request):
    schemes=Scheme.objects.all().order_by('published_on')
    return render(request,'worker/worker_viewschemes.html',{'schemes':schemes})

def worker_viewvaccinations(request):
    wid=request.session['wid']
    wpan=Worker.objects.get(id=wid).panchayat
    vaccines=VaccinationInfo.objects.filter(healthcentre__panchayat=wpan)#can view any health centers vaccine info inside a panchayat
    print(vaccines)
    return render(request,'worker/worker_viewvaccinations.html',{'vaccines':vaccines})

def worker_viewdiseases(request):
    wid=request.session['wid']
    worker=Worker.objects.get(id=wid).panchayat
    diseases=Disease.objects.filter(healthcentre__panchayat=worker)
    print(diseases)
    return render(request,'worker/worker_viewdiseases.html',{"diseases":diseases})

#mother
def mother_dashboard(request):
    return render(request,'mother/mother_dashboard.html')

def mother_viewcaretips(request):
    motherid=request.session['mid']
    mother=Mother.objects.get(id=motherid).worker
    tips=Tips.objects.filter(worker=mother)
    return render(request,'mother/mother_viewcaretips.html',{"tips":tips})

def mother_viewfooddetails(request):
    motherid=request.session['mid']
    motherworker=Mother.objects.get(id=motherid).worker.id
    mother_ischild=Mother.objects.get(id=motherid).is_child
    mother_ispregnant=Mother.objects.get(id=motherid).is_pregnant
    print(mother_ischild,mother_ispregnant)
    foods=Food.objects.filter(worker_id=motherworker)
    print(foods)
    return render(request,'mother/mother_viewfooddetails.html',{"foods":foods,"mother_ischild":mother_ischild,"mother_ispregnant":mother_ispregnant})

def mother_viewschemes(request):
    schemes=Scheme.objects.all().order_by('published_on')
    return render(request,'mother/mother_viewschemes.html',{'schemes':schemes})

def mother_viewdiseases(request):
    mid=request.session['mid']
    mother=Mother.objects.get(id=mid).worker.panchayat
    diseases=Disease.objects.filter(healthcentre__panchayat=mother)
    print(diseases)
    return render(request,'mother/mother_viewdiseases.html',{"diseases":diseases})

def mother_viewvaccinationdetails(request):
    mid=request.session['mid']
    mother=Mother.objects.get(id=mid).worker.panchayat
    vaccines=VaccinationInfo.objects.filter(healthcentre__panchayat=mother)
    print(vaccines,'/')
    return render(request,'mother/mother_viewvaccinationdetails.html',{"vaccines":vaccines})

#health
def healthcenter_dashboard(request):
    return render(request,'health/healthcenter_dashboard.html')

def health_adddiseasedetails(request):
    healthid=request.session['hid']
    if request.POST:
        title=request.POST['title']
        desc=request.POST['desc']
        symptom=request.POST['symptom']
        prevention=request.POST['prevention']
        diseaseadd=Disease.objects.create(healthcentre_id=healthid,disease_title=title,disease_desc=desc,disease_symptoms=symptom,disease_prevention=prevention)
        diseaseadd.save()
        messages.success(request,'Disease added sucessfully')
        return redirect('/health-adddiseasedetails')
    diseases=Disease.objects.filter(healthcentre_id=healthid)
    return render(request,'health/health_adddiseasedetails.html',{"diseases":diseases})

def health_deletedisease(request):
    healthid=request.session['hid']
    disease=Disease.objects.filter(id=healthid).delete()
    return redirect('/health-adddiseasedetails')

def health_addvaccineinfo(request):
    healthid=request.session['hid']
    print(healthid)
    hpan=Healthcentre.objects.get(id=healthid).panchayat.id
    if request.POST:
        title=request.POST['title']
        desc=request.POST['desc']
        age=request.POST['age']
        prevention=request.POST['prevention']
        dose=request.POST['dose']
        availablecount=request.POST['availablecount']
        vdate=request.POST['vdate']
        vfrom=request.POST['vfrom']
        vto=request.POST['vto']
        vaccineadd=VaccinationInfo.objects.create(vaccination_date=vdate,vaccination_from=vfrom,vaccination_to=vto,healthcentre_id=healthid,availabecount=availablecount,vaccination_name=title,vaccination_desc=desc,vaccination_age=age,disease_prevented=prevention,dose=dose)
        vaccineadd.save()
        messages.success(request,'Vaccination Info added sucessfully')
        return redirect('/health-addvaccineinfo')
    vaccines=VaccinationInfo.objects.filter(healthcentre__panchayat__id=hpan)
    print(vaccines)
    return render(request,'health/health_addvaccineinfo.html',{'vaccines':vaccines})