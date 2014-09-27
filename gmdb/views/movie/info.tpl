{% extends "base.tpl" %}

{% block title %} - Movie - {{ movie.title|title }}{% endblock %}

{% block content %}
<div class="row">
    <div class="row">
        <div class="col-sm-3">
            <h2>Get Movie</h2>
        </div>
        <div class="col-sm-9">
            <a href="/movie/{{ movie.id }}/usersWithRatingsAbove" type="button" class="btn btn-default">Users Who Rated</a>
            <a href="/movie/{{ movie.id }}/moviesWithRatingsAbove" type="button" class="btn btn-default">Other Rated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovie" type="button" class="btn btn-default">Corated Movies</a>
            <a href="/movie/{{ movie.id }}/coratedMovieByGenre" type="button" class="btn btn-default">Corated Movies by Genre</a>
            <a href="/movie/{{ movie.id }}/coratedMovieByAllGenre" type="button" class="btn btn-default">Corated Movies by All Genres</a>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>Movie.get(&lt;int:vertex_id&gt;) or Movie.find_by_value('movie_title', &lt;str:movie_title&gt;)</code>.
        </div>
        <div class="col-sm-6">
            <h3>Code</h3>
            <pre>{{ code }}</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Movie:</h2>
        <table class="table table-striped">
        <tr><th>Vertex ID</th><th>Movie Title</th></tr>
        <tr><td>{{ movie.id }}</td><td>{{ movie.title }}</td></tr>
        </table>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-10" id="infoVis"></div>
        <div id="log" class="col-sm-2"></div>
    </div>
</div>
{% endblock %}