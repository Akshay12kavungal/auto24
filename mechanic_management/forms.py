from django import forms
from .models import Mechanic, MechanicWork

class UpdateWorkStatusForm(forms.ModelForm):
    class Meta:
        model = MechanicWork
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=MechanicWork._meta.get_field('status').choices),
        }
        
class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['profile_pic', 'address', 'mobile', 'skill', 'salary']