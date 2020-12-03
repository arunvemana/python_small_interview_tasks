from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"


class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subCategory_name

    class Meta:
        db_table = "subcategory"
