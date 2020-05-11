# Generated by Django 2.0.6 on 2018-12-29 00:15

from django.db import migrations
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0003_change_column_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='items',
            field=gm2m.fields.GM2MField('invoicing.Invoice', 'accounts.Team', 'board.Task', 'board.Inquiry', 'board.Announcement', 'chronicle.Event', 'directory.Company', 'directory.Carrier', 'directory.Activity', 'helpdesk.Article', 'logistics.Offer', 'logistics.Order', 'logistics.Option', 'logistics.ShippingOrder', related_name='exports_where_item', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk')),
        ),
    ]
