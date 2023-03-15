from django.urls import include, path, re_path
from rest_framework import routers
from .import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet,'users')
# router.register(r'groups', views.GroupViewSet)
# router.register(r'register', views.register.as_view(),basename='register')
# register_user=
# router.register(r'signup',views.RegisterViewSet,basename='register')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('verify-otp/',views.getPhoneNumberRegistered.as_view()),#<str:email>
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view()),
    path('register/',views.register),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/',views.hello),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)