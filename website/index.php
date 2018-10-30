<?php include('php_functions.php') ?>
<html>
  <head>
    <title>Outil Respo Web</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <link rel="stylesheet" href="assets/css/custom.css" />
    <link rel="icon" type="image/png" href="images/icon.png" />
  </head>
  <body class="is-preload">

    <!-- Nav -->
    <nav id="nav">
      <ul class="container">
        <li><a href="#info">Informations</a></li>
        <li><a href="#adh">Adhérents</a></li>
        <li><a href="#hosting">Hosting</a></li>
        <li><a href="#dev_rev">Dev Revproxy</a></li>
        <li><a href="#dev">Dev</a></li>
        <li><a href="#prod_rev">Prod Revproxy</a></li>
        <li><a href="#prod">Prod</a></li>
      </ul>
    </nav>

    <!-- Home -->
    <article id="info" class="wrapper style1">
      <div class="container">
        <div class="row">
          <div class="col-8 col-7-large col-12-medium">
            <header>
              <h1>L'outil du <strong>Respo Web MiNET</strong>.</h1>
            </header>
            <p style="padding: 2em;">
            Le respo web est “responsable” du contenu hébergé par MiNET, que ce soit les associations ou les utilisateurs. Il faut donc vérifier qu'un contenu hébergé sur notre réseau ne soit pas en contradiction avec la loi (films/musiques protégées …)

            Dans l'absolu il faut:
            <ul class="ul-width-margin">
            <li> Vérifier le contenu des pages MiNET.</li>
              <li> Vérifier le contenu des sites web hébergés par Hosting.</li>
              <li> Vérifier le contenu des sites web auto hébergés par les adhérents.</li>
              <li> Vérifier le contenu des ftps anonymes ayant un port non filtré par kickass </li>
            </ul>
            </p>
            <a href="https://github.com/zteeed/SNWT/" class="button large scrolly">Contribution au projet &nbsp;<i class="fa fa-github" aria-hidden="true"></i></a>
          </div>
          <div class="col-4 col-5-large col-12-medium">
            <span class="image fit"><img src="images/minet.png" alt="" /></span>
            <span class="image fit"><img src="images/minet.png" alt="" /></span>
          </div>
        </div>
      </div>
    </article>

    <article id="adh" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Adhérents</h2>
        </header>
        <?php $arr = get_scan_info('adhérent') ?>
        <div class="row aln-center">
          <?php display_data_scan($arr) ?>
        </div>
      </div>
    </article>

    <article id="hosting" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Hosting</h2>
        </header>
        <?php $arr = get_hosting_info() ?>
        <div class="row aln-center">
          <?php display_data_hosting($arr) ?>
        </div>
      </div>
    </article>

    <article id="dev_rev" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Dev Revproxy</h2>
        </header>
        <div class="row aln-center">
        </div>
      </div>
    </article>

    <article id="dev" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Dev</h2>
        </header>
        <?php $arr = get_scan_info('développement') ?>
        <div class="row aln-center">
          <?php display_data_scan($arr) ?>
        </div>
      </div>
    </article>

    <article id="prod_rev" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Prod Revproxy</h2>
        </header>
        <div class="row aln-center">
        </div>
      </div>
    </article>

    <article id="prod" class="wrapper style2">
      <div class="container">
        <header>
          <h2>Prod</h2>
        </header>
        <?php $arr = get_scan_info('production') ?>
        <div class="row aln-center">
          <?php display_data_scan($arr) ?>
        </div>
      </div>
    </article>

    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/jquery.scrolly.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
    <script src="assets/js/custom.js"></script>

  </body>
</html>
