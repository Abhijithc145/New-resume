from rest_framework import serializers
from .models import *

class dataserilaizer(serializers.ModelSerializer):
    class Meta:
        model = JobType_json
        fields = "__all__"


class candidateserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"