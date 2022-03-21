from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="MertketFy API",
      default_version='v1',
      description="",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="batman@merketfy.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include('core.urls')),
    # Schema Generation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
