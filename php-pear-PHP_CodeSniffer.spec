# TODO
# - save config to /etc:
# $ phpcs --config-set default_standard PEAR
# PHP Warning:  file_put_contents(/usr/share/pear/data/PHP_CodeSniffer/CodeSniffer.conf): failed to open stream: Permission denied in /usr/share/pear/PHP/CodeSniffer.php on line 1532
%define		status		stable
%define		pearname	PHP_CodeSniffer
%define		php_min_version 5.1.2
%include	/usr/lib/rpm/macros.php
Summary:	PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards
Summary(pl.UTF-8):	PHP_CodeSniffer analizuje kod PHP pod kątem naruszeń zdefiniowanych standardów kodowania
Name:		php-pear-%{pearname}
Version:	1.4.3
Release:	2
Epoch:		1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	5183c6f31cb154f4adbc4f7044a79645
Patch0:		case-sensitive.patch
Patch1:		peardeps.patch
URL:		http://pear.php.net/package/PHP_CodeSniffer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php(tokenizer)
Requires:	php-pear
Suggests:	php-phpunit-PHP_Timer
Obsoletes:	php-pear-PHP_CodeSniffer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_CodeSniffer is a PHP5 script that tokenises and "sniffs" PHP code
to detect violations of a defined set of coding standards. It is an
essential development tool that ensures that your code remains clean
and consistent. It can even help prevent some common semantic errors
made by developers.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
PHP_CodeSniffer jest skryptem PHP5 służącym do rozkładu tekstu kodu
PHP w celu wykrycia naruszeń pewnych zdefiniowanych standardów
kodowania. Jest to istotne narzędzie, dzięki któremu można zapewnić
czystość i spójność kodu. Może także pomóc w zapobieganiu popełniania
przez programistów pewnych częstych błędów semantycznych.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p .%{_bindir}/phpcs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpcs
%{php_pear_dir}/PHP/CodeSniffer
%{php_pear_dir}/PHP/CodeSniffer.php
