# Generated by Django 5.0.1 on 2024-02-06 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DeptName", models.CharField(max_length=25)),
            ],
            options={
                "db_table": "department",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Role", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "role",
            },
        ),
        migrations.CreateModel(
            name="ToDoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("DateCompleted", models.DateTimeField(auto_created=True)),
                ("Deadline", models.DateTimeField(auto_created=True)),
                ("Title", models.CharField(max_length=25)),
                ("Tags", models.CharField(max_length=255)),
                ("DateCreated", models.DateTimeField(auto_now_add=True)),
                ("Description", models.TextField(max_length=255)),
                (
                    "Status",
                    models.CharField(
                        choices=[
                            ("c", "completed"),
                            ("p", "pending"),
                            ("nt", "not started"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
            options={
                "db_table": "todolist",
            },
        ),
        migrations.CreateModel(
            name="Master",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=25)),
                ("IsActive", models.BooleanField(default=False)),
                (
                    "Role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="todo_app.role"
                    ),
                ),
            ],
            options={
                "db_table": "master",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ProfileImage",
                    models.FileField(default="avatar.png", upload_to="users/avatars"),
                ),
                ("FullName", models.CharField(blank=True, max_length=35, null=True)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("m", "male"), ("f", "female")], max_length=2
                    ),
                ),
                ("Dob", models.DateField()),
                (
                    "Phone",
                    models.CharField(blank=True, max_length=10, null=True, unique=True),
                ),
                ("Pincode", models.CharField(blank=True, max_length=5, null=True)),
                ("Languages", models.CharField(blank=True, max_length=35, null=True)),
                ("City", models.CharField(blank=True, max_length=35, null=True)),
                ("State", models.CharField(blank=True, max_length=35, null=True)),
                ("Address_1", models.CharField(blank=True, max_length=35, null=True)),
                ("Address_2", models.CharField(blank=True, max_length=35, null=True)),
                ("Country", models.CharField(blank=True, max_length=35, null=True)),
                ("Twitter", models.CharField(blank=True, max_length=35, null=True)),
                ("Instagram", models.CharField(blank=True, max_length=35, null=True)),
                ("Website", models.CharField(blank=True, max_length=35, null=True)),
                ("Facebook", models.CharField(blank=True, max_length=35, null=True)),
                (
                    "master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_app.master",
                    ),
                ),
            ],
            options={
                "db_table": "userprofile",
            },
        ),
        migrations.CreateModel(
            name="TaskAssociation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ToDoList",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_app.todolist",
                    ),
                ),
                (
                    "Member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_app.userprofile",
                    ),
                ),
            ],
            options={
                "db_table": "TaskAssociation",
            },
        ),
    ]
