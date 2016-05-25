%global composer_vendor         fkooman
%global composer_project        rest-plugin-authentication-indieauth
%global composer_namespace      %{composer_vendor}/Rest/Plugin/Authentication/IndieAuth

%global github_owner            fkooman
%global github_name             php-lib-rest-plugin-authentication-indieauth
%global github_commit           77878aa6c5650004156a1088ebb72e08e238216b
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    2.0.2
Release:    1%{?dist}
Summary:    IndieAuth Authentication plugin for fkooman/rest

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if %{with_tests}
BuildRequires:  php(language) >= 5.4.0
BuildRequires:  php-dom
BuildRequires:  php-filter
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-standard
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/http) >= 1.0.0
BuildRequires:  php-composer(fkooman/http) < 2.0.0
BuildRequires:  php-composer(fkooman/io) >= 2.0.0
BuildRequires:  php-composer(fkooman/io) < 3.0.0
BuildRequires:  php-composer(fkooman/json) >= 2.0.0
BuildRequires:  php-composer(fkooman/json) < 3.0.0
BuildRequires:  php-composer(fkooman/rest) >= 1.0.1
BuildRequires:  php-composer(fkooman/rest) < 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) < 3.0.0
BuildRequires:  php-composer(fkooman/tpl) >= 2.0.0
BuildRequires:  php-composer(fkooman/tpl) < 3.0.0
BuildRequires:  php-composer(guzzlehttp/guzzle) >= 5.3
BuildRequires:  php-composer(guzzlehttp/guzzle) < 6.0
%endif

Requires:   php(language) >= 5.4.0
Requires:   php-dom
Requires:   php-filter
Requires:   php-libxml
Requires:   php-pcre
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(fkooman/http) >= 1.0.0
Requires:   php-composer(fkooman/http) < 2.0.0
Requires:   php-composer(fkooman/io) >= 2.0.0
Requires:   php-composer(fkooman/io) < 3.0.0
Requires:   php-composer(fkooman/json) >= 2.0.0
Requires:   php-composer(fkooman/json) < 3.0.0
Requires:   php-composer(fkooman/rest) >= 1.0.1
Requires:   php-composer(fkooman/rest) < 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) < 3.0.0
Requires:   php-composer(fkooman/tpl) >= 2.0.0
Requires:   php-composer(fkooman/tpl) < 3.0.0
Requires:   php-composer(guzzlehttp/guzzle) >= 5.3
Requires:   php-composer(guzzlehttp/guzzle) < 6.0

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Library written in PHP to make it easy to develop REST applications.

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
* Wed May 25 2016 François Kooman <fkooman@tuxed.net> - 2.0.2-1
- update to 2.0.2

* Fri Mar 25 2016 François Kooman <fkooman@tuxed.net> - 2.0.1-1
- update to 2.0.1

* Fri Jan 22 2016 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Tue Oct 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.2-1
- update to 1.0.2

* Tue Oct 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-4
- no longer require workaround for php-guzzlehttp-guzzle autoloader

* Sun Sep 27 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-3
- fix autoloader for GuzzleHttp

* Mon Sep 21 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-2
- forgot to update git tag

* Mon Sep 21 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Sun Sep 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- change source0 to commit reference
- other cleanups
- add autoloader
- run tests during build

* Mon Jul 20 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
