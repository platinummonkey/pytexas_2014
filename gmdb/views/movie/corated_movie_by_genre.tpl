{% extends "base.tpl" %}

{% block title %} - Movie - Corated Movie by Genre{% endblock %}

{% block content %}
<div class="row">
    <!--h2>Get Corated Movies by Genre</h2-->
    <div class="row">
        <div class="col-sm-3">
            <h2>Get Corated Movies by Genre</h2>
        </div>
        <div class="col-sm-9">
            <a href="/movie/{{ movie.id}}" type="button" class="btn btn-default">Get Movie</a>
            <a href="/movie/{{ movie.id }}/usersWithRatingsAbove" type="button" class="btn btn-default">Users Who Rated</a>
            <a href="/movie/{{ movie.id }}/moviesWithRatingsAbove" type="button" class="btn btn-default">Other Rated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovie" type="button" class="btn btn-default">Corated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovieByAllGenre" type="button" class="btn btn-default">Corated Movies by All Genres</a>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <h3>Model</h3>
            Simply use <code>movie.get_corated_movie_by_genre(stars=stars, limit=limit)</code>.
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <h3>Code</h3>
            <pre>{{ code }}</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Corated Movies by Genre:</h2>
        <table class="table table-striped">
        <tr><th>#</th><th>ID</th><th>Movie Title</th><th>Number of Users Who Rated with at least {{ stars }} stars</th></tr>
        {% for item in movies|dictsort(False, 'value')|reverse %}
            <tr><td><a href="/movie/{{ item[0].id }}">{{ loop.index }}</a></td>
                <td><a href="/movie/{{ item[0].id }}">{{ item[0].id }}</a></td>
                <td><a href="/movie/{{ item[0].id }}">{{ item[0].title }}</a></td>
                <td><a href="/movie/{{ item[0].id }}">{{ item[1] }}</a></td></tr>
        {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock %}
