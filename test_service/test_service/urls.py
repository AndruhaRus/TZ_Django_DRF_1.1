from django.urls import include, path
from rest_framework import routers
from tests.views import QuestionViewSet, TestResultViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'results', TestResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]