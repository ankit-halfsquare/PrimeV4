from django.db import models

# Create your models here.


class User(models.Model):
    name_first = models.CharField(max_length=50, blank=True, null=True)
    name_last = models.CharField(max_length=50, blank=True, null=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    universal_project_controller = models.CharField(max_length=4, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    email_verification = models.SmallIntegerField(blank=True, null=True)
    email_verification_code = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    # create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='create_by_user')
    update_date = models.DateTimeField(blank=True, null=True)
    # update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='update_by_user')
    organization = models.ForeignKey('Organization',models.DO_NOTHING,blank=True, null=True)
    role_primary = models.CharField(max_length=50, blank=True, null=True)
    resume_file_name = models.CharField(max_length=50, blank=True, null=True)
    current_latest_company = models.CharField(max_length=50, blank=True, null=True)
    current_latest_position = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    skills_keywords = models.CharField(max_length=50, blank=True, null=True)
    obsolete = models.BooleanField(default=False)
    code = models.CharField(max_length=50, blank=True, null=True)
    login_disabled = models.SmallIntegerField(blank=True, null=True)
    project_membership = models.CharField(max_length=255, blank=True, null=True)
    project_membership_json = models.TextField(blank=True, null=True)
    ux_memory = models.TextField(blank=True, null=True)
    task_datatable_view_id = models.IntegerField(blank=True, null=True)
    current_project_id = models.IntegerField(blank=True, null=True)
    history_comments = models.TextField(blank=True, null=True)
    pref_datatable_width = models.IntegerField(blank=True, null=True)
    pref_datatable_height = models.IntegerField(blank=True, null=True)
    app_item_project_id = models.IntegerField(blank=True, null=True)
    app_item_view_id = models.IntegerField(blank=True, null=True)
    app_building_view_id = models.IntegerField(blank=True, null=True)
    app_building_item_selected_building_id = models.IntegerField(blank=True, null=True)
    app_building_item_selected_view_id = models.IntegerField(blank=True, null=True)
    app_task_selected_project_id = models.IntegerField(blank=True, null=True)
    app_task_selected_view_id = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.name_first} {self.name_last}"
 



class Organization(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    organization_administrator = models.IntegerField(blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='organization_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='organization_updated_by')
    active = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"



class People(models.Model):
    name_first = models.CharField(max_length=50, blank=True, null=True)
    name_last = models.CharField(max_length=50, blank=True, null=True)
    resume_file_name = models.CharField(max_length=50, blank=True, null=True)
    current_latest_position = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    skills_keywords = models.CharField(max_length=255, blank=True, null=True)
    obsolete = models.BooleanField(default=False)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='people_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='people_updated_by')
   
    organization = models.ForeignKey(Organization,models.DO_NOTHING,blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    history_comments = models.TextField(blank=True, null=True)
    current_latest_company = models.CharField(max_length=255, blank=True, null=True)

  


class Building(models.Model):
    organization = models.ForeignKey(Organization,models.DO_NOTHING,blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_created_by')
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_updated_by')
    obsolete = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    ta1_alias = models.CharField(max_length=255, blank=True, null=True)
    ta2_alias = models.CharField(max_length=255, blank=True, null=True)
    ta3_alias = models.CharField(max_length=255, blank=True, null=True)
    ta4_alias = models.CharField(max_length=255, blank=True, null=True)
    ta5_alias = models.CharField(max_length=255, blank=True, null=True)
    ta6_alias = models.CharField(max_length=255, blank=True, null=True)
    ta7_alias = models.CharField(max_length=255, blank=True, null=True)
    ta8_alias = models.CharField(max_length=255, blank=True, null=True)
    ta9_alias = models.CharField(max_length=255, blank=True, null=True)
    ta10_alias = models.CharField(max_length=255, blank=True, null=True)
    ta11_alias = models.CharField(max_length=255, blank=True, null=True)
    ta12_alias = models.CharField(max_length=255, blank=True, null=True)
    ta13_alias = models.CharField(max_length=255, blank=True, null=True)
    ta14_alias = models.CharField(max_length=255, blank=True, null=True)
    ta15_alias = models.CharField(max_length=255, blank=True, null=True)
    ta16_alias = models.CharField(max_length=255, blank=True, null=True)
    ta17_alias = models.CharField(max_length=255, blank=True, null=True)
    ta18_alias = models.CharField(max_length=255, blank=True, null=True)
    ta19_alias = models.CharField(max_length=255, blank=True, null=True)
    ta20_alias = models.CharField(max_length=255, blank=True, null=True)
    sl1_alias = models.CharField(max_length=255, blank=True, null=True)
    sl1_list = models.IntegerField(blank=True, null=True)
    sl2_alias = models.CharField(max_length=255, blank=True, null=True)
    sl2_list = models.IntegerField(blank=True, null=True)
    sl3_alias = models.CharField(max_length=255, blank=True, null=True)
    sl3_list = models.IntegerField(blank=True, null=True)
    sl4_alias = models.CharField(max_length=255, blank=True, null=True)
    sl4_list = models.IntegerField(blank=True, null=True)
    sl5_alias = models.CharField(max_length=255, blank=True, null=True)
    sl5_list = models.IntegerField(blank=True, null=True)
    sl6_alias = models.CharField(max_length=255, blank=True, null=True)
    sl6_list = models.IntegerField(blank=True, null=True)
    sl7_alias = models.CharField(max_length=255, blank=True, null=True)
    sl7_list = models.IntegerField(blank=True, null=True)
    sl8_alias = models.CharField(max_length=255, blank=True, null=True)
    sl8_list = models.IntegerField(blank=True, null=True)
    sl9_alias = models.CharField(max_length=255, blank=True, null=True)
    sl9_list = models.IntegerField(blank=True, null=True)
    sl10_alias = models.CharField(max_length=255, blank=True, null=True)
    sl10_list = models.IntegerField(blank=True, null=True)
    sl11_alias = models.CharField(max_length=255, blank=True, null=True)
    sl11_list = models.IntegerField(blank=True, null=True)
    sl12_alias = models.CharField(max_length=255, blank=True, null=True)
    sl12_list = models.IntegerField(blank=True, null=True)
    sl13_alias = models.CharField(max_length=255, blank=True, null=True)
    sl13_list = models.IntegerField(blank=True, null=True)
    sl14_alias = models.CharField(max_length=255, blank=True, null=True)
    sl14_list = models.IntegerField(blank=True, null=True)
    sl15_alias = models.CharField(max_length=255, blank=True, null=True)
    sl15_list = models.IntegerField(blank=True, null=True)
    sl16_alias = models.CharField(max_length=255, blank=True, null=True)
    sl16_list = models.IntegerField(blank=True, null=True)
    sl17_alias = models.CharField(max_length=255, blank=True, null=True)
    sl17_list = models.IntegerField(blank=True, null=True)
    sl18_alias = models.CharField(max_length=255, blank=True, null=True)
    sl18_list = models.IntegerField(blank=True, null=True)
    sl19_alias = models.CharField(max_length=255, blank=True, null=True)
    sl19_list = models.IntegerField(blank=True, null=True)
    sl20_alias = models.CharField(max_length=255, blank=True, null=True)
    sl20_list = models.IntegerField(blank=True, null=True)
    zip = models.CharField(max_length=128, blank=True, null=True)
    guid = models.CharField(max_length=36, blank=True, null=True)





class BuildingItem(models.Model):
    building = models.ForeignKey(Building,models.DO_NOTHING,blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    parent_building_item = models.IntegerField(blank=True, null=True)
    people = models.ForeignKey(People,on_delete=models.DO_NOTHING,  blank=True, null=True)
    code = models.CharField(max_length=788, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    ta1 = models.CharField(max_length=768, blank=True, null=True)
    ta2 = models.CharField(max_length=768, blank=True, null=True)
    ta3 = models.CharField(max_length=768, blank=True, null=True)
    ta4 = models.CharField(max_length=768, blank=True, null=True)
    ta5 = models.CharField(max_length=768, blank=True, null=True)
    ta6 = models.CharField(max_length=768, blank=True, null=True)
    ta7 = models.CharField(max_length=768, blank=True, null=True)
    ta8 = models.CharField(max_length=768, blank=True, null=True)
    ta9 = models.CharField(max_length=768, blank=True, null=True)
    ta10 = models.CharField(max_length=768, blank=True, null=True)
    ta11 = models.CharField(max_length=768, blank=True, null=True)
    ta12 = models.CharField(max_length=768, blank=True, null=True)
    ta13 = models.CharField(max_length=768, blank=True, null=True)
    ta14 = models.CharField(max_length=768, blank=True, null=True)
    ta15 = models.CharField(max_length=768, blank=True, null=True)
    ta16 = models.CharField(max_length=768, blank=True, null=True)
    ta17 = models.CharField(max_length=768, blank=True, null=True)
    ta18 = models.CharField(max_length=768, blank=True, null=True)
    ta19 = models.CharField(max_length=768, blank=True, null=True)
    ta20 = models.CharField(max_length=768, blank=True, null=True)
    sl1 = models.IntegerField(blank=True, null=True)
    sl2 = models.IntegerField(blank=True, null=True)
    sl3 = models.IntegerField(blank=True, null=True)
    sl4 = models.IntegerField(blank=True, null=True)
    sl5 = models.IntegerField(blank=True, null=True)
    sl6 = models.IntegerField(blank=True, null=True)
    sl7 = models.IntegerField(blank=True, null=True)
    sl8 = models.IntegerField(blank=True, null=True)
    sl9 = models.IntegerField(blank=True, null=True)
    sl10 = models.IntegerField(blank=True, null=True)
    sl11 = models.IntegerField(blank=True, null=True)
    sl12 = models.IntegerField(blank=True, null=True)
    sl13 = models.IntegerField(blank=True, null=True)
    sl14 = models.IntegerField(blank=True, null=True)
    sl15 = models.IntegerField(blank=True, null=True)
    sl16 = models.IntegerField(blank=True, null=True)
    sl17 = models.IntegerField(blank=True, null=True)
    sl18 = models.IntegerField(blank=True, null=True)
    sl19 = models.IntegerField(blank=True, null=True)
    sl20 = models.IntegerField(blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_item_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_item_updated_by')
    guid = models.CharField(max_length=36, blank=True, null=True)
    additional_data_type_form_instance_id = models.IntegerField(blank=True, null=True)
    additional_data_type_form_name = models.CharField(max_length=255, blank=True, null=True)
    building_item_category_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'core_building_item'

    


class BuildingSelectionList(models.Model):
    building = models.ForeignKey(Building,models.DO_NOTHING,blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_selection_list_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_selection_list_updated_by')
    obsolete = models.BooleanField(default=False)

   



class BuildingSelectionListItem(models.Model):
    building_selection_list = models.ForeignKey(BuildingSelectionList,models.DO_NOTHING,blank=True, null=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    code = models.CharField(max_length=125, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_selection_list_item_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='building_selection_list_item_updated_by')
    obsolete = models.BooleanField(default=False)

    




class Project(models.Model):
    organization = models.ForeignKey(Organization,models.DO_NOTHING,blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    project_administrator_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    revenue = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    margin = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_updated_by')
    obsolete = models.BooleanField(default=False)
    item_name_track = models.CharField(max_length=10, blank=True, null=True)
    item_name_order = models.CharField(max_length=50, blank=True, null=True)
    item_name_table = models.CharField(max_length=10, blank=True, null=True)
    item_name_alias = models.CharField(max_length=50, blank=True, null=True)
    ta1_alias = models.CharField(max_length=50, blank=True, null=True)
    ta2_alias = models.CharField(max_length=50, blank=True, null=True)
    ta3_alias = models.CharField(max_length=50, blank=True, null=True)
    ta4_alias = models.CharField(max_length=50, blank=True, null=True)
    ta5_alias = models.CharField(max_length=50, blank=True, null=True)
    sl1_list = models.IntegerField(blank=True, null=True)
    sl1_alias = models.CharField(max_length=50, blank=True, null=True)
    sl2_list = models.IntegerField(blank=True, null=True)
    sl2_alias = models.CharField(max_length=50, blank=True, null=True)
    sl3_list = models.IntegerField(blank=True, null=True)
    sl3_alias = models.CharField(max_length=50, blank=True, null=True)
    sl4_list = models.IntegerField(blank=True, null=True)
    sl4_alias = models.CharField(max_length=50, blank=True, null=True)
    sl5_list = models.IntegerField(blank=True, null=True)
    sl5_alias = models.CharField(max_length=50, blank=True, null=True)
    customization = models.TextField(blank=True, null=True)
    role_management = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    customer_feedback = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    building = models.ForeignKey(Building,models.DO_NOTHING,blank=True, null=True)





class ProjectSelectionList(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_selection_list_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_selection_list_updated_by')
    obsolete = models.BooleanField(default=False)

  


class ProjectSelectionListItem(models.Model):
    project_selection_list = models.ForeignKey(ProjectSelectionList, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    code = models.CharField(max_length=125, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_selection_list_item_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='project_selection_list_item_updated_by')
    obsolete = models.BooleanField(default=False)



class SkillsKeywords(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='skills_keywords_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='skills_keywords_updated_by')
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)




class Task(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    assignees = models.CharField(max_length=125, blank=True, null=True)
    task_order_within_project = models.CharField(max_length=125, blank=True, null=True)
    task = models.CharField(max_length=768, blank=True, null=True)
    task_group_order_within_project = models.FloatField(blank=True, null=True)
    task_group_id = models.IntegerField(blank=True, null=True)
    prerequisite_status = models.CharField(max_length=50, blank=True, null=True)
    task_parent_id = models.IntegerField(blank=True, null=True)
    start_days_prior_to_parent_plan_stop_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stop_days_prior_to_parent_plan_stop_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_days_prior_to_parent_plan_start_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stop_days_prior_to_parent_plan_start_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    milestone_id = models.IntegerField(blank=True, null=True)
    start_days_prior_to_milestone_plan_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stop_days_prior_to_milestone_plan_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    task_planning_group_id_1 = models.IntegerField(blank=True, null=True)
    task_planning_group_id_2 = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    additional_data_type_form_id = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    plan_start_date = models.DateField(blank=True, null=True)
    plan_start_ww = models.CharField(max_length=10, blank=True, null=True)
    plan_start_month = models.CharField(max_length=10, blank=True, null=True)
    forecast_start_date = models.DateField(blank=True, null=True)
    forecast_start_ww = models.CharField(max_length=10, blank=True, null=True)
    forecast_start_month = models.CharField(max_length=10, blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    actual_start_ww = models.CharField(max_length=10, blank=True, null=True)
    actual_start_month = models.CharField(max_length=10, blank=True, null=True)
    plan_stop_date = models.DateField(blank=True, null=True)
    plan_stop_ww = models.CharField(max_length=10, blank=True, null=True)
    plan_stop_month = models.CharField(max_length=10, blank=True, null=True)
    forecast_stop_date = models.DateField(blank=True, null=True)
    forecast_stop_ww = models.CharField(max_length=10, blank=True, null=True)
    forecast_stop_month = models.CharField(max_length=10, blank=True, null=True)
    actual_stop_date = models.DateField(blank=True, null=True)
    actual_stop_ww = models.CharField(max_length=10, blank=True, null=True)
    actual_stop_month = models.CharField(max_length=10, blank=True, null=True)
    priority_importance_definition = models.CharField(max_length=50, blank=True, null=True)
    priority_importance = models.CharField(max_length=50, blank=True, null=True)
    duration_unit = models.CharField(max_length=50, blank=True, null=True)
    plan_duration = models.CharField(max_length=50, blank=True, null=True)
    actual_duration = models.CharField(max_length=50, blank=True, null=True)
    cost_unit = models.CharField(max_length=50, blank=True, null=True)
    plan_cost = models.CharField(max_length=50, blank=True, null=True)
    actual_cost = models.CharField(max_length=50, blank=True, null=True)
    difficulty_definition = models.CharField(max_length=50, blank=True, null=True)
    plan_difficulty = models.CharField(max_length=50, blank=True, null=True)
    actual_difficulty = models.CharField(max_length=50, blank=True, null=True)
    labor_unit = models.CharField(max_length=50, blank=True, null=True)
    plan_labor_time = models.CharField(max_length=50, blank=True, null=True)
    plan_labor_qty = models.CharField(max_length=50, blank=True, null=True)
    plan_labor = models.CharField(max_length=50, blank=True, null=True)
    actual_labor_time = models.CharField(max_length=50, blank=True, null=True)
    actual_labor_qty = models.CharField(max_length=50, blank=True, null=True)
    actual_labor = models.CharField(max_length=50, blank=True, null=True)
    delivery_committed_to = models.CharField(max_length=50, blank=True, null=True)
    on_time_delivery = models.CharField(max_length=50, blank=True, null=True)
    otd_variance_details = models.CharField(max_length=50, blank=True, null=True)
    otd_variance_category = models.CharField(max_length=50, blank=True, null=True)
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    task_status = models.CharField(max_length=50, blank=True, null=True)
    approval_disapproval_date = models.DateField(blank=True, null=True)
    approval_disapprover_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    spare1 = models.TextField(blank=True, null=True)
    spare2 = models.TextField(blank=True, null=True)
    spare3 = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=788, blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    prerequisite_id = models.IntegerField(blank=True, null=True)
    people_id = models.IntegerField(blank=True, null=True)
    task_parent_name = models.CharField(max_length=768, blank=True, null=True)
    position_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='task_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='task_updated_by')
    additional_data_type_form_instance_id = models.IntegerField(blank=True, null=True)
    additional_data_type_form_name = models.CharField(max_length=255, blank=True, null=True)
    obsolete = models.BooleanField(default=False)
    project_position_assignee_id = models.IntegerField(blank=True, null=True)
    project_role_id = models.IntegerField(blank=True, null=True)
    ta1 = models.CharField(max_length=255, blank=True, null=True)
    ta2 = models.CharField(max_length=255, blank=True, null=True)
    ta3 = models.CharField(max_length=255, blank=True, null=True)
    ta4 = models.CharField(max_length=255, blank=True, null=True)
    ta5 = models.CharField(max_length=255, blank=True, null=True)
    sl1 = models.IntegerField(blank=True, null=True)
    sl2 = models.IntegerField(blank=True, null=True)
    sl3 = models.IntegerField(blank=True, null=True)
    sl4 = models.IntegerField(blank=True, null=True)
    sl5 = models.IntegerField(blank=True, null=True)
    task_details = models.CharField(max_length=1024, blank=True, null=True)
    days_required_to_complete = models.IntegerField(blank=True, null=True)

    


class File(models.Model):
    table_key = models.IntegerField(blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    file_type = models.CharField(max_length=256, blank=True, null=True)
    file_name = models.CharField(max_length=512, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='file_created_by')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='file_updated_by')
    obsolete = models.BooleanField(default=False)
    building = models.ForeignKey(Building,models.DO_NOTHING,blank=True, null=True)

  



class NonWorkingDays(models.Model):
    obsolete = models.BooleanField(default=False)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='non_working_days_created_by_user')
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User,models.DO_NOTHING,blank=True, null=True,related_name='non_working_days_updated_by_user')
    # project_id = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    value_day = models.CharField(max_length=50, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    day_or_date = models.CharField(max_length=4, blank=True, null=True)
    value_display = models.CharField(max_length=50, blank=True, null=True)

    




class SupportRequest(models.Model):
    comment = models.TextField(blank=True, null=True)  # This field type is a guess.
    component = models.CharField(max_length=255, blank=True, null=True)
    userid = models.CharField(max_length=255, blank=True, null=True)
    request_datetime = models.DateField(blank=True, null=True)

  



class View(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    filter_sql = models.TextField(blank=True, null=True)
    filter_user_only = models.CharField(max_length=10, blank=True, null=True)
    enable_obsolete = models.BooleanField(default=False)
    enable_attach_files = models.SmallIntegerField(blank=True, null=True)
    enable_add_children = models.SmallIntegerField(blank=True, null=True)
    enable_add_constraint = models.SmallIntegerField(blank=True, null=True)
    enable_clone_task = models.SmallIntegerField(blank=True, null=True)
    obsolete = models.BooleanField(default=False)
    enable_item_null = models.SmallIntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    parent_app = models.CharField(max_length=255, blank=True, null=True)
    view_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    default_sort = models.CharField(max_length=255, blank=True, null=True)
    building = models.ForeignKey(Building,models.DO_NOTHING,blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)
    enable_add_link = models.SmallIntegerField(blank=True, null=True)
    filter_conditions = models.TextField(blank=True, null=True)  # This field type is a guess.
    enable_clone_item = models.SmallIntegerField(blank=True, null=True)

    


class ViewField(models.Model):
    column_name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    column_width = models.IntegerField(blank=True, null=True)
    column_order = models.IntegerField(blank=True, null=True)
    visible = models.SmallIntegerField(blank=True, null=True)
    cssformat = models.CharField(db_column='cssFormat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    column_system_name = models.CharField(max_length=255, blank=True, null=True)
    column_view_name = models.CharField(max_length=255, blank=True, null=True)
    column_sort_method = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(max_length=255, blank=True, null=True)
    field_selection_list = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey(View, models.DO_NOTHING, blank=True, null=True)
    form_visible = models.SmallIntegerField(blank=True, null=True)
    form_enabled = models.SmallIntegerField(blank=True, null=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    hidden = models.SmallIntegerField(blank=True, null=True)
    filter_visible = models.SmallIntegerField(blank=True, null=True)
    view_editor_enabled = models.SmallIntegerField(blank=True, null=True)
    excel_filter = models.SmallIntegerField(blank=True, null=True)

    

class ColorMaster(models.Model):
    color_id = models.CharField(max_length=255, blank=True, null=True)
    background_color_hex = models.CharField(max_length=255, blank=True, null=True)
    background_color = models.CharField(max_length=255, blank=True, null=True)
    text_color_hex = models.CharField(max_length=255, blank=True, null=True)
    text_color = models.CharField(max_length=255, blank=True, null=True)



class MenuSystem(models.Model):
    html = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    security_groups = models.CharField(max_length=1024, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    js_function = models.CharField(max_length=512, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    opened = models.BooleanField(blank=True, null=True)

   






