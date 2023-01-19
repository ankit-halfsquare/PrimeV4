# Generated by Django 3.2 on 2023-01-19 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_building_organization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildingitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='buildingselectionlist',
            name='building_id',
        ),
        migrations.RemoveField(
            model_name='buildingselectionlistitem',
            name='building_selection_list_id',
        ),
        migrations.RemoveField(
            model_name='file',
            name='building_id',
        ),
        migrations.RemoveField(
            model_name='people',
            name='organization_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='building_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='organization_id',
        ),
        migrations.RemoveField(
            model_name='projectselectionlistitem',
            name='project_selection_list_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='update_user',
        ),
        migrations.RemoveField(
            model_name='view',
            name='building_id',
        ),
        migrations.AddField(
            model_name='buildingselectionlist',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.building'),
        ),
        migrations.AddField(
            model_name='buildingselectionlistitem',
            name='building_selection_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.buildingselectionlist'),
        ),
        migrations.AddField(
            model_name='file',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.building'),
        ),
        migrations.AddField(
            model_name='people',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization'),
        ),
        migrations.AddField(
            model_name='project',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.building'),
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization'),
        ),
        migrations.AddField(
            model_name='projectselectionlistitem',
            name='project_selection_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.projectselectionlist'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.organization'),
        ),
        migrations.AddField(
            model_name='view',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='building',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='buildingselectionlist',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_selection_list_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='buildingselectionlist',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_selection_list_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='buildingselectionlistitem',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_selection_list_item_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='buildingselectionlistitem',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='building_selection_list_item_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='file',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='file',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='file_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='nonworkingdays',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='non_working_days_created_by_user', to='core.user'),
        ),
        migrations.AlterField(
            model_name='nonworkingdays',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='non_working_days_updated_by_user', to='core.user'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='people',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='people_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='people',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='people_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='project',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='projectselectionlist',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_selection_list_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='projectselectionlist',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_selection_list_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='projectselectionlistitem',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_selection_list_item_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='projectselectionlistitem',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_selection_list_item_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='skillskeywords',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='skills_keywords_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='skillskeywords',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='skills_keywords_updated_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_created_by', to='core.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_updated_by', to='core.user'),
        ),
    ]