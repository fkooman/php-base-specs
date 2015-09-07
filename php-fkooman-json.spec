%global composer_vendor         fkooman
%global composer_project        json
%global composer_namespace      %{composer_vendor}/Json

%global github_owner            fkooman
%global github_name             php-lib-json
%global github_commit           2767e16032401ed2395c33282709e48b8e41cc6f
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.0
Release:    3%{?dist}
Summary:    JSON convenience library written in PHP

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
%endif

Requires:   php(language) >= 5.3.3
Requires:   php-json
Requires:   php-spl
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This is a PHP library written to make it easy and safe to process JSON.
It will throw exceptions when encoding or decoding fails.

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
* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-3
- change source0 to commit reference
- other cleanups

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Mon Jul 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0

* Wed Oct 22 2014 François Kooman <fkooman@tuxed.net> - 0.6.0-1
- update to 0.6.0 

* Tue Sep 16 2014 François Kooman <fkooman@tuxed.net> - 0.5.1-1
- update to 0.5.1

* Tue Sep 16 2014 François Kooman <fkooman@tuxed.net> - 0.5.0-1
- update to 0.5.0

* Sun Aug 31 2014 François Kooman <fkooman@tuxed.net> - 0.4.1-1
- update to 0.4.1

* Fri Aug 29 2014 François Kooman <fkooman@tuxed.net> - 0.4.0-2
- use github tagged release sources
- update group to System Environment/Libraries

* Sat Aug 16 2014 François Kooman <fkooman@tuxed.net> - 0.4.0-1
- initial package
