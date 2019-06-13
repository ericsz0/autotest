from django.contrib import admin
from apptest.models import Appcase,Appcasestep
from webtest.models import Webcase,Webcasestep

# Register your models here.
class AppcasestepAdmin(admin.TabularInline):
    list_display = ['appteststep','apptestobjname','appfindmethod','appevelement','appoptmethod','appassertdata','apptestresult','create_time','id','appcase']
    model = Appcasestep
    extra = 1

class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename','apptestresult','create_time','id']
    inlines = [AppcasestepAdmin]

class WebcasestepAdmin(admin.TabularInline):
    list_display = ['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata','webtestresult','create_time','id','webcase']
    model = Webcasestep
    extra = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresult','create_time','id']
    inlines = [WebcasestepAdmin]
admin.site.register(Appcase,AppcaseAdmin)