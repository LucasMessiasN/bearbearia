from django import forms
from .models import Cliente, Barbeiro, Atendimento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CadastroFuncionarioForm(UserCreationForm):
    OPCOES_CARGO = (
        ('Atendente', 'Atendente'),
        ('Administrativo', 'Gerência/Administrativo'),
    )
    cargo = forms.ChoiceField(choices=OPCOES_CARGO, label='Cargo do Funcionario')

    class Meta(UserCreationForm.Meta):
        model = User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class BarbeiroForm(forms.ModelForm):
    class Meta:
        model = Barbeiro
        fields = ['nome_barbeiro', 'email', 'telefone']

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['cliente_atendimento', 'barbeiro_atendimento', 'data_hora']

        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }