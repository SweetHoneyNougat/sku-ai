<?php
    $password = $_POST['password'];
    $password = escapeshellarg($password); // 문자열을 안전한 Shell 인수로 변환

    $obj = new stdClass();
    $obj->code = $password;
    $obj->feature = shell_exec("python3 feature_extraction.py $password"); // 특징 추출하는 Python 코드 실행

    $json = json_encode($obj);
    echo $json;
?>
