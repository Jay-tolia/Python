<?php
// Example of fetching course data from a MySQL database and generating HTML

$host = 'localhost';
$username = 'your_db_username';
$password = 'your_db_password';
$dbname = 'your_db_name';

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
  die('Connection failed: ' . $conn->connect_error);
}

$sql = 'SELECT id, title, description FROM courses';
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    echo '<div class="course-card">';
    echo '<h2>' . $row['title'] . '</h2>';
    echo '<p>' . $row['description'] . '</p>';
    echo '</div>';
  }
} else {
  echo 'No courses available.';
}

$conn->close();
?>
