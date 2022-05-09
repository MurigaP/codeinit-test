from rest_framework.routers import DefaultRouter
from .views.user import UserAccountViewSet

from .views.document import DocumentViewSet

router = DefaultRouter(trailing_slash=False)
# configuring api routers
router.register("user", UserAccountViewSet, basename="user")
router.register("", DocumentViewSet, basename="")
urlpatterns = router.urls
