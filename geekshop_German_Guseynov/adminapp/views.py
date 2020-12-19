from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser

# Create your views here.

#users
from mainapp.models import ProductCategory, Product


# def user_create(request):
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {
#         'update_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', content)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Пользователь/Создание'
        return content

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active')
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)

class UsersListVies(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method =='POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     content = {
#         'update_form': edit_form
#     }
#
#     return render(request, 'adminapp/user_update.html', content)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Пользователь/Редактирование'
        return content


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         if user_item.is_active:
#             user_item.is_active = False
#         else:
#             user_item.is_active = True
#         user_item.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     content = {
#         'user_to_delete': user_item
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

#categories

# def category_create(request):
#     pass

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     categories_list = ProductCategory.objects.all().order_by('-is_active')
#     content = {
#         'objects': categories_list
#     }
#     return render(request, 'adminapp/categories.html', content)

class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Категории'
        return content

# def category_update(request, pk):
#     pass

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context

# def category_delete(request, pk):
#     pass

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


    #products
# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductEditForm(request.POST, request.FILES)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#
#     else:
#         update_form = ProductEditForm()
#
#     content = {
#         'update_form': update_form,
#         'category': category_item
#     }
#     return render(request, 'adminapp/product_update.html', content)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Продукт/Редактирование'
        content['category'] = self.kwargs['pk']
        return content

    def get_success_url(self):
        return reverse_lazy('admin:products', args=[self.kwargs['pk']])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print(kwargs)
        category_item = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        kwargs['initial'] = {'category': category_item}
        return kwargs

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     categories_item = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category=categories_item)
#     content = {
#         'objects': products_list,
#         'category': categories_item
#     }
#     return render(request, 'adminapp/products.html', content)

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Категории'
        content['category'] = self.kwargs['pk']
        return content

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category_id=category_pk)

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     product_items = get_object_or_404(Product, pk=pk)
#     content = {
#         'object': product_items
#     }
#     return render(request, 'adminapp/product_read.html', content)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Категории/Редактирование'
        return content



# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductEditForm(request.POST, request.FILES, instance=product_item)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#
#     else:
#         update_form = ProductEditForm(instance=product_item)
#
#     content = {
#         'update_form': update_form,
#         'category': product_item.category
#     }
#     return render(request, 'adminapp/product_update.html', content)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Продукт/Редактирование'
        update_product = get_object_or_404(Product, pk=self.kwargs['pk'])
        content['category'] = update_product.category.pk
        return content

    def get_success_url(self):
        update_product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', args=[update_product.category.pk])

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     delete_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         if delete_product.is_active:
#             delete_product.is_active = False
#             delete_product.save()
#         else:
#             delete_product.is_active = True
#             delete_product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[delete_product.category.pk]))
#
#     content = {
#         'product_to_delete': delete_product
#     }
#     return render(request, 'adminapp/product_delete.html', content)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        delete_product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', args=[delete_product.category.pk])

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())