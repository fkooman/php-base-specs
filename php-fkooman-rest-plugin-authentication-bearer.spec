%global composer_vendor         fkooman
%global composer_project        rest-plugin-authentication-bearer
%global composer_namespace      %{composer_vendor}/Rest/Plugin/Authentication/Bearer

%global github_owner            fkooman
%global github_name             php-lib-rest-plugin-authentication-bearer
%global github_commit           f0abf30d3835a8dd39fb86899073128543067d61
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    2.2.0
Release:    1%{?dist}
Summary:    Bearer Authentication plugin for fkooman/rest

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if %{with_tests}
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-standard
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/rest) >= 1.0.0
BuildRequires:  php-composer(fkooman/rest) < 2.0.0
BuildRequires:  php-composer(fkooman/http) >= 1.3.1
BuildRequires:  php-composer(fkooman/http) < 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) < 3.0.0
BuildRequires:  php-composer(guzzlehttp/guzzle) >= 5.3
BuildRequires:  php-composer(guzzlehttp/guzzle) < 6.0
%endif

Requires:   php(language) >= 5.4
Requires:   php-pcre
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(guzzlehttp/guzzle) >= 5.3
Requires:   php-composer(guzzlehttp/guzzle) < 6.0
Requires:   php-composer(fkooman/http) >= 1.3.1
Requires:   php-composer(fkooman/http) < 2.0.0
Requires:   php-composer(fkooman/rest) >= 1.0.0
Requires:   php-composer(fkooman/rest) < 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) >= 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) < 3.0.0

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
* Thu Feb 25 2016 François Kooman <fkooman@tuxed.net> - 2.2.0-1
- update to 2.2.0

* Sat Dec 05 2015 François Kooman <fkooman@tuxed.net> - 2.1.0-1
- update to 2.1.0

* Thu Nov 19 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Sun Sep 13 2015 François Kooman <fkooman@tuxed.net>
- change source0 to commit reference
- other cleanups
- add autoloader
- run tests during build

* Mon Jul 20 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
