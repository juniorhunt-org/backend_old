from rest_framework.viewsets import ModelViewSet

from .models import Ad, AdPhoto, AdSchedule, AdCategory
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlySecond, IsAdminOrReadOnly
from .serializers import AdPhotoSerializer, AdCategorySerializer, AdSerializer, AdScheduleSerializer


class AdList(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdPhotoList(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnlySecond]
    queryset = AdPhoto.objects.all()
    serializer_class = AdPhotoSerializer

    def get_queryset(self):
        queryset = AdPhoto.objects.all()
        ad = self.request.query_params.get('ad')
        if ad:
            queryset = queryset.filter(ad=int(ad))
        return queryset


class AdScheduleList(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnlySecond]
    serializer_class = AdScheduleSerializer

    def get_queryset(self):
        queryset = AdSchedule.objects.all()
        ad = self.request.query_params.get('ad')
        if ad:
            queryset = queryset.filter(ad=int(ad))
        return queryset


class AdCategoryList(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = AdCategory.objects.all()
    serializer_class = AdCategorySerializer
