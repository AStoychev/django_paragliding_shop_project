import os

from django import forms

from paragliding_shop.equipment.models import Wings, Harness, Reserves, Instruments, Helmets


class WingBaseForm(forms.ModelForm):
    class Meta:
        model = Wings
        fields = ('manufacturer', 'model', 'image_url', 'price', 'en_certification', 'year', 'condition', 'test', 'porosity',)
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class CreateWingForm(WingBaseForm):
    pass


class EditWingForm(WingBaseForm):
    pass


class DeleteWingForm(WingBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Wings
        fields = "__all__"
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class HarnessBaseForm(forms.ModelForm):
    class Meta:
        model = Harness
        fields = ('manufacturer', 'model', 'image_url', 'price', 'category', 'year', 'condition',)
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class CreateHarnessesForm(HarnessBaseForm):
    pass


class EditHarnessesForm(HarnessBaseForm):
    pass


class DeleteHarnessForm(HarnessBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Harness
        fields = "__all__"


class ReservesBaseForm(forms.ModelForm):
    class Meta:
        model = Reserves
        fields = ('manufacturer', 'model', 'image_url', 'price', 'type', 'year', 'condition',)
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class CreateReservesForm(ReservesBaseForm):
    pass


class EditReservesForm(ReservesBaseForm):
    pass


class DeleteReservesForm(HarnessBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Reserves
        fields = "__all__"


class InstrumentsBaseForm(forms.ModelForm):
    class Meta:
        model = Instruments
        fields = ('manufacturer', 'image_url', 'price', 'type', 'condition',)
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class CreateInstrumentsForm(InstrumentsBaseForm):
    pass


class EditInstrumentsForm(InstrumentsBaseForm):
    pass


class DeleteInstrumentsForm(InstrumentsBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Instruments
        fields = "__all__"


class HelmetsBaseForm(forms.ModelForm):
    class Meta:
        model = Helmets
        fields = ('manufacturer', 'image_url', 'price', 'visor', 'condition',)
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            )}


class CreateHelmetsForm(HelmetsBaseForm):
    pass


class EditHelmetsForm(HelmetsBaseForm):
    pass


class DeleteHelmetsForm(HelmetsBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
