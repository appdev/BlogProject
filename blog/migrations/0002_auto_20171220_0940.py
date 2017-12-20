# Generated by Django 2.0 on 2017-12-20 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=66, verbose_name='站点名称')),
                ('description', models.TextField(blank=True, max_length=150, verbose_name='站点说明')),
                ('userAvatar', models.ImageField(blank=True, null=True, upload_to='blog_image/%Y/%m/%d', verbose_name='用户头像')),
                ('UserName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '站点管理',
                'verbose_name': '文章',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time', 'title'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
