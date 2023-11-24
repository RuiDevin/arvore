# Generated by Django 4.2.7 on 2023-11-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arvore", "0003_rename_endereço_trabalho_endereço_atual_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trabalho",
            name="endereço_atual",
        ),
        migrations.AddField(
            model_name="trabalho",
            name="endereco_atual",
            field=models.ManyToManyField(related_name="endereco_atual", to="arvore.endereco"),
        ),
        migrations.AddField(
            model_name="trabalho",
            name="recebo_salario_minimo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Salário Mínimo 1994", "70 Reais (1994)"),
                    ("Salário Mínimo 1995", "100 Reais (1995)"),
                    ("Salário Mínimo 1996", "112 Reais (1996)"),
                    ("Salário Mínimo 1997", "120 Reais (1997)"),
                    ("Salário Mínimo 1998", "130 Reais (1998)"),
                    ("Salário Mínimo 1999", "136 Reais (1999)"),
                    ("Salário Mínimo 2000", "151 Reais (2000)"),
                    ("Salário Mínimo 2001", "180 Reais (2001)"),
                    ("Salário Mínimo 2002", "200 Reais (2002)"),
                    ("Salário Mínimo 2003", "240 Reais (2003)"),
                    ("Salário Mínimo 2004", "260 Reais (2004)"),
                    ("Salário Mínimo 2005", "300 Reais (2005)"),
                    ("Salário Mínimo 2006", "350 Reais (2006)"),
                    ("Salário Mínimo 2007", "380 Reais (2007)"),
                    ("Salário Mínimo 2008", "415 Reais (2008)"),
                    ("Salário Mínimo 2009", "465 Reais (2009)"),
                    ("Salário Mínimo 2010", "510 Reais (2010)"),
                    ("Salário Mínimo 2011", "545 Reais (2011)"),
                    ("Salário Mínimo 2012", "622 Reais (2012)"),
                    ("Salário Mínimo 2013", "678 Reais (2013)"),
                    ("Salário Mínimo 2014", "724 Reais (2014)"),
                    ("Salário Mínimo 2015", "788 Reais (2015)"),
                    ("Salário Mínimo 2016", "880 Reais (2016)"),
                    ("Salário Mínimo 2017", "937 Reais (2017)"),
                    ("Salário Mínimo 2018", "954 Reais (2018)"),
                    ("Salário Mínimo 2019", "998 Reais (2019)"),
                    ("Salário Mínimo 2020", "1045 Reais (2020)"),
                    ("Salário Mínimo 2021", "1100 Reais (2021)"),
                    ("Salário Mínimo 2022", "1212 Reais (2022)"),
                    ("Salário Mínimo 2023", "1320 Reais (2023)"),
                ],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="trabalho",
            name="profissao_atual",
            field=models.ManyToManyField(related_name="sua_profissao_atual", to="arvore.profissao"),
        ),
        migrations.AlterField(
            model_name="trabalho",
            name="salario_atual",
            field=models.CharField(blank=True, choices=[], default=1320, max_length=25),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="AntigoTrabalho",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("salario", models.CharField(blank=True, choices=[], max_length=25)),
                (
                    "recebia_salario_minimo",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Salário Mínimo 1994", "70 Reais (1994)"),
                            ("Salário Mínimo 1995", "100 Reais (1995)"),
                            ("Salário Mínimo 1996", "112 Reais (1996)"),
                            ("Salário Mínimo 1997", "120 Reais (1997)"),
                            ("Salário Mínimo 1998", "130 Reais (1998)"),
                            ("Salário Mínimo 1999", "136 Reais (1999)"),
                            ("Salário Mínimo 2000", "151 Reais (2000)"),
                            ("Salário Mínimo 2001", "180 Reais (2001)"),
                            ("Salário Mínimo 2002", "200 Reais (2002)"),
                            ("Salário Mínimo 2003", "240 Reais (2003)"),
                            ("Salário Mínimo 2004", "260 Reais (2004)"),
                            ("Salário Mínimo 2005", "300 Reais (2005)"),
                            ("Salário Mínimo 2006", "350 Reais (2006)"),
                            ("Salário Mínimo 2007", "380 Reais (2007)"),
                            ("Salário Mínimo 2008", "415 Reais (2008)"),
                            ("Salário Mínimo 2009", "465 Reais (2009)"),
                            ("Salário Mínimo 2010", "510 Reais (2010)"),
                            ("Salário Mínimo 2011", "545 Reais (2011)"),
                            ("Salário Mínimo 2012", "622 Reais (2012)"),
                            ("Salário Mínimo 2013", "678 Reais (2013)"),
                            ("Salário Mínimo 2014", "724 Reais (2014)"),
                            ("Salário Mínimo 2015", "788 Reais (2015)"),
                            ("Salário Mínimo 2016", "880 Reais (2016)"),
                            ("Salário Mínimo 2017", "937 Reais (2017)"),
                            ("Salário Mínimo 2018", "954 Reais (2018)"),
                            ("Salário Mínimo 2019", "998 Reais (2019)"),
                            ("Salário Mínimo 2020", "1045 Reais (2020)"),
                            ("Salário Mínimo 2021", "1100 Reais (2021)"),
                            ("Salário Mínimo 2022", "1212 Reais (2022)"),
                            ("Salário Mínimo 2023", "1320 Reais (2023)"),
                        ],
                        max_length=25,
                    ),
                ),
                ("endereco", models.ManyToManyField(related_name="endereco", to="arvore.endereco")),
                ("profissao", models.ManyToManyField(related_name="sua_profissao", to="arvore.profissao")),
            ],
        ),
    ]
