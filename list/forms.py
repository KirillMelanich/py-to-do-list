from django import forms
from tempus_dominus.widgets import DateTimePicker

from list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'done', 'tag']

    widgets = {
        'deadline': DateTimePicker(
            options={
                'useCurrent': True,
                'sideBySide': True,
                'icons': {
                    'time': 'fa fa-clock',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-calendar-check-o',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times'
                }
            },
            attrs={
                'append': 'fa fa-calendar',
                'input_toggle': True,
                'input_group': True,
            },
        ),
    }

