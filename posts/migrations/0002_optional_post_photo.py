from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('posts', '0001_initial')]
    operations = [migrations.AlterField(model_name='post', name='image', field=models.ImageField(blank=True, default='', upload_to='images/'))]
