from django.contrib import admin
from .models import Issue,Inword,Stock,Collages
# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(Collages)
class CollagesAdmin(ImportExportModelAdmin):
    list_display = ('id', 
 
    'name',
)

@admin.register(Issue)
class IssueAdmin(ImportExportModelAdmin):
    list_display = ('id', 
    'particulars',
    'qty',   
    'issue_by',
)

@admin.register(Inword)
class InwordAdmin(ImportExportModelAdmin):
    list_display = ('id', 
    'name',
    'particulars',
    'qty',
    'delivery_date',
   
)

@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ('id', 

    'particulars',
    'qty',
    'delivery_date',
   
)
