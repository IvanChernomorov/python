from django.contrib import admin
from .models import Songs, Artists,Albums

class SongsAdmin(admin.ModelAdmin):
 	list_display = ['title', 'id_al', 'id_ar', 'length']
 	list_display_links = ['id_al', 'id_ar']
 	list_filter = ['id_ar']
 	search_fields = ['title']
 	list_editable = ['title']

class AlbumsAdmin(admin.ModelAdmin):
 	list_display = ['title', 'id_ar', 'release_date', 'label']
 	list_display_links = ['id_ar']
 	list_filter = ['id_ar', 'label']
 	search_fields = ['title']
 	list_editable = ['title']

class ArtistsAdmin(admin.ModelAdmin):
 	list_display = ['pseudonym', 'genre', 'formed_in', 'country']
 	list_filter = ['genre', 'country']
 	search_fields = ['pseudonym']

admin.site.register(Albums, AlbumsAdmin)	
admin.site.register(Songs, SongsAdmin)
admin.site.register(Artists, ArtistsAdmin)