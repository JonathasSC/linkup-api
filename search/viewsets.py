from rest_framework.views import APIView
from rest_framework.response import Response

from apps.profile.models import Users
from apps.profile.serializers import UsersSerializer

from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class SearchAPIView(APIView):

    @method_decorator(cache_page(6))
    def post(self, request, *args, **kwargs):
        queries = request.data.get('queries', '')
        terms = queries.split()
        query: Q = Q()

        for term in terms:
            query |= Q(username__icontains=term) | Q(
                first_name__icontains=term) | Q(last_name__icontains=term)

        users = Users.objects.filter(query).distinct()
        user_serializer = UsersSerializer(users, many=True)

        return Response({
            'users': user_serializer.data,
        })
