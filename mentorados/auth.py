from .models import Mentorados

def valida_token(token):
    return Mentorados.objects.filter(token=token).first() #.first para pegar o mentorado pelo fato de retornar uma lista