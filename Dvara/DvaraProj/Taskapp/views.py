from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import UploadFileForm
from .models import *
import pandas as pd
from django.db import connection
from django.conf import settings
# Create your views here.


def sub_category_list(request):
    sub_category_list = SubCategory.objects.filter(
        cat_id=request.GET.get('cat_id')).values_list('cat_id', 'subCategory_name')

    # generate an html template for the specific option
    html_code = ""
    for sub_category in sub_category_list:
        var = f"<option value = '{sub_category[0]}' > {sub_category[1]} </option>"
        html_code += var

    return HttpResponse(html_code)


class Home(View):
    form_obj = UploadFileForm

    def inserting_rows(self, file_data):
        tables_list = connection.introspection.table_names()
        df = pd.ExcelFile(file_data)
        sheet_names = df.sheet_names

        all_tables_exist = False
        for sheet in sheet_names:
            if sheet.lower() in tables_list:
                all_tables_exist = True
            else:
                all_tables_exist = False

        if all_tables_exist:
            try:
                df1 = pd.read_excel(df, 'category')
                df2 = pd.read_excel(df, 'subcategory', names=[
                                    'id', 'subcategory'])
                dff = pd.merge(df1, df2, on="id")
                category_obj = Category()
                for i in dff.categories.unique():
                    Category.objects.create(category_name=i)
                    Category.save
                    filter_data = dff.loc[dff['categories'] == i]
                    for j in filter_data.subcategory.unique():
                        SubCategory.objects.create(
                            cat_id=Category.objects.latest('id'), subCategory_name=j)
                        SubCategory.save
                return "Data loaded sucessfully"
            except Exception as error:
                return f"Error arise while loading the data,{error}"

        else:
            return "Please check the sheet names, no tables are present "

        return "Data was not loaded"

    def get(self, request):
        category_data = Category.objects.all()
        return render(request, 'index.html', {'form': self.form_obj(), 'category': category_data})

    def post(self, request):
        form = self.form_obj(request.POST, request.FILES)

        if form.is_valid():
            file_data = request.FILES['file']
            resp = self.inserting_rows(file_data)
            return render(request, 'index.html', {"data": resp})

        return HttpResponse("<h1>not working</h1>")
