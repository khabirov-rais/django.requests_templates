from django.http import HttpResponse
from django.shortcuts import render, reverse

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
    'okroshka': {
        'квас, л': 1,
        'колбаса, г': 300,
        'яйцо, шт': 4,
        'картофель, шт': 5,
        'огурец, шт': 3,
        'редис, г': 125, 
    }
    # можете добавить свои рецепты ;)
}

# def home_view(request):
#     template_name = 'app/home.html'

#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать рецепт омлета': reverse('dish'),
#         'Показать рецепт пасты': reverse('dish'),
#         'Показать рецепт бутера': reverse('dish'),
#         'Рецепт окрошки(на квасе)': reverse('dish')
#     }
#     context = {
#         'pages': pages
#     }
#     return render(request, template_name, context)

def dish_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    DATA[f'{dish}'].update((key, value * servings) for key, value in DATA[f'{dish}'].items())
    context = {'recipe': DATA[f'{dish}']}
    return render(request, 'calculator/index.html', context)
    # return HttpResponse(f'{DATA['omlet']}')

# def pasta(request):
#     servings = int(request.GET.get('servings', 1))
#     DATA['pasta'].update((key, value * servings) for key, value in DATA['pasta'].items())
#     context = {'recipe': DATA['pasta']}
#     return render(request, 'calculator/index.html', context)

# def buter(request):
#     servings = int(request.GET.get('servings', 1))
#     DATA['buter'].update((key, value * servings) for key, value in DATA['buter'].items())
#     context = {'recipe': DATA['buter']}
#     return render(request, 'calculator/index.html', context)

# def okroshka(request):
#     servings = int(request.GET.get('servings', 1))
#     DATA['okroshka'].update((key, value * servings) for key, value in DATA['okroshka'].items())
#     context = {'recipe': DATA['okroshka']}
#     return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
