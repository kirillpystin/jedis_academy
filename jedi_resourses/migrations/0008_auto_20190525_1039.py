# Generated by Django 2.1.7 on 2019-05-25 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("jedi_resourses", "0007_auto_20190525_1035")]

    operations = [
        migrations.RenameField(
            model_name="padawan", old_name="candidat", new_name="candidate"
        )
    ]