#!/bin/sh
set -e
package=PHP_CodeSniffer
svn=http://svn.php.net/repository/pear/packages/$package

svn checkout $svn/trunk $package
pear package $package/package.xml
