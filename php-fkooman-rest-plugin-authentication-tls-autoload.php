<?php

/**
 * Autoloader for fkooman/rest-plugin-authentication-tls.
 */
$vendorDir = '/usr/share/php';

// Use Symfony autoloader
if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once $vendorDir.'/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}
$fedoraClassLoader->addPrefixes(array(
    'fkooman\\Rest\\Plugin\\Authentication\\Tls' => dirname(dirname(dirname(dirname(dirname(__DIR__))))),
));

require_once $vendorDir.'/fkooman/Rest/autoload.php';
require_once $vendorDir.'/fkooman/Rest/Plugin/Authentication/autoload.php';
require_once $vendorDir.'/fkooman/Base64/autoload.php';
