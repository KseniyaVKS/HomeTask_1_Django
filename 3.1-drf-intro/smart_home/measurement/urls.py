from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from measurement.views import SensorView, MeasurementView, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>', SensorDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
