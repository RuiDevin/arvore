# Generated by Django 4.2.7 on 2023-11-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arvore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Irmaos",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome_completo", models.CharField(max_length=255)),
                ("data_de_nascimento", models.DateField()),
                ("cidade_natal", models.CharField(max_length=255)),
            ],
        ),
    ]
