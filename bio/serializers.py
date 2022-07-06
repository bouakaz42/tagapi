from lib2to3.pgen2.token import VBAR
from rest_framework import serializers
from .models import Bio , Content , Heading , Link , Contactform , Product , vCard  , Sociallinks
from drf_writable_nested import WritableNestedModelSerializer

# Write A serializers for Link model and Contactform model and Product model and vCard model
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class ContactformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactform
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class vCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = vCard
        fields = '__all__'


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = '__all__'


class ContentSerializer(WritableNestedModelSerializer):
    heading = HeadingSerializer(allow_null=True)
    link = LinkSerializer(allow_null=True)
    contact_form = ContactformSerializer(allow_null=True)
    vcard = vCardSerializer(allow_null=True)
    product = ProductSerializer(allow_null=True)
    class Meta:
        model = Content
        fields = '__all__'


class SociallinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sociallinks
        fields = '__all__'




class BioSerializer(WritableNestedModelSerializer):
    content  = ContentSerializer()
    class Meta:
        model = Bio
        fields = '__all__'
        read_only_fields = ('user',)
        depth = 1

    # write a create function to handle the null fields
   