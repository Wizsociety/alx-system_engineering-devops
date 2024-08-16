# Fixing Apach var/www/html/wp-content/object-cache.php" file not available

exec { 'fix-wordpress':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
  path	   => '/usr/local/bin/:bin/'
}
