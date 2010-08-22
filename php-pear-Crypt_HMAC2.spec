%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	HMAC2
%define		_status		stable
%define		_pearname	Crypt_HMAC2
Summary:	%{_pearname} - Implementation of Hashed Message Authentication Code for PHP5
Summary(pl.UTF-8):	%{_pearname} - implementacja kodu HMAC (Hashed Message Authentication Code) dla PHP5
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a409494b0baad6da364424f1e18bcc0f
URL:		http://pear.php.net/package/Crypt_HMAC2/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Hashed Message Authentication Code for PHP5. This
package may use the hash or mhash extensions when enabled to extend
the range of cryptographic hash functions beyond the natively
implemented MD5 and SHA1.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja kodu Hashed Message Authentication Code dla PHP5. Pakiet
może skorzystać z modułów hash oraz mhash w celu poszerzenia zakresu
kryptograficznych funkcji skrótu poza natywnie zaimplementowane MD5
oraz SHA1.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

rm .%{php_pear_dir}/generate_package_xml.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Crypt_HMAC2/docs/intro.xml
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Crypt/HMAC2
%{php_pear_dir}/Crypt/HMAC2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Crypt_HMAC2
