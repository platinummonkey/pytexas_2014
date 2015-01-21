{% extends "base.tpl" %}

{% block title %} - Movie - Users With Ratings above {{ stars }}{% endblock %}

{% block content %}
<div class="row">
    <div class="row">
        <div class="col-sm-3">
            <h2>Get {{ limit }} Users who Rated other movies with at least {{ stars }} stars.</h2>
        </div>
        <div class="col-sm-9">
            <a href="/movie/{{ movie.id }}" type="button" class="btn btn-default">Get Movie</a>
            <a href="/movie/{{ movie.id }}/moviesWithRatingsAbove" type="button" class="btn btn-default">Other Rated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovie" type="button" class="btn btn-default">Corated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovieByGenre" type="button" class="btn btn-default">Corated Movies by Genre</a>
            <a href="/movie/{{ movie.id }}/coratedMovieByAllGenre" type="button" class="btn btn-default">Corated Movies by All Genres</a>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <h3>Model</h3>
            Simply use <code>movie.get_users_given_movie_with_rating_above(stars=int, limit=int)</code>.
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
        <h2>Users:</h2>
        <table class="table table-striped">
        <tr><th>#</th><th>Vertex ID</th><th>User Age</th><th>User Gender</th></tr>
        {% for user in users %}
            <tr><td>{{ loop.index }}</td><td>{{ user.id }}</td><td>{{ user.age }}</td><td>{{ user.gender }}</td></tr>
        {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock %}
