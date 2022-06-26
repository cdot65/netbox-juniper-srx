# Generated by Django 4.0.4 on 2022-06-24 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0007_contact_link'),
        ('dcim', '0153_created_datetimefield'),
        ('netbox_juniper_srx', '0002_alter_securitypolicy_default_action_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitypolicy',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='securitypolicy',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.device'),
        ),
        migrations.AddField(
            model_name='securitypolicy',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.site'),
        ),
        migrations.AddField(
            model_name='securitypolicy',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='securitypolicyrule',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.device'),
        ),
        migrations.AddField(
            model_name='securitypolicyrule',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.site'),
        ),
        migrations.AddField(
            model_name='securitypolicyrule',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tenancy.tenant'),
        ),
        migrations.AlterField(
            model_name='securitypolicyrule',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
