from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, View
from main.models import *
from main.mixins import *
from django.core.mail import send_mail
from django.conf import settings


class Main_Page(CartMixin, View):

    def get(self, request, *args, **kwargs):
        slides = Slides.objects.all()
        goodCategories = GoodsCategory.objects.all()
        goods = Good.objects.all()
        goodsImages = Goods_Images.objects.all()
        goodsHeight = Goods_Height.objects.all()
        goodSizes = Goods_Sizes.objects.all()
        goodIcons = Goods_Icons.objects.all()
        comments = Comments.objects.all()
        context = {
            'slides_list': slides,
            'goods_list': goods,
            'goods_images': goodsImages,
            'goods_height': goodsHeight,
            'goods_sizes': goodSizes,
            'goods_icons': goodIcons,
            'goods_cats': goodCategories,
            'cart': self.cart,
            'comments': comments,
        }
        return render(
            request,
            'main/index.html',
            context=context
        )

    def post(self, request, *args, **kwargs):
        Size = request.POST.get('FilterSize')
        Height = request.POST.get('FilterHeight')
        Rigidity = request.POST.get('FilterRigidity')
        goods = Good.objects.all()
        goodCategories = GoodsCategory.objects.all()
        if Height == '' and Rigidity == '':
            selection = Good.objects.filter(size=Size)
            if not selection.exists():
                context = {
                    'selections': selection.exists(),
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
            else:
                context = {
                    'selections': selection,
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
        elif Size == '' and Rigidity == '':
            if Height == 'Низкая':
                selection = Good.objects.filter(height__lte=9)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Средняя':
                selection = Good.objects.filter(height__range=(10, 15))
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Высокая':
                selection = Good.objects.filter(height__gte=16)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
        elif Size == '' and Height == '':
            selection = Good.objects.filter(rigidity=Rigidity)
            if not selection.exists():
                context = {
                    'selections': selection.exists(),
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
            else:
                context = {
                    'selections': selection,
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
        elif Size == '':
            if Height == 'Низкая':
                selection = Good.objects.filter(rigidity=Rigidity, height__lte=9)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Средняя':
                selection = Good.objects.filter(rigidity=Rigidity, height__range=(10, 15))
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Высокая':
                selection = Good.objects.filter(rigidity=Rigidity, height__gte=16)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
        elif Height == '':
            selection = Good.objects.filter(rigidity=Rigidity, size=Size)
            if not selection.exists():
                context = {
                    'selections': selection.exists(),
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
            else:
                context = {
                    'selections': selection,
                    'goods_list': goods,
                    'goods_cats': goodCategories,
                }
                return render(
                    request,
                    'main/selection.html',
                    context=context,
                )
        elif Rigidity == '':
            if Height == 'Низкая':
                selection = Good.objects.filter(height__lte=9, size=Size)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Средняя':
                selection = Good.objects.filter(height__range=(10, 15), size=Size)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Высокая':
                selection = Good.objects.filter(height__gte=16, size=Size)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
        else:
            if Height == 'Низкая':
                selection = Good.objects.filter(rigidity=Rigidity, size=Size, height__lte=9)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Средняя':
                selection = Good.objects.filter(rigidity=Rigidity, size=Size, height__range=(10, 15))
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
            elif Height == 'Высокая':
                selection = Good.objects.filter(rigidity=Rigidity, size=Size, height__gte=16)
                if not selection.exists():
                    context = {
                        'selections': selection.exists(),
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )
                else:
                    context = {
                        'selections': selection,
                        'goods_list': goods,
                        'goods_cats': goodCategories,
                    }
                    return render(
                        request,
                        'main/selection.html',
                        context=context,
                    )


class Product_Comparison(CartMixin, View):

    def post(self, request, *args, **kwargs):
        ct_model, slug = kwargs.get('ct_model'), kwargs.get('slug')
        if ct_model == 'Матрасы':
            product_ids = []
            ids = Good.objects.filter(category=2).values_list('id', flat=True)
            goods = Good.objects.all()
            for remaining_id in ids:
                product_ids.append(remaining_id)
            product_ids.remove(int(slug))
            goodCategories = GoodsCategory.objects.all()
            product_comparison = Good.objects.get(pk=slug)
            products = Good.objects.filter(pk__in=product_ids)
            context = {
                'goods_list': goods,
                'products': products,
                'goods_cats': goodCategories,
                'ct_model': ct_model,
                'product_comparison': product_comparison,
            }
            return render(
                request,
                'main/comparing.html',
                context=context,
            )
        elif ct_model == 'Кресла':
            product_ids = []
            ids = Good.objects.filter(category=3).values_list('id', flat=True)
            print(ids)
            goods = Good.objects.all()
            for remaining_id in ids:
                product_ids.append(remaining_id)
            product_ids.remove(int(slug))
            goodCategories = GoodsCategory.objects.all()
            product_comparison = Good.objects.get(pk=slug)
            products = Good.objects.filter(pk__in=product_ids)
            context = {
                'goods_list': goods,
                'products': products,
                'goods_cats': goodCategories,
                'ct_model': ct_model,
                'product_comparison': product_comparison,
            }
            return render(
                request,
                'main/comparing.html',
                context=context,
            )
        else:
            product_ids = []
            ids = Good.objects.filter(category=1).values_list('id', flat=True)
            print(ids)
            goods = Good.objects.all()
            for remaining_id in ids:
                product_ids.append(remaining_id)
            product_ids.remove(int(slug))
            goodCategories = GoodsCategory.objects.all()
            product_comparison = Good.objects.get(pk=slug)
            products = Good.objects.filter(pk__in=product_ids)
            context = {
                'goods_list': goods,
                'products': products,
                'goods_cats': goodCategories,
                'ct_model': ct_model,
                'product_comparison': product_comparison,
            }
            return render(
                request,
                'main/comparing.html',
                context=context,
            )


class Items_Details(CartMixin, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'Матрасы': Good,
        'Кровати': Good,
        'Кресла': Good,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Items_Details, self).get_context_data(**kwargs)
        context['images'] = Goods_Images.objects.all()
        context['ct_model'] = self.model
        context['height'] = Goods_Height.objects.all()
        context['sizes'] = Goods_Sizes.objects.all()
        context['goods_cats'] = GoodsCategory.objects.all()
        context['goods_list'] = Good.objects.all()
        context['comments'] = Comments.objects.all()
        return context

    context_object_name = 'item'
    template_name = 'main/item.html'
    slug_url_kwarg = 'slug'


class Cart_View(CartMixin, View):

    def get(self, request, *args, **kwargs):
        category = GoodsCategory.objects.all()
        images = Goods_Images.objects.all()
        goods = Good.objects.all()
        goodCategories = GoodsCategory.objects.all()
        context = {
            'cart': self.cart,
            'category': category,
            'image': images,
            'goods_cats': goodCategories,
            'goods_list': goods,
        }
        return render(
            request,
            'main/basket.html',
            context=context
        )

    def post(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        customer = Customer.objects.get(session_id=ip)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email_order = request.POST.get('email')
        comment = request.POST.get('comment')
        order = Order.objects.create(
            name=name,
            telephone=phone,
            email=email_order,
            agreement=True,
            cart=self.cart,
            comment=comment,
            customer=customer
        )
        customer.orders.add(order)
        order.save()
        send_mail('Заказ №{}'.format(order.id),
                  'Заказчик {}, телефон заказчика {}, товар можно посмотреть в козине {}, комментарии к заказу: {}'.format(
                      name,
                      phone,
                      self.cart.id,
                      comment
                  ),
                  settings.EMAIL_HOST_USER,
                  ['ilu6a234@gmail.com'])
        return HttpResponseRedirect('/success/')


class Add_To_Cart(CartMixin, View):

    def post(self, request, *args, **kwargs):
        height = request.POST.get('goodsHEIGHT')
        size = request.POST.get('goodsSIZE')
        ct_model, slug = kwargs.get('ct_model'), kwargs.get('slug')
        product = Good.objects.get(pk=slug)
        if height is None and size is None:
            cart_product, created = Goods_Cart.objects.get_or_create(
                user=self.cart.owner,
                cart=self.cart,
                content_type_id=1,
                object_id=product.id
            )
            if created:
                self.cart.products.add(cart_product)
                self.cart.save()
            return HttpResponseRedirect('/cart/')
        else:
            cart_product, created = Goods_Cart.objects.get_or_create(
                user=self.cart.owner,
                cart=self.cart,
                content_type_id=1,
                object_id=product.id,
                height=int(height),
                size=str(size)
            )
            if created:
                self.cart.products.add(cart_product)
                self.cart.save()
            return HttpResponseRedirect('/cart/')


class Delete_From_Cart(CartMixin, View):

    def post(self, request, *args, **kwargs):
        ct_model, slug = kwargs.get('ct_model'), kwargs.get('slug')
        product = Good.objects.get(pk=slug)
        cart_product = Goods_Cart.objects.get(
            user=self.cart.owner,
            cart=self.cart,
            content_type_id=1,
            object_id=product.id
        )

        self.cart.products.remove(cart_product)
        cart_product.delete()
        self.cart.save()
        return HttpResponseRedirect('/cart/')


class Change_Count_Items(CartMixin, View):

    def post(self, request, *args, **kwargs):
        ct_model, slug = kwargs.get('ct_model'), kwargs.get('slug')
        product = Good.objects.get(pk=slug)
        cart_product = Goods_Cart.objects.get(
            user=self.cart.owner,
            cart=self.cart,
            content_type_id=1,
            object_id=product.id
        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        self.cart.save()
        return HttpResponseRedirect('/cart/')


class Success_Page(CartMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'main/success.html'
        )
