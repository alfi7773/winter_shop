from django.db import models
from django_resized import ResizedImageField

class TimeAbstractModel(models.Model):
    created_at = models.DateField('дата добавления', auto_now_add=True)
    updated_at = models.DateField('дата изменения', auto_now=True)
    
    class Meta:
        abstract = True
        

class Type(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'типы'
        verbose_name = 'тип'
        
    name = models.CharField(verbose_name='название', max_length=100)
    
    def __str__(self):
        return self.name

        
class Category(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'
        
    name = models.CharField(verbose_name='название', max_length=100)
    
    def __str__(self):
        return self.name

class Tag(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'тэги'
        verbose_name = 'тэг'
        
    name = models.CharField(verbose_name='название', max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Brand(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'брэнды'
        verbose_name = 'брэнд'
        
    name = models.CharField(verbose_name='название', max_length=100)
    image = models.ImageField(verbose_name='мзображение', upload_to='brand_images/')
    
    def __str__(self):
        return self.name
    
    
class Country(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'страны'
        verbose_name = 'страна'
        
    name = models.CharField(verbose_name='название', max_length=100)
    
    def __str__(self):
        return self.name
    
class City(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'города'
        verbose_name = 'город'
        
    name = models.CharField(verbose_name='название', max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Product(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'товары'
        verbose_name = 'товар'
        
    name = models.CharField(verbose_name='название', max_length=100)
    decription = models.CharField('описание', max_length=100)
    type = models.ForeignKey('board.Type',verbose_name='типы', on_delete=models.PROTECT)
    category = models.ForeignKey('board.Category',verbose_name='категория', on_delete=models.PROTECT, related_name='product')
    tags = models.ManyToManyField('board.Tag', verbose_name='тэги')
    image = models.ManyToManyField('board.ImageProduct')
    price = models.DecimalField('цена', decimal_places=2, max_digits=10, blank=True, null=True)
    
    @property
    def image(self):
        if self.images.first():
            return self.images.first().image
        return None
    
    def __str__(self):
        return self.name
    

class ImageProduct(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'изображении товаров'
        verbose_name = 'изображение товара'
        ordering = ('-created_at',)
        
        
    product = models.ForeignKey('board.Product', on_delete=models.PROTECT, verbose_name='товар', related_name='images')
    image = ResizedImageField('фото', upload_to='product_images/', quality=90, force_format='WEBP')
    
    def __str__(self):
        return f'{self.product.name}'
    
    
class AttributeProduct(TimeAbstractModel):
    
    class Meta:
        verbose_name_plural = 'атрибуты'
        verbose_name = 'атрибут'
        ordering = ('-created_at',)
        
    
    name = models.CharField(verbose_name='название', max_length=50)    
    value = models.CharField(verbose_name='значение', max_length=50)    
    product = models.ForeignKey('board.Product', on_delete=models.PROTECT, related_name='attributes')
    
    def __str__(self):
        return f'{self.name} - {self.value}'
    

# Create your models here.
