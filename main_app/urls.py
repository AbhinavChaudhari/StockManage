from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.dashboard,name="desktop"),
    path('',views.issue,name="issue"),
    path('issue_list/',views.issue_list,name="issue_list"),
    # path('Newissue/',views.Newissue,name="Newissue"),
    # path('editIssue/<issueid>',views.editIssue,name="editIssue"),
    # path('deleteIssue/<issueid>',views.DeleteIssue,name="deleteIssue"),

    # purchased
    path('inword/',views.inword,name="inword"),
    path('getBatchData/',views.getBatchData,name="getBatchData"),

    path('stock/',views.stock,name="stock"),

    # report
    path("report/", views.report, name="report"),
    path("inwordreport/", views.inwordreport, name="inwordreport"),
    path("issuereport/", views.issuereport, name="issuereport"),
    path("stockreport/", views.stockreport, name="stockreport"),

    path('backuprestore/', views.backuprestore,name="backuprestore"),
    path('admin/', views.admin,name="admin"),


]