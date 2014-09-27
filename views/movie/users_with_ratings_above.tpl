{% extends "base.tpl" %}

{% block title %} - Movie - Users With Ratings above {{ stars }}{% endblock %}

{% block content %}
<div class="row">
    <h2>Get {{ limit }} Users who Rated other movies with at least {{ stars }} stars.</h2>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>movie.get_users_given_movie_with_rating_above(stars=int, limit=int)</code>.
        </div>
        <div class="col-sm-6">
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