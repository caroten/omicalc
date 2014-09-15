from django.db import models


class PrintFormat(models.Model):
    """Форматы печати"""
    name = models.CharField('Название', max_length=16)
    denominator = models.IntegerField(
        'Знаменатель',
        help_text='Знаменатель для получения количества полос из условного А1')

    def __str__(self):
        return '{}/{}'.format(self.name, self.denominator)

    class Meta:
        ordering = ['denominator']
        verbose_name = 'Формат печати'
        verbose_name_plural = 'Форматы печати'


class CirculationLimit(models.Model):
    """Пороги тиража при которых меняются нормы отходов"""
    limit = models.IntegerField(unique=True)

    def __str__(self):
        other = type(self).objects.filter(limit__gt=self.limit).first()
        if other:
            if self.limit:
                return 'от {} до {}'.format(self.limit, other.limit)
            else:
                return 'менее {}'.format(other.limit)
        else:
            return 'свыше {}'.format(self.limit)

    @classmethod
    def get_limit(cls, value):
        return cls.objects.filter(limit__lt=value).last()

    class Meta:
        ordering = ['limit']
        verbose_name = 'Ограничение тиража'
        verbose_name_plural = 'Ограничения тиража'


class InkFaceBack(models.Model):
    face = models.IntegerField()
    back = models.IntegerField()

    values = models.ManyToManyField(CirculationLimit,
                                    through='WasteRatio')

    def __str__(self):
        return '{}+{}'.format(self.face, self.back)

    def plates_count(self):
        return self.face + self.back

    class Meta:
        ordering = ['face', 'back']
        verbose_name = 'Красочность'
        verbose_name_plural = 'Красочность'


class WasteRatio(models.Model):
    limit = models.ForeignKey('CirculationLimit')
    ink = models.ForeignKey('InkFaceBack')
    value = models.IntegerField('Норматив')

    def __str__(self):
        return '{} ({}) - {}'.format(self.limit, self.ink, self.value)

    class Meta:
        verbose_name = 'Норма отходов'
        verbose_name_plural = 'Нормы отходов'


class PubSquare(models.Model):
    """Площадь издания"""
    value = models.IntegerField('Площадь издания')

    def __str__(self):
        return '[{}]'.format(self.value)
