from .models import Pgn
from .serializers import PgnSerializer
from authentication.serializers import UserPgnSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from authentication.models import User


class PgnList(APIView):
    
    @permission_classes([IsAuthenticated])
    def get(self, request):
        pgns = Pgn.objects.all()
        serializer = PgnSerializer(pgns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = PgnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchMyGames(APIView):
# Get all mygames of a user

    @permission_classes([IsAuthenticated])
    def get(self, request):
        pgns=[]
        user = User.objects.get(id=request.user.id)
        user_serializer = UserPgnSerializer(user)
  
        for pgn in user_serializer.data['my_games']:
            real_PGN = Pgn.objects.get(id=pgn)
            pgn_serializer=PgnSerializer(real_PGN)
            pgns.append(pgn_serializer.data)
        
        return Response(pgns, status=status.HTTP_200_OK)


class FetchFavorites(APIView):
# Get all favorites of a user

    @permission_classes([IsAuthenticated])
    def get(self, request):
        pgns=[]
        user = User.objects.get(id=request.user.id)
        user_serializer = UserPgnSerializer(user)
  
        for pgn in user_serializer.data['favorites']:
            real_PGN = Pgn.objects.get(id=pgn)
            pgn_serializer=PgnSerializer(real_PGN)
            pgns.append(pgn_serializer.data)
        
        return Response(pgns, status=status.HTTP_200_OK)


class FetchAssigned(APIView):
# Get all assigned games of a user

    @permission_classes([IsAuthenticated])
    def get(self, request):
        pgns=[]
        user = User.objects.get(id=request.user.id)
        user_serializer = UserPgnSerializer(user)
  
        for pgn in user_serializer.data['assigned']:
            real_PGN = Pgn.objects.get(id=pgn)
            pgn_serializer=PgnSerializer(real_PGN)
            pgns.append(pgn_serializer.data)
        
        return Response(pgns, status=status.HTTP_200_OK)


class AddPgnToMyGames(APIView):
# Record in junction table for MyGames

    @permission_classes([IsAuthenticated])
    def patch(self, request, pgn_pk):
        try:
            user = User.objects.get(id=request.user.id)
            pgn = Pgn.objects.get(id=pgn_pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.my_games.add(pgn)
        user.save()
        serializer = UserPgnSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddPgnToFavorites(APIView):
# Record in junction table for Favorites

    @permission_classes([IsAuthenticated])
    def patch(self, request, pgn_pk):
        try:
            user = User.objects.get(id=request.user.id)
            pgn = Pgn.objects.get(id=pgn_pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.favorites.add(pgn)
        user.save()
        serializer = UserPgnSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class AddPgnToAssigned(APIView):
    # Record in junction table for Assigned

    @permission_classes([IsAuthenticated])
    def patch(self, request, pgn_pk):
        try:
            user = User.objects.get(id=request.user.id)
            pgn = Pgn.objects.get(id=pgn_pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.assigned.add(pgn)
        user.save()
        serializer = UserPgnSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class PgnDetail(APIView):

#     # GET Pgn by Id
#     @permission_classes([IsAuthenticated])
#     def get(self, request, pk):
#         games = Pgn.objects.filter(user_id=request.user.id)
#         my_game = games.filter(id=pk).values()
#         serializer=PgnSerializer(my_game)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # DELETE Pgn
#     @permission_classes([IsAuthenticated])
#     def delete(self, pk):
#         game = get_object_or_404(Pgn, pk=pk)
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)