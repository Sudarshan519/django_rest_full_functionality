from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
# from drf_yasg.generators import OpenAPISchemaGenerator
# class CustomSchemaGeneratorClass(OpenAPISchemaGenerator):
#         def determine_path_prefix(self, request):
#             return super().determine_path_prefix("/v2/")
schema_view = get_schema_view(
   openapi.Info(
      title="Hajir API",
      default_version='v1',
    #   url='hajir',
      urlconf='hajir/',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ), 
#    generator_class=CustomSchemaGeneratorClass,
   public=True,
   permission_classes=[permissions.AllowAny],
)

# class CustomSchemaGeneratorClass(OpenAPISchemaGenerator):
#         def determine_path_prefix(self, request):
#             return super().determine_path_prefix("/hajir/v2/")

# schema_view = get_schema_view(
#     openapi.Info(
#         title="title",
#         default_version="v1",
#         description="desc",
#         url='/hajir/'
#     ),
#     generator_class=CustomSchemaGeneratorClass,
# )

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
#     def get_schema(self, request=None, public=False):
#         schema = super().get_schema(request, public)
#         schema.base_path = '/api/v1/public/'
#         return schema


# class PrivateAPISchemeGenerator(OpenAPISchemaGenerator):
#     def get_schema(self, request=None, public=False):
#         schema = super().get_schema(request, public)
#         schema.base_path = '/api/v1/private/'
#         return schema
# class HajirAPISchemeGenerator(OpenAPISchemaGenerator):
#     def get_schema(self, request=None, public=False):
#         schema = super().get_schema(request, public)
#         schema.base_path = ''
#         return schema

# public_schema_view = get_schema_view(...,
#                                      urlconf='public_apis.urls',
#                                      generator_class=PublicAPISchemeGenerator)
# private_schema_view = get_schema_view(...,
#                                       urlconf='private_apis.urls',
# #                                       generator_class=PrivateAPISchemeGenerator)
# schema_view = get_schema_view(
#     openapi.Info(title="HAJIR",default_version='v1',),
#     public=True, urlconf='hajir.urls',
#     generator_class=HajirAPISchemeGenerator 
#     )
# get_schema_view(
#    openapi.Info(
#       title="Hajir API",
#       default_version='v1',
#       description="Test description",
     
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#      urlconf='hajir.urls',
#    permission_classes=[permissions.AllowAny],
# )

# from drf_yasg.generators import OpenAPISchemaGenerator
# class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
#     def get_schema(self, request=None, public=False):
#         schema = super().get_schema(request, public)
#         schema.base_path = 'hajir/'
#         return schema

# public_schema_view = get_schema_view(   openapi.Info(
#       title="Hajir API",
#       default_version='v1',
#       description="Test description",
     
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#                                      urlconf='public_apis.urls',
#                                      generator_class=PublicAPISchemeGenerator)



from drf_yasg.generators import OpenAPISchemaGenerator
class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/hajir'
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
from . import views
urlpatterns = [
     path("ip-addr/", views.get_ip_address, name="ip address"),
   path("login/",views.login),
   path("employee/dashboard/",views.EmployeeDashboard.as_view()),
   path("employee/accept-invitation",views.AcceptInvitation.as_view()),
   path("dashboard/",views.employee_dashboard),
   path("throttle/",views.view),
   path("weekly-report",views.get_weekly_report),
   # path("dashboard/",views.EmployeeDashboard.as_view()),
   path("verify-otp/",views.verify_phone),
   path('swagger/', public_schema_view.with_ui('swagger', cache_timeout=0), name='schema-public'),
    # re_path(r'^auth/', include('djoser.urls')),
   #  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   
]

urlpatterns = format_suffix_patterns(urlpatterns)