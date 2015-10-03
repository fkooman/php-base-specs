%global composer_vendor         fkooman
%global composer_project        io
%global composer_namespace      %{composer_vendor}/IO

%global github_owner            fkooman
%global github_name             php-lib-io
%global github_commit           0c2d8c49b1e37b9e3593c9e8dc51f4abc0c6712a
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.1
Release:    1%{?dist}
Summary:    Simple IO library

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
Requires:   php-date
Requires:   php-openssl
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Simple IO library.

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
* Sat Oct 03 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-3
- change source0 to commit reference
- other cleanups

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Tue Jul 21 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
