from django import forms
from .models import IVFCycle, StimulationDay, EggRetrieval, EmbryoTransfer

class IVFCycleForm(forms.ModelForm):
    class Meta:
        model = IVFCycle
        fields = ['couple', 'protocol', 'start_date', 'notes']

class StimulationDayForm(forms.ModelForm):
    class Meta:
        model = StimulationDay
        fields = "__all__"

class EggRetrievalForm(forms.ModelForm):
    class Meta:
        model = EggRetrieval
        fields = "__all__"

class EmbryoTransferForm(forms.ModelForm):
    class Meta:
        model = EmbryoTransfer
        fields = "__all__"