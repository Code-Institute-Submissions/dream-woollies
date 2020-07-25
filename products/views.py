from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Collection

def all_products(request):
    """ A view to show all products, including sorting and search queries.
        Pagination included for more than 12 products on page
    """
    
    products_list = Product.objects.all()
    query = None
    collections = None
    collection_page = None
    sort = None
    direction = None
    query_page = None
   
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products_list = products_list.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products_list = products_list.order_by(sortkey)

        if 'collection' in request.GET:
            collections = request.GET['collection'].split(',')
            products_list = products_list.filter(collection__name__in=collections)
            collections = Collection.objects.filter(name__in=collections)
            collection_page = request.GET['collection']

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!\
                                        You were automatically redirected to All Products page.")
                return redirect(reverse('products'))
            query_page = request.GET['q']
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products_list = products_list.filter(queries)
    
    current_sorting = f'{sort}_{direction}'
    
    paginator = Paginator(products_list, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'current_collections': collections,
        'collection_page': collection_page,
        'search_term': query,
        'query_page': query_page,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show one product's details """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

    