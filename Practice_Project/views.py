from django.shortcuts import render
import operator

def homePage(request):
    return render(request,'home.html')

def count(request):
    
    fulltext = request.GET['fulltext']
    textList=fulltext.split() 
    textDictionary={}
    for word in textList:
        if word in textDictionary:
            textDictionary[word]+=1
        else:
            textDictionary[word]=1
    sorted_dictionary = sorted(textDictionary.items(),key=operator.itemgetter(1),reverse=True)
    
    return render(request,'count.html',{"word_count":len(textList),"fulltext":fulltext,"sorted_dictionary":sorted_dictionary})

def about(request):
    return render(request,'about.html')