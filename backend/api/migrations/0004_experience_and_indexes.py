from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_skill_options_remove_skill_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, help_text='Leave blank for a current position', null=True)),
                ('technologies', models.JSONField(blank=True, default=list, help_text='List of technologies used in this role')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('order', models.PositiveIntegerField(default=0, help_text='Display order (lower numbers first)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order', '-start_date'],
            },
        ),
        migrations.AddIndex(
            model_name='education',
            index=models.Index(fields=['order', '-start_date'], name='api_educati_order_a846a1_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['order', '-created_at'], name='api_project_order_b45312_idx'),
        ),
        migrations.AddIndex(
            model_name='skill',
            index=models.Index(fields=['order'], name='api_skill_order_22633d_idx'),
        ),
        migrations.AddIndex(
            model_name='experience',
            index=models.Index(fields=['order', '-start_date'], name='api_experie_order_755e58_idx'),
        ),
    ]
