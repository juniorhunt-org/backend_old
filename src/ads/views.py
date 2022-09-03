from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import ProfileUser
from .models import Ad, AdPhoto, AdSchedule, AdCategory
from .permissions import IsOwnerOrReadOnlySecond, IsAdminOrReadOnly
from .serializers import AdPhotoSerializer, AdCategorySerializer, AdSerializer, AdScheduleSerializer, AdUserSerializer


class AdList(ModelViewSet):
    permission_classes = []
    serializer_class = AdSerializer

    def get_queryset(self):
        owner = self.request.query_params.get('owner')
        queryset = Ad.objects.all()
        if owner:
            return queryset.filter(owner_id=int(owner))
        return queryset


class AdUserApi(CreateAPIView, DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUserSerializer

    permission_classes = [IsAuthenticated]

    def get_user_profile(self) -> int:
        user = Token.objects.get(key=self.request.auth.key).user
        profile = ProfileUser.objects.get(user__username=user.username)
        return profile

    def create(self, request, *args, **kwargs):
        try:
            ad_id = request.data['ad_id']
            ad = Ad.objects.get(pk=ad_id)
            user = self.get_user_profile()
            ad.users.add(user)
            ad.save()
            headers = self.get_success_headers(request.data)
            serializer = AdUserSerializer(ad)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response({'detail': 'Некорректные данные'}, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            ad_id = self.request.query_params['ad_id']
            ad = Ad.objects.get(pk=ad_id)
            user = self.get_user_profile()
            ad.users.remove(user)
            ad.save()
            headers = self.get_success_headers(request.data)
            serializer = AdUserSerializer(ad)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response({'detail': 'Некорректные данные'}, status.HTTP_400_BAD_REQUEST)


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


class AdReplyUserApi(ListCreateAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_user_id(self) -> int:
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        profile = ProfileUser.objects.get(user_id=user_id)
        return profile.pk

    def get_queryset(self):
        return Ad.objects.filter(users__id=self.get_user_id())
