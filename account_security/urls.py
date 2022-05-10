from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from twofa import views as twofa_views
from phone_verification import views as verify_views

urlpatterns = [
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

                  path('', twofa_views.register, name='register'),
                  path('2fa/', twofa_views.twofa, name='2fa'),  # green
                  path('token/sms', twofa_views.token_sms, name='token-sms'),
                  path('token/voice', twofa_views.token_voice, name='token-voice'),
                  path('token/onetouch', twofa_views.token_onetouch, name='token-onetouch'),  # noqa: E501
                  path('protected/', twofa_views.protected, name='protected'),
                  path('onetouch-status', twofa_views.onetouch_status, name='onetouch-status'),  # noqa: E501
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
