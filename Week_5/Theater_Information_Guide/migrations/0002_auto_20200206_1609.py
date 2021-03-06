# Generated by Django 3.0.2 on 2020-02-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Theater_Information_Guide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentid', models.AutoField(db_column='CommentID', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='Content', max_length=255, null=True)),
                ('reply', models.CharField(blank=True, db_column='Reply', max_length=255, null=True)),
                ('likes', models.IntegerField(blank=True, db_column='Likes', null=True)),
                ('image', models.TextField(blank=True, db_column='Image', null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theaters',
            fields=[
                ('theaterid', models.AutoField(db_column='TheaterID', primary_key=True, serialize=False)),
                ('theatername', models.CharField(db_column='TheaterName', max_length=50)),
                ('location', models.CharField(db_column='Location', max_length=50)),
                ('period', models.CharField(db_column='Period', max_length=50)),
                ('place', models.CharField(db_column='Place', max_length=50)),
                ('openingday', models.DateField(db_column='OpeningDay')),
                ('closingday', models.DateField(blank=True, db_column='ClosingDay', null=True)),
                ('openrun', models.CharField(blank=True, db_column='OpenRun', max_length=50, null=True)),
            ],
            options={
                'db_table': 'theaters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=50)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TheaterDetails',
        ),
        migrations.DeleteModel(
            name='TheaterDf',
        ),
        migrations.CreateModel(
            name='TheatersDetails',
            fields=[
                ('theaterid', models.OneToOneField(db_column='TheaterID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Theater_Information_Guide.Theaters')),
                ('viewingage', models.CharField(blank=True, db_column='ViewingAge', max_length=50, null=True)),
                ('performancetime', models.CharField(blank=True, db_column='PerformanceTime', max_length=50, null=True)),
                ('descriptions', models.CharField(blank=True, db_column='Descriptions', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, db_column='Price', decimal_places=0, max_digits=7, null=True)),
                ('shoptitle', models.CharField(blank=True, db_column='ShopTitle', max_length=50, null=True)),
                ('shoplink', models.TextField(blank=True, db_column='ShopLink', null=True)),
                ('image', models.CharField(blank=True, db_column='Image', max_length=255, null=True)),
            ],
            options={
                'db_table': 'theaters_details',
                'managed': False,
            },
        ),
    ]
