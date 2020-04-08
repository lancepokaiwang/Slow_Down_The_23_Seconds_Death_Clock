<?php
ini_set('memory_limit', '-1');



header('Content-Type: text/html; charset=utf-8');
//設定時區
date_default_timezone_set('Asia/Taipei');

//引入函式庫
include 'excel-reader/PHPExcel.php';


function loadData($file){
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "ns";

    //設定要被讀取的檔案
    $file = $file;
    try {
        $objPHPExcel = PHPExcel_IOFactory::load($file);
    } catch(Exception $e) {
        die('Error loading file "'.pathinfo($file,PATHINFO_BASENAME).'": '.$e->getMessage());
    }

    $sheetData = $objPHPExcel->getActiveSheet()->toArray(null,true,true,true);


//取得欄位與行列的值
    $firstLine = true;
    foreach($sheetData as $key => $col)
    {
        $data = array();
        if($firstLine == false){
            foreach ($col as $colkey => $colvalue) {
                switch ($colkey) {
                    case "A":
                        $data['collision_date'] = $colvalue;
                        break;
                    case "B":
                        $data['hour_of_day'] = $colvalue;
                        break;
                    case "C":
                        $data['light_condition'] = $colvalue;
                        break;
                    case "D":
                        $data['road_classification'] = $colvalue;
                        break;
                    case "E":
                        $data['severity'] = $colvalue;
                        break;
                    case "F":
                        $data['weather'] = $colvalue;
                        break;
                    case "G":
                        $data['road_surface'] = $colvalue;
                        break;
                    case "H":
                        $data['collision_config'] = $colvalue;
                        break;
                    default:
                        break;
                }
            }
        }
        if(!$firstLine){
            if($data['collision_date'] != null && $data['hour_of_day'] != null && $data['light_condition'] != null){
                try {
                    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
                    // set the PDO error mode to exception
                    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                    $sql = "INSERT INTO row(collision_date, hour_of_day, light_condition, road_classification, severity, weather, road_surface, collision_config) 
VALUES ('".$data['collision_date']."','".$data['hour_of_day']."','".$data['light_condition']."','".$data['road_classification']."','".$data['severity']."','".$data['weather']."','".$data['road_surface']."','".$data['collision_config']."')";
                    // use exec() because no results are returned
                    $conn->exec($sql);
                }
                catch(PDOException $e)
                {
                    echo $sql . "<br>" . $e->getMessage();
                }
                $conn = null;
            }
        }
        $firstLine = false;
    }
}

loadData('../data/ns/2010-2013.xlsx');
loadData('../data/ns/2014-2018.xlsx');