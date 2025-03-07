<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $url = $_POST["url"];
    $new_label = $_POST["new_label"];
    $output = shell_exec("python3 rename_v2ray_configs.py $url $new_label");
    echo "<h1>Modified Subscription Link</h1>";
    echo "<p>$output</p>";
}
?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>V2Ray Config Renamer</title>
  </head>
  <body>
    <h1>V2Ray Config Renamer</h1>
    <form action="" method="post">
      <label for="url">Subscription URL:</label><br>
      <input type="text" id="url" name="url" required><br><br>
      <label for="new_label">New Label:</label><br>
      <input type="text" id="new_label" name="new_label" required><br><br>
      <input type="submit" value="Rename">
    </form>
  </body>
</html>
