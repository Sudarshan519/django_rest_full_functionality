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
# from .models import PostalCode
# import json
# def inser_postal():
#     PostalCode.objects.all().delete()
#     f=open('./nepal_postal_code.json')
#     data=json.load(f)
#     for i in data:
#         postal_code=PostalCode()
#         postal_code.district=i['district']
#         postal_code.post_office=i['post_office']
#         postal_code.postal_pin_code=i['postal_pin_code']
#         postal_code.post_office_type=i['post_office_type']
#         postal_code.save()
# inser_postal()
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      urlpath='hajir.urls',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()
router.register(r'banners',views.BannerViewSet,basename='banners')
router.register(r'documents',views.ProfileDocumentViewset,basename='profileDocuments')
router.register(r'users', views.UserViewSet,'users')
router.register(r'document_history',viewset=views.ProfileVersionViewSet,basename='documents_versions')
# router.register(r'groups', views.GroupViewSet)
# router.register(r'register', views.register.as_view(),basename='register')
# register_user=
# router.register(r'signup',views.RegisterViewSet,basename='register')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


from drf_yasg.generators import OpenAPISchemaGenerator
class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/'
        return schema

public_schema_view = get_schema_view(   openapi.Info(
      title="Hajir API",
      default_version='v1',
      description="Test description",
     
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
                                     urlconf='hajir.urls',
                                     generator_class=PublicAPISchemeGenerator)
urlpatterns = [
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
    #   path('hajir/',include('hajir.urls')),
    # path('hajir/', public_schema_view.with_ui('swagger', cache_timeout=0), name='schema-public'),
    path('home',views.home),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('latest-transactions',views.get_latest_transactions),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('get-otp/<str:email>',views.get_otp),#<str:email>
    path('verify-otp/',views.getPhoneNumberRegistered.as_view()),#<str:email>
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view()),
    path('get-signup-info/',views.get_signup_info),
    path('register/',views.register),
    path('address/<str:code>',views.get_address),
    path('user_agreement/<str:type>',views.get_terms),
    path('emoji/',views.get_emoji_flag),
    path('countries_list',views.get_country_list),
    #  re_path(r'^auth/', include('djoser.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/',views.hello),
    path('insert_postal/',views.store_postal_codes_Nepal),
    path('get_rates_list',views.get_rates_list),
    path('provinces_district/',views.get_disticts_provinces),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user-orders',views.allproducts)
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls