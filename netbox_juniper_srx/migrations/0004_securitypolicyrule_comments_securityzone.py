# Generated by Django 4.0.4 on 2022-06-26 11:37

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0153_created_datetimefield'),
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('tenancy', '0007_contact_link'),
        ('netbox_juniper_srx', '0003_securitypolicy_description_securitypolicy_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitypolicyrule',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='SecurityZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('comments', models.TextField(blank=True)),
                ('default_action', models.CharField(default='permit', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('app_tracking', models.BooleanField(default=False)),
                ('inbound_protocols', models.CharField(default='all', max_length=50)),
                ('inbound_services', models.CharField(default='all', max_length=50)),
                ('status', models.CharField(default='active', max_length=50)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.device')),
                ('match_interfaces', models.ManyToManyField(blank=True, related_name='+', to='dcim.interface')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.site')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
