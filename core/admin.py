from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.



class BuildingTableAdmin(admin.ModelAdmin):
    list_display = ('organization_id','name','code','city','state','country','zip','status')
    list_filter = ('organization_id','city','status')
    # readonly_fields=('fileUploadUser','candidateFileName','candidateFileNamePDF','date_added','fileUploadDate')
    # list_display_links = ('first_name','last_name','skill_keywords_found',)

    # def skill_keywords_found(self,obj):
    #     return format_html(f'<h4 style="color:green" >{obj.skill_keywords_full}</h4>')



class BuildingItemTableAdmin(admin.ModelAdmin):
    list_display = ('building_id','name','parent_building_item','people_id','code','building_item_category_id',)
    list_filter = ('code','building_id','parent_building_item','building_item_category_id')


class BuildingSelectionListTableAdmin(admin.ModelAdmin):
    list_display = ('building_id','name','code','obsolete')
    list_filter = ('building_id','name','code','obsolete')


class BuildingSelectionListItemTableAdmin(admin.ModelAdmin):
    list_display = ('building_selection_list_id','name','code','obsolete')
    list_filter = ('building_selection_list_id','name','code','obsolete')




class ProjectTableAdmin(admin.ModelAdmin):
    list_display = ('organization_id','name','code','project_administrator_id','company_id','city','state','country')
    list_filter = ('organization_id','name','code','project_administrator_id','company_id','city','state','country')


class ProjectSelectionListTableAdmin(admin.ModelAdmin):
    list_display = ('project','name','code','obsolete',)
    list_filter = ('project','name','code','obsolete',)


class ProjectSelectionListItemTableAdmin(admin.ModelAdmin):
    list_display = ('project_selection_list_id','name','code','obsolete')
    list_filter = ()



class SkillsKeywordsTableAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    list_filter = ('name','code',)


class TaskTableAdmin(admin.ModelAdmin):
    list_display = ('project','assignees','task')
    list_filter = ('project','assignees','task')



class FileTableAdmin(admin.ModelAdmin):
    list_display = ('table_key','table_name','file_type','file_name')
    list_filter = ('table_key','table_name','file_type','file_name')



class NonWorkingDaysTableAdmin(admin.ModelAdmin):
    list_display = ('obsolete','project_id','value_day','value_date','day_or_date','value_display')
    list_filter = ('obsolete','project_id','value_day','value_date','day_or_date','value_display')



class OrganizationTableAdmin(admin.ModelAdmin):
    list_display = ('name','code','organization_administrator','customer_company','active')
    list_filter = ('name','code','organization_administrator','customer_company','active')




class PeopleTableAdmin(admin.ModelAdmin):
    list_display = ('name_first','name_last','resume_file_name','current_latest_position','phone','email')
    list_filter = ('current_latest_position','code')



class SupportRequestTableAdmin(admin.ModelAdmin):
    list_display = ('userid','comment')
    list_filter = ()


class ViewTableAdmin(admin.ModelAdmin):
    list_display = ('name','app','view_name',)
    list_filter = ('category',)



class ViewFieldTableAdmin(admin.ModelAdmin):
    list_display = ('column_name','alias')
    list_filter = ('column_name','alias')


class ColorMasterTableAdmin(admin.ModelAdmin):
    list_display = ('color_id','background_color_hex','background_color','text_color_hex')
    list_filter = ('color_id','background_color_hex','background_color','text_color_hex')

class MenuSystemTableAdmin(admin.ModelAdmin):
    list_display = ('html','icon','action','parent_id','security_groups','value')
    list_filter = ()


admin.site.register(Building,BuildingTableAdmin)
admin.site.register(BuildingItem,BuildingItemTableAdmin)
admin.site.register(BuildingSelectionList,BuildingSelectionListTableAdmin)
admin.site.register(BuildingSelectionListItem,BuildingSelectionListItemTableAdmin)
admin.site.register(Project,ProjectTableAdmin)
admin.site.register(ProjectSelectionList,ProjectSelectionListTableAdmin)
admin.site.register(ProjectSelectionListItem,ProjectSelectionListItemTableAdmin)
admin.site.register(SkillsKeywords,SkillsKeywordsTableAdmin)
admin.site.register(Task,TaskTableAdmin)
admin.site.register(File,FileTableAdmin)
admin.site.register(NonWorkingDays,NonWorkingDaysTableAdmin)
admin.site.register(Organization,OrganizationTableAdmin)
admin.site.register(People,PeopleTableAdmin)
admin.site.register(SupportRequest,SupportRequestTableAdmin)
admin.site.register(View,ViewTableAdmin)
admin.site.register(ViewField,ViewFieldTableAdmin)
admin.site.register(ColorMaster,ColorMasterTableAdmin)
admin.site.register(MenuSystem,MenuSystemTableAdmin)
