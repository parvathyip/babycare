"""
URL configuration for babycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from babycare_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('users-login/',views.users_login),
    #admin
    path('admin-dashboard/',views.admin_dashboard),
    path('admin-addpanchayat/',views.admin_addpanchayat),
    path('admin-viewpanchayat/',views.admin_viewpanchayat),
    path('admin-viewwarddetails/',views.admin_viewwarddetails),
    path('admin-viewmotherfood/',views.admin_viewmotherfood),
    path('admin-updatepanchayat/',views.admin_updatepanchayat),
    path('admin-deletepanchayat/',views.admin_deletepanchayat),
    path('admin-addscheme/',views.admin_addscheme),
    path('admin-deletescheme/',views.admin_deletescheme),
    path('admin-updatescheme/',views.admin_updatescheme),
    path('admin-viewworkers/',views.admin_viewworkers),
    path('admin-viewcaretips/',views.admin_viewcaretips),
    path('admin-viewvaccinations/',views.admin_viewvaccinations),
    #panchayat
    path('panchayat-dashboard/',views.panchayat_dashboard),
    # path('panchayat-addward/',views.panchayat_addward),
    # path('panchayat-updateward/',views.panchayat_updateward),
    # path('panchayat-deleteward/',views.panchayat_deleteward),
    path('panchayat-addworker/',views.panchayat_addworker),
    path('panchayat-viewworker/',views.panchayat_viewworker),
    path('panchayat-updateworker/',views.panchayat_updateworker),
    path('panchayat-deleteworker/',views.panchayat_deleteworker),
    path('panchayat-addhealthcenter/',views.panchayat_addhealthcenter),
    path('panchayat-viewhealthcenter/',views.panchayat_viewhealthcenter),
    path('panchayat-deletehealthcenter/',views.panchayat_deletehealthcenter),
    path('panchayat-updatehealthcenter/',views.panchayat_updatehealthcenter),
    #worker
    path('worker-dashboard/',views.worker_dashboard),
    path('worker-addmother/',views.worker_addmother),
    path('worker-viewmother/',views.worker_viewmother),
    path('worker-addmotherfood/',views.worker_addmotherfood),
    path('worker-deletemotherfood/',views.worker_deletemotherfood),
    path('worker-addcaretips/',views.worker_addcaretips),
    path('worker-deletecaretip/',views.worker_deletecaretip),
    path('worker-updatecaretip/',views.worker_updatecaretip),
    path('worker-viewschemes/',views.worker_viewschemes),
    path('worker-viewvaccinations/',views.worker_viewvaccinations),
    # path('worker-addvaccinedate/',views.worker_addvaccinedate),
    path('worker-viewdiseases/',views.worker_viewdiseases),
    #mother
    path('mother-dashboard/',views.mother_dashboard),
    path('mother-viewcaretips/',views.mother_viewcaretips),
    path('mother-viewfooddetails/',views.mother_viewfooddetails),
    path('mother-viewschemes/',views.mother_viewschemes),
    path('mother-viewdiseases/',views.mother_viewdiseases),
    path('mother-viewvaccinationdetails/',views.mother_viewvaccinationdetails),
    #health
    path('healthcenter-dashboard/',views.healthcenter_dashboard),
    path('health-adddiseasedetails/',views.health_adddiseasedetails),
    path('health-deletedisease/',views.health_deletedisease),
    path('health-addvaccineinfo/',views.health_addvaccineinfo),
    
]
