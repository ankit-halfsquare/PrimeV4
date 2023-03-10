# Generated by Django 3.2 on 2023-01-19 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230119_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=50, null=True)),
                ('name_first', models.CharField(blank=True, max_length=50, null=True)),
                ('name_last', models.CharField(blank=True, max_length=50, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('universal_project_controller', models.CharField(blank=True, max_length=4, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('active', models.SmallIntegerField(blank=True, null=True)),
                ('email_verification', models.SmallIntegerField(blank=True, null=True)),
                ('email_verification_code', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.IntegerField(blank=True, null=True)),
                ('organization_id', models.IntegerField(blank=True, null=True)),
                ('role_primary', models.CharField(blank=True, max_length=50, null=True)),
                ('resume_file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('current_latest_company', models.CharField(blank=True, max_length=50, null=True)),
                ('current_latest_position', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('skills_keywords', models.CharField(blank=True, max_length=50, null=True)),
                ('obsolete', models.SmallIntegerField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('login_disabled', models.SmallIntegerField(blank=True, null=True)),
                ('project_membership', models.CharField(blank=True, max_length=255, null=True)),
                ('project_membership_json', models.TextField(blank=True, null=True)),
                ('ux_memory', models.TextField(blank=True, null=True)),
                ('task_datatable_view_id', models.IntegerField(blank=True, null=True)),
                ('current_project_id', models.IntegerField(blank=True, null=True)),
                ('history_comments', models.TextField(blank=True, null=True)),
                ('pref_datatable_width', models.IntegerField(blank=True, null=True)),
                ('pref_datatable_height', models.IntegerField(blank=True, null=True)),
                ('app_item_project_id', models.IntegerField(blank=True, null=True)),
                ('app_item_view_id', models.IntegerField(blank=True, null=True)),
                ('app_building_view_id', models.IntegerField(blank=True, null=True)),
                ('app_building_item_selected_building_id', models.IntegerField(blank=True, null=True)),
                ('app_building_item_selected_view_id', models.IntegerField(blank=True, null=True)),
                ('app_task_selected_project_id', models.IntegerField(blank=True, null=True)),
                ('app_task_selected_view_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='building',
            name='create_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='create_by_user', to='core.user'),
        ),
        migrations.AlterField(
            model_name='building',
            name='update_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_by_user', to='core.user'),
        ),
    ]
