from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from api.serializer import Post_form
from api.models import Posts

@api_view(['GET'])
def get_all(request):
    if request.method == "GET":
        posts = Posts.objects.all().order_by('-id')
        serializer = Post_form(posts, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response("Invalid request type", status=405)

@api_view(['GET'])
def get_by_id(request, id):
    if request.method == "GET":
        try:
            posts = Posts.objects.get(id=id)
            serializer = Post_form(posts, many=False)
            return Response(serializer.data, status=200)
        except Posts.DoesNotExist:
            raise Http404
    else:
        return Response("Invalid request type", status=405)


@api_view(['POST'])
def post_blog(request):
    if request.method == 'POST':
        serializer = Post_form(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)
    else:
        return Response("Invalid request type", status=405)

@api_view(["PUT"])
def edit_blog(request, id):
    if request.method == "PUT":
        try:
            post = Posts.objects.get(id=id)
            serilaizer = Post_form(post, data=request.data)
            if serilaizer.is_valid(raise_exception=True):
                serilaizer.save()
                return Response(serilaizer.data, status=201)
            else:
                return Response(serilaizer.data, status=405)
        except Posts.DoesNotExist():
            raise Http404
    else:
        return Response("Invalid request type", status=400)