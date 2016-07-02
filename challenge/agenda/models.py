from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_name(value):
    name = str(value)
    name = name.split();
    if len(name) == 1:
        raise ValidationError(
            _('O nome precisa ter, no minimo, duas palavras')
        )
    for word in name:
        if len(word)<2:
            raise ValidationError(
            _('Cada palavra que compoe o nome deve ter ao menos duas letras')
            )

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=42,validators=[validate_name])
    email = models.EmailField(max_length = 320, unique=True,  error_messages={'unique':"Ja existe um usuario com este email"})

    def __unicode__(self):
        return self.name

