from django import forms

class BinarioForm(forms.Form):
    numero_binario = forms.CharField(
        label='Número Binario',
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 1010'})
    )

    def clean_numero_binario(self):
        data = self.cleaned_data['numero_binario']
        if not all(c in '01' for c in data):
            raise forms.ValidationError("El número debe contener solo 0 y 1")
        return data