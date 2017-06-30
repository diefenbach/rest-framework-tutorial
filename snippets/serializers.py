from rest_framework import serializers
from snippets.models import Snippet
from authors.models import Author


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='snippet-detail')
    author = serializers.HyperlinkedRelatedField(view_name="author-detail", queryset=Author.objects.all())

    class Meta:
        model = Snippet
        fields = ('url', "author", 'title', 'code')
