{% extends "base.tpl" %}

{% block title %} - Movie - Movies With Ratings above {{ stars }}{% endblock %}

{% block content %}
<div class="row">
    <h2>Get {{ limit }} Movies which were Rated by Users who Rated other movies with at least {{ stars }} stars.</h2>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>movie.get_movies_with_user_ratings_above(stars=int, limit=int)</code>.
        </div>
        <div class="col-sm-6">
            <h3>Code</h3>
            <pre>{{ code }}</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Movies:</h2>
        <table class="table table-striped">
        <tr><th>#</th><th>Vertex ID</th><th>Movie Title</th></tr>
        {% for m in movies %}
            <tr><td><a href="/movie/{{ m.id }}">{{ loop.index }}</a></td>
                <td><a href="/movie/{{ m.id }}">{{ m.id }}</a></td>
                <td><a href="/movie/{{ m.id }}">{{ m.title }}</a></td></tr>
        {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock %}