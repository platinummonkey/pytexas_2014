{% extends "base.tpl" %}

{% block title %} - User - Occupation Distribution{% endblock %}

{% block content %}
<div class="row">
    <h2>Get Occupation Distribution</h2>
    <div class="row">
        <div class="col-sm-6">
            <h3>Model</h3>
            Simply use <code>Occupation.get_distribution()</code>.
        </div>
        <div class="col-sm-6">
            <h3>Code</h3>
            <pre>{{ code }}</pre>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
        <h2>Occupation Distribution of Users:</h2>
        <table class="table table-striped">
        <tr><th>#</th><th>ID</th><th>Occupation</th><th>Number of Users</th></tr>
        {% for item in distribution|dictsort(False, 'value')|reverse %}
            <tr><td>{{ loop.index }}</td><td>{{ item[0].id }}</td><td>{{ item[0].occupation }}</td><td>{{ item[1] }}</td></tr>
        {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock %}