from django.contrib import admin

# Register your models here.

from .models import Stopage,BusOption,Edge



class BusOptionInline(admin.TabularInline):
	model = BusOption.edges.through

class EdgeAdmin(admin.ModelAdmin):
	list_filter = ('source', 'dest')
	inlines = [
	   BusOptionInline
	]
	class Meta:
		model = Edge





class StopageAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_filter = ['adjacent']
	class Meta:
		model=Stopage



class BusOptionAdmin(admin.ModelAdmin):
	search_fields=['name']
	list_filter = ('edges', 'cost')
	class Meta:
		model=BusOption


admin.site.register(Stopage,StopageAdmin)
admin.site.register(BusOption,BusOptionAdmin)
admin.site.register(Edge,EdgeAdmin)
