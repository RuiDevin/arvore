# Generated by Django 4.2.7 on 2023-11-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arvore", "0007_irmaos_mae_irmaos_pai_primos_mae_primos_pai"),
    ]

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rua", models.CharField(max_length=255)),
                ("bairro", models.CharField(max_length=255)),
                ("numero", models.IntegerField(max_length=10)),
                ("cidade", models.CharField(max_length=255)),
                ("estado", models.CharField(max_length=255)),
                ("ponto_de_referencia", models.CharField(max_length=255)),
            ],
        ),
    ]