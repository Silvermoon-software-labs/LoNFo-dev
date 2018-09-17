from django.contrib import admin

# Register your models here.
from lnf.models import Admin_Page

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['Name', 'Contact', 'Lost_Found_Product', 'Small_Description','Tags','Location','Date_and_Time']
	list_filter = ['Name', 'Contact', 'Lost_Found_Product', 'Small_Description','Tags','Location','Date_and_Time']
	# search_fields = ["title"]


	class Meta:
		model = Admin_Page


admin.site.register(Admin_Page, PostModelAdmin)



# admin.site.register(Admin_Page)