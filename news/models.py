from django.db.models import DateTimeField, Model, CASCADE, ForeignKey, CharField, DecimalField, ImageField


class Category(Model):
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Product(Model):
    category = ForeignKey(Category, on_delete=CASCADE)
    name = CharField(max_length=128)
    price = DecimalField(max_digits=8, decimal_places=2)
    picture = ImageField(upload_to='products/')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
