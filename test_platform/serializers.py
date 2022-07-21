from rest_framework import serializers
from .models import Test_question, Verifity_Models


class TestSerializer(serializers.ModelSerializer):
    # test_type = serializers.CharField(max_length = 10)
    question  = serializers.CharField(max_length = 100)
    options_A = serializers.CharField(max_length = 50)
    options_B = serializers.CharField(max_length = 50)
    options_C = serializers.CharField(max_length = 50)
    options_D = serializers.CharField(max_length = 50)
    answer    = serializers.IntegerField()

    def create(self, validated_data):
        return Test_question.objects.create(**validated_data)


    class Meta:
        model = Test_question
        fields = '__all__'

class User_Test_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Verifity_Models
        fields = '__all__'
