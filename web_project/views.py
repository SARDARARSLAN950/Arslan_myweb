from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request,'index.html')

#def downlouds(request):
  #  return HttpResponse( '<h1> this is no responce </h1>')

# def result(request):
#     article = request.GET.get('article', '')
#     words = article.split()
#     word_count = len(words)
#     dict_words = {}
#     for word in words:
#         if word in dict_words:
#             dict_words[word] += 1
#         else:
#             dict_words[word] = 1

    # name = request.GET.get('user_name', '')
    # age = request.GET.get('user_age', '')

    # if not name or not age:
    #     message = 'Please provide user_name and user_age in the form.'
    # else:
    #     message = f'hi {name}, your are {age}, years old'
    # var_dict= sorted(dict_words.items(),key = operator.itemgetter(1),reverse=True)
    
    # return render(request, 'result.html', {'article':article,'word_count':word_count,'dict_words':var_dict})

def result(request):
    article = request.GET.get('article', '')
    var_dict,word_count =counter.count(article)

    return render(request, 'result.html', {'article':article,'word_count':word_count,'dict_words':var_dict})
