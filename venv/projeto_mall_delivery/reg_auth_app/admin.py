from django.contrib import admin
from .models import Lojista

@admin.action(description='Aprovar lojistas selecionados')
def approve_lojistas(modeladmin, request, queryset):
    queryset.update(is_approved=True)

class LojistaAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_approved')
    list_filter = ('is_approved', 'is_active')
    actions = [approve_lojistas]

admin.site.register(Lojista, LojistaAdmin)