from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)
    characters = len(fulltext) - (count-1)
    indiwords = {}
    for word in wordlist:
        if word in indiwords:
            indiwords[word] += 1
        else:
            indiwords[word] = 1
    sortedwords = sorted(indiwords.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext , 'count': count, 'characters': characters, 'indiwords': sortedwords})

def about(request):
    return render(request, 'about.html')
