from rest_framework.routers import DefaultRouter
from .views import TodoViews

router = DefaultRouter()
router.register(r'todos',TodoViews,basename='todo')

urlpatterns = router.urls