from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('username','birthday')
    search_fields=('username',)
    def username(self, obj):
        return obj.user.username



