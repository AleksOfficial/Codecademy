



<h1>My First PHP Site</h1>
<p>This HTML will get delivered as is</p>
<?/*PHP used to build dynamic webpage =customized content 
this is sent from the backend to the front-end
-> ignores whitespace + not case-sensitive -> echo "Hello World!" works also as Echo "Hello World!"
// or # -> can also be a one line comment*/?>
<?php echo "<p>But this code is interpreted by PHP and turned into HTML</p>";?>
<?php echo "<ul><li>You can use any HTML tags,</li><li>like this list.</li></ul>";?>
<footer>
  <p>And this code is back in plain HTML</p>
</footer>