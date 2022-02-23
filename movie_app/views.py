from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Director not found'})

    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializer(movie, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Product not found'})
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        Movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.text = request.data.get('text')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.save()
        return Response(data=MovieSerializer(movie).data)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Review not found'})

    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=MovieSerializer(review).data)


@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializer(movie_reviews, many=True).data
    return Response(data=data)
