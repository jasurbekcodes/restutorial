from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from app.models import Portfolio, Category, Post
from app.serializers import PortfolioSerializer, CategorySerializer, PostSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data)


@api_view(['GET'])
def all_posts_view(request):
    category_id = request.GET.get('category', None)
    posts = Post.objects.all()
    if category_id:
        posts = posts.filter(category__id=category_id)
    data = PostSerializer(posts, many=True).data
    return Response(data, 200)


@api_view(['GET'])
def portfolio_view(request):
    portfolio = Portfolio.objects.all()
    data = PortfolioSerializer(portfolio, many=True).data
    return Response(data)


@swagger_auto_schema(methods=['post',], request_body=CategorySerializer)
@api_view(['POST'])
def category_create_view(request):
    data = CategorySerializer(request.POST).data
    category_data = CategorySerializer(category).data
    return Response(category_data, 201)
