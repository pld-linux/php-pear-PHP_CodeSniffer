# TODO
# - save config to /etc:
# $ phpcs --config-set default_standard PEAR
# PHP Warning:  file_put_contents(/usr/share/pear/data/PHP_CodeSniffer/CodeSniffer.conf): failed to open stream: Permission denied in /usr/share/pear/PHP/CodeSniffer.php on line 1532
%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	PHP_CodeSniffer
%define		php_min_version 5.1.2
%define		subver	RC2
%define		rel		0.1
Summary:	PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards
Summary(pl.UTF-8):	PHP_CodeSniffer analizuje kod PHP pod kątem naruszeń zdefiniowanych standardów kodowania
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
#Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
Source0:	%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	699eb3fc4e9650b5608fdf7a4067fdf3
Patch0:		case-sensitive.patch
URL:		http://pear.php.net/package/PHP_CodeSniffer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pear
Suggests:	php-pear-PHP_Timer
Obsoletes:	php-pear-PHP_CodeSniffer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq pear(PHP/CodeSniffer/../CodeSniffer.php) pear($dir/{$standard}CodingStandard.php) pear(PHP/Timer.*)

%description
PHP_CodeSniffer is a PHP5 script that tokenises and "sniffs" PHP code
to detect violations of a defined set of coding standards. It is an
essential development tool that ensures that your code remains clean
and consistent. It can even help prevent some common semantic errors
made by developers.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_CodeSniffer jest skryptem PHP5 służącym do rozkładu tekstu kodu
PHP w celu wykrycia naruszeń pewnych zdefiniowanych standardów
kodowania. Jest to istotne narzędzie, dzięki któremu można zapewnić
czystość i spójność kodu. Może także pomóc w zapobieganiu popełniania
przez programistów pewnych częstych błędów semantycznych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p .%{_bindir}/phpcs $RPM_BUILD_ROOT%{_bindir}

# tests should not be packaged
%{__rm} -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpcs
%{php_pear_dir}/PHP/CodeSniffer
%{php_pear_dir}/PHP/CodeSniffer.php

%{php_pear_dir}/data/PHP_CodeSniffer
