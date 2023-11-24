from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from arvore.view import PaisViewSet, TiosViewSet, IrmaosViewSet,PrimosViewSet, EnderecoViewSet, EscolaridadeViewSet, TrabalhoViewSet, ProfissaoViewSet, MesViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"pai", PaisViewSet)
router.register(r"tio", TiosViewSet)
router.register(r"irmao", IrmaosViewSet)
router.register(r"primos", PrimosViewSet)
router.register(r"endereco", EnderecoViewSet)
router.register(r"escolaridade", EscolaridadeViewSet)
router.register(r"trabalho", TrabalhoViewSet)
router.register(r"profissao", ProfissaoViewSet)
router.register(r"mes", MesViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
