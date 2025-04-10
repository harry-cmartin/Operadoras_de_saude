from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Operadora
from .serializers import OperadoraSerializer

@api_view(['GET'])
def api_root(request):
    return Response({"message": "Funcionaanso"})

# Classe que implementa apenas o método GET 
class OperadoraViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Operadora.objects.all()
    serializer_class = OperadoraSerializer
    
    def get_queryset(self):
        queryset = Operadora.objects.all()
        search = self.request.query_params.get('search', None)
        
        if search:
            queryset = queryset.filter(
                Q(registro_ans__icontains=search) |
                Q(razao_social__icontains=search) |
                Q(nome_fantasia__icontains=search) |
                Q(cidade__icontains=search) |
                Q(cnpj__icontains=search) |
                Q(representante__icontains=search) |
                Q(modalidade__icontains=search) |
                Q(cep__icontains=search) |
                Q(regiao_comercializacao__icontains=search) |
                Q(uf__icontains=search)
            )
        
        return queryset



