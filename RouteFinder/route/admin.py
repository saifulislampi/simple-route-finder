from django.contrib import admin

# Register your models here.

from .models import Stopage,BusOption,Edge



class BusOptionInline(admin.TabularInline):
	model = BusOption.edges.through

class EdgeAdmin(admin.ModelAdmin):
	inlines = [
	   BusOptionInline
	]
	class Meta:
		model = Edge


# class AdjacentStopageInline(admin.TabularInline):
# 	model = Stopage.adjacent.through
#
# class StopageAdmin(admin.ModelAdmin):
# 	inlines = [
# 	   AdjacentStopageInline
# 	]
# 	class Meta:
# 		model = Stopage


admin.site.register(Stopage)
admin.site.register(BusOption)
admin.site.register(Edge,EdgeAdmin)
