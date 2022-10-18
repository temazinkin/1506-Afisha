from django.db.models import (
    Model,
    CharField,
    TextField,
    SlugField,
    BooleanField,
    DateTimeField,
)


class Event(Model):
    title = CharField(
        'название',
        max_length=200,
    )
    description = TextField(
        'описание',
        blank=True,
    )
    slug = SlugField(
        'URL',
    )
    date = DateTimeField(
        'дата события',
    )
    is_public = BooleanField(
        'опубликовано',
        default=True,
    )
    created = DateTimeField(
        'создано',
        auto_now_add=True,
    )
    updated = DateTimeField(
        'обновлено',
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'
