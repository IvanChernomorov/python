from django.contrib import admin
from .models import Songs, Artists,Albums

admin.site.register(Artists)
admin.site.register(Albums)	
 

class PostModelAdmin(admin.ModelAdmin):
	list_display ['title', 'timestamp', 'updated']
	list_display_links ['timestamp', 'updated']
	list_filter ['timestamp', 'updated']
	search_fields ['title', 'content']
	list_editable ['title']
	class Meta:
		model Songs

admin.site.register(Songs, PostModelAdmin)