%global composer_vendor         fkooman
%global composer_project        rest
%global composer_namespace      %{composer_vendor}/Rest

%global github_owner            fkooman
%global github_name             php-lib-rest
%global github_commit           17930fcdd581743528448d37d3f9c70c0fb0e63f
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.6
Release:    1%{?dist}
Summary:    Simple PHP library for writing REST services

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  php-composer(fkooman/http) >= 1.1.0
BuildRequires:  php-composer(fkooman/http) < 2.0.0
%endif

Requires:   php(language) >= 5.3.0
Requires:   php-pcre
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)
Requires:   php-composer(fkooman/http) >= 1.1.0
Requires:   php-composer(fkooman/http) < 2.0.0

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
* Thu Jan 07 2016 François Kooman <fkooman@tuxed.net> - 1.0.6-1
- update to 1.0.6

* Wed Oct 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.5-1
- update to 1.0.5

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.4-1
- update to 1.0.4

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.3-1
- update to 1.0.3

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 1.0.2-2
- add autoloader
- run tests during build

* Wed Aug 05 2015 François Kooman <fkooman@tuxed.net> - 1.0.2-1
- update to 1.0.2

* Mon Jul 20 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Sun Jul 19 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
