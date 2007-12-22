%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	CodeSniffer
%define		_status		stable
%define		_pearname	PHP_CodeSniffer
Summary:	%{_pearname} - PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards
Summary(pl):	%{_pearname} - PHP_CodeSniffer analizuje kod PHP pod kątem naruszeń zdefiniowanych standardów kodowania
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	38c4b9e522a9588fcddcae9ff70c84f7
URL:		http://pear.php.net/package/PHP_CodeSniffer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install .%{_bindir}/phpcs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpcs
%{php_pear_dir}/PHP/CodeSniffer/
%{php_pear_dir}/PHP/CodeSniffer.php
%{php_pear_dir}/data/PHP_CodeSniffer/

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_CodeSniffer
