from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest,HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.contrib import messages
from movierecommendationapp.form import LoginForm, RegisterForm
from movierecommendationapp.models import MovieCustomUser, Movie, MovieSelection
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from re import IGNORECASE
import re
import json


#Views

# Login
def user_login(request: HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        uname = request.POST['username']
        pword = request.POST['password']
        movieuser = authenticate(username=uname, password=pword)
        if movieuser:
            login(request,movieuser)
            print(request.user.is_authenticated)
            request.session['user_id']= movieuser.id
            print(request.session['user_id'])
            return HttpResponseRedirect('http://localhost:5173')
        else:
            messages.error(request,'Unsuccessful login. Please check and try the credentials again.')
    form = LoginForm()
    return render (request, 'movierecommendationapp/login.html',{'form':form})

# check whether a session is created and user is authenticated before logging in
def user_session(request):
    if request.method == "GET":
        print(request.user.is_authenticated)
        # Django Project. (n.d.). Django. [online] Available at: https://docs.djangoproject.com/en/4.2/topics/http/sessions/ 
        return JsonResponse( { 'user_id' : request.session.__getitem__("_auth_user_id") } , safe=False ) 

       
# Register
def user_register(request: HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            movieuser = authenticate(request, username=username, password=password)
            messages.success(request, 'Successful registration for ' + username)
            login(request,movieuser)
            return HttpResponseRedirect('http://localhost:8000')
        else:
            messages.error(request,'An error has occured. Please try again and make sure the restrictions are followed.')
    form = RegisterForm()
    return render (request, 'movierecommendationapp/register.html',{'form':form})
 

def user_logout(request: HttpRequest)-> HttpResponse:
    logout(request)
    request.session.clear
    return HttpResponseRedirect('http://localhost:8000')

"""
Access the movies and create a new movie object in JSON, 
and post it to the movie list using POST request, save the new object
"""

def get_movies(request: HttpRequest)-> HttpResponse:

    # GET Ajax request method
    if request.method == 'GET':
        return JsonResponse(
            {
                'movies':[
                    movie.to_dict()
                    for movie in Movie.objects.all()
                ]
            }
        )
@csrf_exempt
def add_movies(request:HttpRequest)-> HttpResponse:
    # POST Ajax request method
    if request.method == 'POST':
        body_decode= request.body.decode('utf-8')
        result= json.loads(body_decode)
        savechoice = MovieSelection.objects.create(
            title = result['title'],
            movieuser = result['userid']
        )

        savechoice.save()
    return JsonResponse({'saved':'saved'}, status=200)


""" To implement the content based algorithm, I am using these tutorials:

*www.youtube.com. (n.d.). Project 18. Movie Recommendation System using Machine Learning with Python. [online] Available at: https://www.youtube.com/watch?v=7rEagFH9tQg&ab_channel=Siddhardhan 
*www.youtube.com. (n.d.). Movie Recommendation System With Python And Pandas: Data Project. [online] Available at: https://www.youtube.com/watch?v=eyEabQRBMQA&ab_channel=Dataquest

* KDnuggets. (n.d.). Content-based Recommender Using Natural Language Processing (NLP). [online] Available at: https://www.kdnuggets.com/2019/11/content-based-recommender-using-natural-language-processing-nlp.html.
"""

@csrf_exempt
def recommendation(request: HttpRequest)-> JsonResponse:
    #Loads body
    if request.method == 'GET':
        
        # find movie index using title
        top_recommended_movies = []

        # load and read the csv file data
        movies = pd.read_csv('final.csv')

        # replace null with empty strings
        movies['title'] = movies['title'].fillna('')
        movies['genres'] = movies['genres'].fillna('')
        movies['happy'] = movies['happy'].fillna('')
        movies['angry'] = movies['angry'].fillna('')
        movies['sad'] = movies['sad'].fillna('')

        # combine the movie features- title, genre and keywords as a bag of words
        movie_features =  movies['title'] + ' ' + movies['genres']

        # define the emotional categories
        movies_emotions = movies[['happy', 'angry', 'sad']]

        # TF*IDF matrix to convert the text of these features into feature vectors
        movie_vectorizer = TfidfVectorizer(ngram_range=(1,2)) # ngram ensures that group of eg 2 words are checked together for searching purposes
        feature_movie_vectors = movie_vectorizer.fit_transform(movie_features)
        # transform set of combined features data into a matrix in numerical form
        emotions = movies_emotions.values

        # concatenate horizontally the current features vectors with the emotional scores to make feature matrix
        new_feature_movie_vectors = np.concatenate((feature_movie_vectors.toarray(), emotions), axis=1)

        # compare each user movie input to each movie within the dataset and determine their similarity between all movies
        movie_similarity = cosine_similarity(new_feature_movie_vectors)

        currentuser = request.session.__getitem__("_auth_user_id")
        # usermovies = MovieSelection.objects.filter(movieuser=currentuser)
        usermovies = [chosenmovie.to_dict() for chosenmovie in MovieSelection.objects.filter(movieuser=currentuser)]
        print(usermovies)
        # https://www.kdnuggets.com/2019/11/content-based-recommender-using-natural-language-processing-nlp.html
        for movie in usermovies:
            # convert user movie choice title into lowercase
            print(movie['title'])
            title = str(movie['title']).lower()
            print(title)

            # find movie index using title
            movie_index = movies[movies['title'].str.contains(title, flags=IGNORECASE, na=False)].index[0]
            # obtain pairwise similarity scores between input movie and other remaining movies within dataset
            movie_similarity_score = list(enumerate(movie_similarity[movie_index])) # run a iteration to find similarity for all movies similarity scores using the movie index
            #sorted_similar_movies = sorted(movie_similarity_score, key = lambda x: x[1], reverse = True) # sort in descending order from index 1 movies based on similarity score

            sorted_similar_movies = sorted(movie_similarity_score, key = lambda x: x[1], reverse = True)[1:]
            for i in range(4):
                # movie index obtained from sorted similar movies
                index = sorted_similar_movies[i][0]
                # access the row of movie from movie then append to top recommended movies
                top_recommended_movies.append(movies.iloc[index]['title'])
            print(top_recommended_movies)

        for movie in usermovies:
            if movie in top_recommended_movies:
                top_recommended_movies.remove(movie)
        top_recommended_movies = list(set(top_recommended_movies))

    return JsonResponse({'recs': top_recommended_movies}, status=200)
