from django.utils.html import format_html, format_html_join
from django.forms.util import ErrorList


class ErrorListOmi(ErrorList):
    """
    Add's bootstrapped error paragraph
    """
    def as_p(self):
        return format_html(
            '<p class="text-warning">{}</p>'.format(
                '<br />'.join(self)))

    def __str__(self):
        return self.as_p()
