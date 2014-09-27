{% extends "base.tpl" %}

{% block title %} - Movie - Corated Movie by All Genres{% endblock %}

{% block content %}
<div class="row">
    <h2>Get Corated Movies by All Genres</h2>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>movie.get_corated_movie_by_all_genres(stars=stars, limit=limit)</code>.
        </div>
        <div class="col-sm-6">
            <h3>Code</h3>
            <pre>{{ code }}</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Corated Movies by All Genres:</h2>
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