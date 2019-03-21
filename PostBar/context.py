from PostBar.models import Category

def additional_categories_list(request):
    return {'base_category_list': Category.objects.all()}
