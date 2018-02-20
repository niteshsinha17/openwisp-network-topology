# Generated by Django 2.0.2 on 2018-02-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0002_snapshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='status_changed',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='topology',
            name='parser',
            field=models.CharField(choices=[('netdiff.OlsrParser', 'OLSRd (txtinfo/jsoninfo)'), ('netdiff.BatmanParser', 'batman-advanced (jsondoc/txtinfo)'), ('netdiff.BmxParser', 'BMX6 (q6m)'), ('netdiff.NetJsonParser', 'NetJSON NetworkGraph'), ('netdiff.CnmlParser', 'CNML 1.0'), ('netdiff.OpenvpnParser', 'OpenVPN')], help_text='Select topology format', max_length=128, verbose_name='format'),
        ),
    ]
