from django import forms
from .models import Mechanic, MechanicWork

class UpdateWorkStatusForm(forms.ModelForm):
    class Meta:
        model = MechanicWork
        fields = ['status', 'cost'] 
        widgets = {
            'status': forms.Select(choices=MechanicWork._meta.get_field('status').choices),
        }
    cost = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
        
class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['profile_pic', 'address', 'mobile', 'skill', 'salary']
