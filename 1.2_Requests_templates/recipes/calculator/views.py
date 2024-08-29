from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def start_page(request):
    return render(request, 'main/start_page.html')

def get_recipe(request, dish):
    amount = int(request.GET.get('servings', 1))
    context = {}
    if dish in DATA:
        context = {'recipe': {key: value * amount for key, value in DATA[dish].items()}}
    return render(request, 'calculator/index.html', context)
