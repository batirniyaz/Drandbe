from django.contrib import admin
from .models import AboutModel, OurPartnersModel, ServicesModel, TestimonialModel, PortfolioModel, \
    TeamMembersModel, FaqModel, BlogModel, ContactModel, AwardsModel, BlogCategoryModel, ProjectCategoryModel


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


class OurPartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description', 'image')
    search_fields = ('name', 'position', 'description')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'url', 'image', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'status', 'created_at', 'updated_at')


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description')
    search_fields = ('name', 'position', 'description')


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'image', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'created_at', 'updated_at')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name_of_award', 'description', 'certificate')
    search_fields = ('name_of_award', 'description')


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(AboutModel, AboutAdmin)
admin.site.register(OurPartnersModel, OurPartnersAdmin)
admin.site.register(ServicesModel, ServicesAdmin)
admin.site.register(TestimonialModel, TestimonialAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)
admin.site.register(TeamMembersModel, TeamMembersAdmin)
admin.site.register(FaqModel, FaqAdmin)
admin.site.register(BlogModel, BlogAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(AwardsModel, AwardsAdmin)
admin.site.register(BlogCategoryModel, BlogCategoryAdmin)
admin.site.register(ProjectCategoryModel, ProjectCategoryAdmin)

