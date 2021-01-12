<?php 
move_uploaded_file($_FILES["testSubmit"]["tmp_name"], "test.wav");
exec("python speechAPI.py");

echo "success";
?>