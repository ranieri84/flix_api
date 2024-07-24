from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
# Create your views here.


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    else:
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201
        )


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()  # salva no banco de dados
        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
        )

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Deletado com sucesso'},
            status=204
        )
