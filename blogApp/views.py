from django.shortcuts import render
from .models import UserPost
from .serializers import UserPostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def UserPostView(request):
    if request.method == "POST":
        data = request.data
        serializer = UserPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post added", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:     
        posts = UserPost.objects.all()
        serializer = UserPostSerializer(posts, many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def UserPostDetailView(request, id):
    try:
        user_post = UserPost.objects.get(id = id)
    except UserPost.DoesNotExist:
        return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        user_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT" or request.method == "PATCH":
        data = request.data
        serializer = UserPostSerializer(data=data, instance=user_post, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Post Edited", 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        serializer = UserPostSerializer(user_post)
        return Response(serializer.data, status=status.HTTP_200_OK)