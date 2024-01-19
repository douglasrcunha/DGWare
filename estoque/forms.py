from django.forms import ModelForm
from .models import Produto
#from .models import Usuario

class ProdutoForm(ModelForm):
    class Meta: 
        model = Produto
        fields = '__all__'
