{% extends "base.tpl" %}

{% block title %} - Movie - Index{% endblock %}

{% block content %}
<div class="row">
    <div class="row">
        <div class="col-sm-12">
            <h2>Get Movies</h2>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>Movie.all()</code>.
        </div>
        <div class="col-sm-6">
            <h3>Code</h3>
            <pre>g.V('element_type', 'movie')</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Movies:</h2>
        <table class="table table-striped">
        <tr><th>#</th><th>Vertex ID</th><th>Movie Title</th><th></th><th></th><th></th><th></th><th></th></tr>
        {% for movie in movies %}
        <tr>
            <td><a href="/movie/{{ movie.id }}">{{ loop.index }}</a></td>
            <td><a href="/movie/{{ movie.id }}">{{ movie.id }}</a></td>
            <td><a href="/movie/{{ movie.id }}">{{ movie.title }}</a></td>
            <td><a href="/movie/{{ movie.id }}/usersWithRatingsAbove" type="button" class="btn btn-sm">Users Who Rated</a></td>
            <td><a href="/movie/{{ movie.id }}/moviesWithRatingsAbove" type="button" class="btn btn-sm">Other Rated Movies</a></td>
            <td><a href="/movie/{{ movie.id }}/coratedMovie" type="button" class="btn btn-sm">Corated Movies</a></td>
            <td><a href="/movie/{{ movie.id }}/coratedMovieByGenre" type="button" class="btn btn-sm">Corated Movies by Genre</a></td>
            <td><a href="/movie/{{ movie.id }}/coratedMovieByAllGenre" type="button" class="btn btn-sm">Corated Movies by All Genres</a></td>
        </tr>
        {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock %}