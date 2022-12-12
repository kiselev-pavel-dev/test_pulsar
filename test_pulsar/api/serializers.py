from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        org_ext = str(obj.image).split(".")[-1]
        formats = [org_ext, "webp"]
        data = {}
        data["path"] = "/" + "".join(str(obj.image).split(".")[:-1])
        data["formats"] = formats
        return data
