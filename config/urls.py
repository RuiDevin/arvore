from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from arvore.view import PaisViewSet, TiosViewSet, IrmaosViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"pai", PaisViewSet)
router.register(r"tio", TiosViewSet)
router.register(r"irmao", IrmaosViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
