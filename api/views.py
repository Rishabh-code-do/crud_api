from rest_framework import generics, filters, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Box
from .serializers import BoxSerializer,RegisterSerializer, LoginSerializer, User, UserSerializer
from .permissions import IsStaffUser, IsBoxCreator
from .filters import BoxFilterSet


# Create your views here.

class BoxList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    filterset_class = BoxFilterSet

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data,context={'request': request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def get(self, request, *args, **kwargs):
        query_params = request.data
        queryset = self.get_queryset()
        queryset = BoxFilterSet(query_params, queryset, request=self.request).qs
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoxUpdate(generics.RetrieveUpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsStaffUser]

    def update(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            error_message = str(e)
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()



class MyBoxList(generics.ListAPIView):
    serializer_class = BoxSerializer
    permission_classes = [IsStaffUser]
    filter_backends = [filters.OrderingFilter]
    filterset_class = BoxFilterSet

    def get_queryset(self):
        queryset = Box.objects.filter(created_by=self.request.user)
        return queryset
    
    def get(self, request, *args, **kwargs):
        query_params = request.data
        queryset = self.get_queryset()
        queryset = BoxFilterSet(query_params, queryset, request=self.request).qs
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BoxDelete(generics.RetrieveDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsStaffUser,IsBoxCreator]

    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        is_staff = serializer.validated_data['is_staff']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,"is_staff": is_staff}, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

 
