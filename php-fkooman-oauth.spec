%global composer_vendor         fkooman
%global composer_project        oauth
%global composer_namespace      %{composer_vendor}/OAuth

%global github_owner            fkooman
%global github_name             php-lib-oauth
%global github_commit           1878a89f196c5ac6d4e450018f1b5470b3b7991b
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    5.2.1
Release:    1%{?dist}
Summary:    OAuth 2.0 Authorization Server library

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-pdo
BuildRequires:  php-spl
BuildRequires:  php-standard
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/json) >= 2.0.0
BuildRequires:  php-composer(fkooman/json) < 3.0.0
BuildRequires:  php-composer(fkooman/http) >= 1.1.0
BuildRequires:  php-composer(fkooman/http) < 2.0.0
BuildRequires:  php-composer(fkooman/io) >= 2.0.0
BuildRequires:  php-composer(fkooman/io) < 3.0.0
BuildRequires:  php-composer(fkooman/rest) >= 1.0.0
BuildRequires:  php-composer(fkooman/rest) < 2.0.0
BuildRequires:  php-composer(fkooman/tpl) >= 2.0.0
BuildRequires:  php-composer(fkooman/tpl) < 3.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) < 3.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication-basic) >= 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication-basic) < 3.0.0
BuildRequires:  php-composer(fkooman/base64) >= 1.0.0
BuildRequires:  php-composer(fkooman/base64) < 2.0.0
%endif

Requires:   php(language) >= 5.4
Requires:   php-filter
Requires:   php-pcre
Requires:   php-pdo
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(fkooman/json) >= 2.0.0
Requires:   php-composer(fkooman/json) < 3.0.0
Requires:   php-composer(fkooman/io) >= 2.0.0
Requires:   php-composer(fkooman/io) < 3.0.0
Requires:   php-composer(fkooman/http) >= 1.1.0
Requires:   php-composer(fkooman/http) < 2.0.0
Requires:   php-composer(fkooman/rest) >= 1.0.0
Requires:   php-composer(fkooman/rest) < 2.0.0
Requires:   php-composer(fkooman/tpl) >= 2.0.0
Requires:   php-composer(fkooman/tpl) < 3.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) < 3.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication-basic) >= 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication-basic) < 3.0.0
Requires:   php-composer(fkooman/base64) >= 1.0.0
Requires:   php-composer(fkooman/base64) < 2.0.0
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
OAuth 2.0 Authorization Server library.

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
%doc README.md CHANGES.md INTEROPERABILITY.md composer.json
%{!?_licensedir:%global license %%doc} 
%license COPYING

%changelog
* Wed Aug 10 2016 François Kooman <fkooman@tuxed.net> - 5.2.1-1
- update to 5.2.1

* Wed Aug 10 2016 François Kooman <fkooman@tuxed.net> - 5.2.0-1
- update to 5.2.0

* Sun Aug 07 2016 François Kooman <fkooman@tuxed.net> - 5.1.2-1
- update to 5.1.2

* Wed May 25 2016 François Kooman <fkooman@tuxed.net> - 5.1.1-1
- update to 5.1.1

* Wed Mar 30 2016 François Kooman <fkooman@tuxed.net> - 5.1.0-1
- update to 5.1.0

* Fri Mar 25 2016 François Kooman <fkooman@tuxed.net> - 5.0.3-1
- update to 5.0.3

* Fri Mar 25 2016 François Kooman <fkooman@tuxed.net> - 5.0.2-1
- update to 5.0.2

* Tue Nov 24 2015 François Kooman <fkooman@tuxed.net> - 5.0.1-1
- update to 5.0.1

* Thu Nov 19 2015 François Kooman <fkooman@tuxed.net> - 5.0.0-1
- update to 5.0.0

* Wed Nov 18 2015 François Kooman <fkooman@tuxed.net> - 4.0.1-1
- update to 4.0.1

* Tue Nov 03 2015 François Kooman <fkooman@tuxed.net> - 4.0.0-1
- update to 4.0.0

* Tue Oct 27 2015 François Kooman <fkooman@tuxed.net> - 3.0.0-1
- update to 3.0.0

* Thu Oct 15 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-2
- also require fkooman/base64

* Thu Oct 15 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Mon Sep 21 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- release 1.0.0
