from rest_framework import serializers
from .models import StudentDrf
from django.views.decorators.csrf import csrf_exempt

class StudentSer(serializers.ModelSerializer):
    model=StudentDrf
    fields='__all__'

    def create(self, validated_data):
        return StudentDrf.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.no=validated_data.get('no',instance.no)
    #     instance.name=validated_data.get('no',instance.name)
    #     instance.address=validated_data.get('no',instance.address)
    #     instance.phone=validated_data.get('no',instance.phone)
    #     instance.save()
    #     return instance

    # class Meta():
    #     model = StudentDrf
    #     fields = "__all__"