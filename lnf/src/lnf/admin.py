from django.contrib import admin

# Register your models here.
from lnf.models import LostNFound


class LnfModelAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Contact', 'Lost_Found_Product', 'Location', 'Date_and_Time']
    list_filter = ['Name', 'Email', 'Contact', 'Lost_Found_Product', 'Small_Description','Location','Date_and_Time']
    search_fields = ['Name', 'Email', 'Contact', 'Lost_Found_Product', 'Small_Description','Location','Date_and_Time']

    # list_display = ['Name', 'tag_list']
    # fieldsets = ((None, {'fields': ('tags',)}),)

    # def get_queryset(self, request):
    #     return super(lnfModelAdmin, self).get_queryset(request).prefetch_related('tags')

    # def tag_list(self, obj):
    #     return u", ".join(o.name for o in obj.tags.all())

    class Meta:
        model = LostNFound


admin.site.register(LostNFound, LnfModelAdmin)
