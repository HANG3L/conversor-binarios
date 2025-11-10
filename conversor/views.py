from django.shortcuts import render
from .forms import BinarioForm

def convertir_binario(request):
    resultado = None
    error = None

    if request.method == 'POST':
        form = BinarioForm(request.POST)
        if form.is_valid():
            binario = form.cleaned_data['numero_binario']
            try:
                #Conversiones
                decimal = int(binario, 2)
                octal = oct(decimal)[2:]
                hexadecimal = hex(decimal)[2:].upper()
                resultado = {
                    'decimal': decimal,
                    'octal': octal,
                    'hexadecimal': hexadecimal
                }
            except ValueError:
                error = "Error al convertir el número"
    else:
        form = BinarioForm()

    return render(request, 'index.html', {
        'form': form,
        'resultado': resultado,
        'error': error
    })