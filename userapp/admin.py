from django.contrib import admin
from .models import CustomUser,Token
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'first_name', 'last_name','is_active']
    list_display_links=['email']
    
    class Meta:
        model = CustomUser

class TokenAdmin(admin.ModelAdmin):
    list_display=['user','token_key']
    list_display_links=['user']
    
    class Meta:
        model = Token

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Token,TokenAdmin)