{% extends "base.tpl" %}

{% block title %} - Home{% endblock %}

{% block content %}
<h2>Welcome to GMDB</h2>

<table class="table table-striped">
    <tr><th>Statistic</th><th>Value</th></tr>
    <tr><td>Total Number of Vertices</td><td>{{ vertexCount }}</td></tr>
    <tr><td>Total Number of Edges</td><td>{{ edgeCount }}</td></tr>
    <tr><td>Number of Movies</td><td>{{ movieCount }}</td></tr>
    <tr><td>Number of Users</td><td>{{ userCount }}</td></tr>
    <tr><td>Number of Occupations</td><td>{{ occupationCount }}</td></tr>
</table>
{% endblock %}