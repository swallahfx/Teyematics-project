from rest_framework.response import Response
from rest_framework import generics, status, pagination
from viewerapp.models import Posts, Comments 
from viewerapp.serializers import SearchSerializer, CommentSerializer, PostSerializer
import pandas as pd
from django.db.models import Q


'''
This function below represents a Schema that was extracted from the .csv header and and was then used
to create a database table, the other part of the .csv file was looped through
and was used to populate the database for futher used

N.B this is DjangoORM replicating SCHEMA or Sql query_test
'''

def populate_post_comment_table(post_model, comment_model):
    
    '''The if cobdition helps to check wether the database is empty or Not
    and if empty, it gets populated and if not empty'''
    
    if not post_model.objects.filter(id=1).exists():
        post_data = pd.read_csv('posts.csv')
        for i in range(post_data.shape[0]):
                posts = post_model.objects.create(
                id= post_data['id'][i],
                title= post_data['title'][i],
                userId= post_data['userId'][i],
                body=post_data['body'][i]
            )
        posts.save()
    if not comment_model.objects.filter(id=1).exists():
        comment_data = pd.read_csv('comments.csv')
        for i in range(comment_data.shape[0]):
            comments = comment_model.objects.create(
                postId= post_model.objects.get(id=comment_data['postId'][i]),
                id= comment_data['id'][i],
                name= comment_data['name'][i],
                email= comment_data['email'][i],
                body=comment_data['body'][i]
            )
        comments.save()

class ResPagination(pagination.PageNumberPagination):
    
    page_size = 10 # Number of objects to return in one page

    def generate_response(self, query_set, serializer_obj, request):
        try:
            page_data = self.paginate_queryset(query_set, request)
        except Exception as e:
            return Response({"error": f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        serialized_page = serializer_obj(page_data, many=True).data
        return self.get_paginated_response(serialized_page)
   
   
class AddComment(generics.GenericAPIView):
    '''
    This is the logic that allow users to add new commwnt
    
    '''
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
        return Response(dict(data=serializer.data), status=200)
        
        
class SearchCommentByPost(generics.GenericAPIView):
    '''
    This is the logic that allow users to comment on a specific post
    
    '''
    serializer_class = SearchSerializer
    queryset = Comments.objects.all()
    pagination_class = ResPagination
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        populate_post_comment_table(Posts, Comments)
        if serializer.is_valid(raise_exception=True):
            get_comment = Comments.objects.filter(Q(body__icontains=serializer.data.get('search')))
            post = Posts.objects.filter(id__in=get_comment.values_list('postId')) 
            data = PostSerializer(post, many=True).data  
            paginator = ResPagination()    
            data = paginator.generate_response(post, PostSerializer, request)    
            # print(data.data, type(data))
            return Response({'data':data.data}, status=200)
        return Response(dict(error="an error occured"), status=400)
    