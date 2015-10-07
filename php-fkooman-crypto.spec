%global composer_vendor         fkooman
%global composer_project        crypto
%global composer_namespace      %{composer_vendor}/Crypto

%global github_owner            fkooman
%global github_name             php-lib-crypto
%global github_commit           c448f4ebf7246160e537a63a6be711ee1d8f2a37
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    2.0.0
Release:    1%{?dist}
Summary:    A simple encryption and decryption library

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 


%if %{with_tests}
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-hash
BuildRequires:  php-pcre
BuildRequires:  php-openssl
BuildRequires:  php-spl
BuildRequires:  php-standard
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/base64) >= 1.0
BuildRequires:  php-composer(fkooman/base64) < 2.0
BuildRequires:  php-composer(fkooman/io) >= 1.0
BuildRequires:  php-composer(fkooman/io) < 2.0
BuildRequires:  php-composer(fkooman/json) >= 1.0
BuildRequires:  php-composer(fkooman/json) < 2.0
%endif

Requires:   php(language) >= 5.3.3
Requires:   php-hash
Requires:   php-pcre
Requires:   php-openssl
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(fkooman/base64) >= 1.0
Requires:   php-composer(fkooman/base64) < 2.0
Requires:   php-composer(fkooman/io) >= 1.0
Requires:   php-composer(fkooman/io) < 2.0
Requires:   php-composer(fkooman/json) >= 1.0
Requires:   php-composer(fkooman/json) < 2.0
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A simple symmetric encryption and decryption library using secure hashes with 
zero configuration.

%prep
%setup -qn %{github_name}-%{github_commit} 
cp %{SOURCE1} src/%{composer_namespace}/autoload.php

%build

%install
rm -rf %{buildroot} 
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%if %{with_tests} 
%check
%{_bindir}/phpab --output tests/bootstrap.php tests
echo 'require "%{buildroot}%{_datadir}/php/%{composer_namespace}/autoload.php";' >> tests/bootstrap.php
%{_bindir}/phpunit \
    --bootstrap tests/bootstrap.php
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/php/%{composer_namespace}
%doc README.md CHANGES.md composer.json
%{!?_licensedir:%global license %%doc} 
%license COPYING

%changelog
* Wed Oct 07 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Tue Sep 15 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1
- change source0 to commit reference
- other cleanups

* Fri Sep 04 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Mon Jul 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
