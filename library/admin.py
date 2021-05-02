from django.contrib import admin
from django import forms

from .models import Category, SubCategory, App, Prop, Image

import re


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []


class PropInline(admin.TabularInline):
    model = Prop
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        handle_uploaded_file(request.FILES['svg_icon'])
        super().save_model(request, obj, form, change)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        handle_uploaded_file(request.FILES['svg_icon'])
        super().save_model(request, obj, form, change)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
            PropInline,
            ImageInline,
    ]


# def handle_uploaded_file(f):
#     svg_code = ''
#     for line in f:
#         svg_code += line.decode()
#
#     ch_count = len(svg_code)
#
#     pattern1 = re.compile('<svg.*>', re.DOTALL)
#     pattern2 = re.compile('<path.*>', re.DOTALL)
#
#     svg_result = pattern1.findall(svg_code, re.DOTALL)[0]
#
#     pattern3 = re.compile('class=[\'\"].*[\'\"]')
#
#     print(pattern3.findall(svg_result))
#
#     if pattern3.search(svg_result, re.DOTALL):
#         svg_handled = pattern3.sub('class="app-list__svg"', svg_result, re.DOTALL)
#     else:
#         svg_handled = re.sub('<svg', '<svg class="app-list__svg"', svg_result, re.DOTALL)
#
#     svg_code = re.sub(str(svg_result), str(svg_handled), svg_code, re.DOTALL)
#
#     path_result = pattern2.findall(svg_code, re.DOTALL)
#
#     path_handled = []
#
#     for i in path_result:
#         print(pattern3.findall(i))
#         print(i)
#         if pattern3.findall(i):
#             path_handled.append(pattern3.sub('class="app-list__svg-path"', i, re.DOTALL))
#         else:
#             path_handled.append(re.sub('<path', '<path class="app-list__svg-path"', i, re.DOTALL))
#
#     for i in range(len(path_handled)):
#         svg_code = re.sub(str(path_result[i]), str(path_handled[i]), svg_code, re.DOTALL)
#
#     f.seek(0)
#
#     f.write((' ' * ch_count).encode())
#     f.seek(0)
#
#     f.write(svg_code.encode())

def handle_uploaded_file(f):
    svg_code = ''
    for line in f:
        svg_code += line.decode()

    ch_count = len(svg_code)

    pattern = re.compile(' class=[\'\"]\S*[\'\"]')

    svg_code = pattern.sub('', svg_code)

    svg_code = re.sub('<svg', '<svg class="app-list__svg"', svg_code, re.DOTALL)
    svg_code = re.sub('<path', '<path class="app-list__svg-path"', svg_code, re.DOTALL)

    f.seek(0)

    f.write((' ' * ch_count).encode())
    f.seek(0)

    f.write(svg_code.encode())
