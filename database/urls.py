from django.conf.urls import url
from database.views import DataControl
from django.views.generic import TemplateView, DetailView


urlpatterns = [
        url(r'^datacontrol/(?P<slug>\w+)$', DataControl.as_view()),
        url(r'^database/login/$',
        TemplateView.as_view(template_name="blog/data_index.html"),
        name='login-view'),

]
