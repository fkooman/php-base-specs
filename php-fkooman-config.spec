%global composer_vendor         fkooman
%global composer_project        config
%global composer_namespace      %{composer_vendor}/Config

%global github_owner            fkooman
%global github_name             php-lib-config
%global github_commit           92eb45e9c32b9fc41d25824dc47d9462b990085c
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.1.0
Release:    1%{?dist}
Summary:    Read and write configuration files

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
BuildRequires:  php-composer(symfony/yaml)
%endif

Requires:   php(language) >= 5.4
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)
Requires:   php-composer(symfony/yaml)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Simple library for reading and writing configuration files.

Supported formats:
* INI
* YAML

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
* Wed Aug 10 2016 François Kooman <fkooman@tuxed.net> - 1.1.0-1
- update to 1.1.0

* Thu May 19 2016 François Kooman <fkooman@tuxed.net> - 1.0.2-1
- update to 1.0.2

* Wed Apr 27 2016 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Mon Nov 09 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-3
- point to old autoloader.php instead of autoload.php as it is missing in el7

* Mon Nov 09 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- fix autoloader to require symfony/yaml

* Mon Nov 09 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
