from django.contrib import admin
from user_profile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('friends',)

admin.site.register(Profile, ProfileAdmin)
