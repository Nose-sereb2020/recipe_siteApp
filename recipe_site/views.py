from django.shortcuts import render
import requests
import json

def request(request):

    api_key = 1044473351726139211
    r = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={}&categoryId=10&elements=recipeTitle,foodImageUrl,rank'.format(api_key))
    data = r.json()
    data = json.dumps(data['result'], ensure_ascii=False)
    data = json.loads(data)
    return render(request, 'recipe_site/request.html', {'data': data})
