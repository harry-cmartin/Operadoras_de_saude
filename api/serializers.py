from rest_framework import serializers
from .models import Operadora

class OperadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operadora
        fields = '__all__'

    def format_cep(self, cep):
        if len(cep) == 7:
            return f"0{cep}"
        return cep

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for field in representation:
            if representation[field] in [None, 'nan', 'nannan']:
                representation[field] = '-'
            if field == 'cep':
                representation[field] = self.format_cep(representation[field])
        return representation
    
        
"""  
    def format_phone(self, phone):
        if not phone or phone in ['nan', 'nannan']:
            return ''
        # n sei
        phone = str(phone).replace('.0', '').replace('.', '')
        if len(phone) >= 2:
            ddd = phone[:2]
            numero = phone[2:].lstrip('0')  # Remove zeros
            return f"{ddd}-{numero}"
        return phone
    
    #
"""