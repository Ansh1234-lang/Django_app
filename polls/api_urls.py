from rest_framework import routers

from .api_views import QuestionviewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionviewSet)
router.register(r'choice', ChoiceViewSet )

urlpatterns = router.urls