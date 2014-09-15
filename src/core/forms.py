from django import forms
from django.utils.html import format_html, format_html_join


class ErrorListBS(forms.utils.ErrorList):
    """
    Add's bootstrapped error paragraph
    """
    def as_p(self):
        return format_html(
            '<p class="text-warning">{}</p>'.format(
                '<br />'.join(self)))

    def __str__(self):
        return self.as_p()

class FormBS(forms.Form):
    """
    Bootstrapped form
    """
    def __init__(self, *args, **kwargs):
        if 'error_class' not in kwargs:
            kwargs['error_class'] = ErrorListBS
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            t = field.widget.attrs.get('class', '').split()
            field.widget.attrs['class'] = ' '.join(t + ['form-control'])
