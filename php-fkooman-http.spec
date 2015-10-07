%global composer_vendor         fkooman
%global composer_project        http
%global composer_namespace      %{composer_vendor}/Http

%global github_owner            fkooman
%global github_name             php-lib-http
%global github_commit           c21cf15653c0d190da0590a015e0e6702cbcc8c3
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.1.0
Release:    1%{?dist}
Summary:    Simple PHP library for dealing with HTTP requests and responses

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
BuildRequires:  php-composer(fkooman/json) >= 1.0.0
BuildRequires:  php-composer(fkooman/json) < 2.0.0
%endif

Requires:   php(language) >= 5.3.0
Requires:   php-mbstring
Requires:   php-session
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)
Requires:   php-composer(fkooman/json) >= 1.0.0
Requires:   php-composer(fkooman/json) < 2.0.0

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Helper library for fkooman/rest to deal with HTTP requests and responses.

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
* Wed Oct 07 2015 François Kooman <fkooman@tuxed.net> - 1.1.0-1
- update to 1.1.0

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-2
- update the commit

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add additional BuildRequires

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
