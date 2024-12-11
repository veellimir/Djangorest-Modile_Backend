from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    NEW_TASK = 0
    WORK_TASK = 1
    CHECK_TASK = 2
    END_TASK = 3

    STATUSES_TASKS = (
        (NEW_TASK, "Новая", ),
        (WORK_TASK, "В работе", ),
        (CHECK_TASK, "На проверке", ),
        (NEW_TASK, "Выполнено", ),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Исполнитель"
    )
    status_task = models.SmallIntegerField(
        default=NEW_TASK,
        choices=STATUSES_TASKS,
        verbose_name="Статус задачи",
    )
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описание задачи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")