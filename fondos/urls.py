from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fondos.views import BancoView

urlpatterns = {
                url(r'banco/$', BancoView.as_view(), name='banco'),
              }

urlpatterns = format_suffix_patterns(urlpatterns)
