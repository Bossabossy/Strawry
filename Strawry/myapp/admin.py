from django.contrib import admin
from myapp.models import Table

class TableAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Table._meta.fields]
admin.site.register(Table,TableAdmin)
	
		