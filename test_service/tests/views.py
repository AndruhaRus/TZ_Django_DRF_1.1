from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question, TestResult
from .serializers import QuestionSerializer, TestResultSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['get'])
    def difficult_question(self, request):
        difficult_question = Question.objects.order_by('-is_correct').first()
        serializer = self.get_serializer(difficult_question)
        return Response(serializer.data)

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer