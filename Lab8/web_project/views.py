from django.http.response import HttpResponse, JsonResponse

products_list = [
   {
   'id': _id,
   'name':  f'Product{_id}',
   'price':_id * 1000
   }
   for _id in range(1,11)
]

def products(request):
   return JsonResponse(products_list, safe=False)

def product_detail(request,product_id):
   return JsonResponse({'id':product_id})
