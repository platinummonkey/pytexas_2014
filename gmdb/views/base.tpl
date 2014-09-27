<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- link rel="icon" href="../../favicon.ico" -->

    <title>GMDB{% block title %}{% endblock %}</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/static/css/sticky-footer-navbar.css" rel="stylesheet"

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">GMDB</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">User <span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="/user/meanAge">Mean Age</a></li>
                <li><a href="/user/occupations">Occupation Distribution</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Movie <span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="/movie/256">Movie</a></li>
                <li><a href="/movie/256/usersWithRatingsAbove">Users who Rated</a></li>
                <li><a href="/movie/256/moviesWithRatingsAbove">Movies from Users who Rated</a></li>
                <li><a href="/movie/256/coratedMovie">Corated Movies</a></li>
                <li><a href="/movie/256/coratedMovieByGenre">Corated Movies by Genre</a></li>
                <li><a href="/movie/256/coratedMovieByAllGenre">Corated Movies by All Genres</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <!-- Begin page content -->
    <div class="container">
      {% block content %}
      <div class="page-header">
        <h1>Sticky footer with fixed navbar</h1>
      </div>
      <p class="lead">Pin a fixed-height footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS. A fixed navbar has been added with <code>padding-top: 60px;</code> on the <code>body > .container</code>.</p>
      <p>Back to <a href="../sticky-footer">the default sticky footer</a> minus the navbar.</p>
      {% endblock %}
    </div>

    <div class="footer">
      <div class="container">
        {% block footer %}<p class="text-muted">GMDB - The &quot;popular&quot; Graph-based Movie DataBase</p>{% endblock %}
      </div>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    {% block javascript %}{% endblock %}
  </body>
</html>