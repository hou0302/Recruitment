# Generated by Django 2.1.7 on 2019-08-30 01:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy', models.CharField(max_length=30, verbose_name='学院')),
            ],
            options={
                'verbose_name': '学院信息',
                'verbose_name_plural': '学院信息',
            },
        ),
        migrations.CreateModel(
            name='Freshman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstudent_id', models.CharField(max_length=11, verbose_name='学号')),
                ('password', models.CharField(max_length=25, verbose_name='密码')),
                ('newname', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(max_length=5, verbose_name='性别')),
                ('college', models.CharField(max_length=30, verbose_name='所属学院')),
                ('major', models.CharField(max_length=100, verbose_name='所属专业')),
                ('newclass', models.CharField(max_length=20, verbose_name='班级')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('qq', models.CharField(max_length=15, verbose_name='QQ号')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('direction', models.CharField(blank=True, choices=[('development', '开发'), ('design', '设计'), ('secretariat', '秘书处')], max_length=15, null=True, verbose_name='选择方向')),
                ('appointment_one', models.CharField(blank=True, max_length=60, null=True, verbose_name='预约时间一')),
                ('appointment_two', models.CharField(blank=True, max_length=60, null=True, verbose_name='预约时间二')),
                ('appointment_three', models.CharField(blank=True, max_length=60, null=True, verbose_name='预约时间三')),
                ('application', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='申请书')),
                ('interview_time', models.CharField(blank=True, max_length=60, null=True, verbose_name='面试时间')),
                ('interview_place', models.CharField(blank=True, max_length=50, null=True, verbose_name='面试地点')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='评分')),
                ('evaluate', models.TextField(blank=True, max_length=300, null=True, verbose_name='评价')),
                ('interview_result_A', models.BooleanField(blank=True, null=True, verbose_name='A轮面试结果')),
                ('interview_result_B', models.BooleanField(blank=True, null=True, verbose_name='B轮面试结果')),
                ('interview_id', models.CharField(blank=True, max_length=60, null=True, verbose_name='面试官')),
                ('province', models.CharField(blank=True, max_length=30, null=True, verbose_name='省份')),
                ('apartment', models.CharField(blank=True, max_length=25, null=True, verbose_name='宿舍楼')),
                ('dormitory', models.CharField(blank=True, max_length=25, null=True, verbose_name='宿舍号')),
                ('remark_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注1')),
                ('remark_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注2')),
                ('remark_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注3')),
            ],
            options={
                'verbose_name': '新生信息',
                'verbose_name_plural': '新生信息',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=30, verbose_name='专业')),
                ('majorAcademy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freshman.Academy', verbose_name='所属学院')),
            ],
            options={
                'verbose_name': '专业信息',
                'verbose_name_plural': '专业信息',
            },
        ),
    ]
