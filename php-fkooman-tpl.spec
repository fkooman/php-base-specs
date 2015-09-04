%global composer_vendor  fkooman
%global composer_project tpl

%global github_owner     fkooman
%global github_name      php-lib-tpl

Name:       php-%{composer_vendor}-%{composer_project}
Version:    2.0.0
Release:    2%{?dist}
Summary:    Simple Template Abstraction Library

Group:      System Environment/Libraries
License:    ASL 2.0
URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    https://github.com/%{github_owner}/%{github_name}/archive/%{version}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Requires:   php(language) >= 5.3.3
Requires:   php-standard

%description
Simple Template Abstraction Library.

%prep
%setup -qn %{github_name}-%{version}
cp %{SOURCE1} src/%{composer_vendor}/Tpl/autoload.php

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%files
%defattr(-,root,root,-)
%dir %{_datadir}/php/%{composer_vendor}/Tpl
%{_datadir}/php/%{composer_vendor}/Tpl
%doc README.md CHANGES.md composer.json
%license COPYING

%changelog
* Thu Sep 03 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-2
- add autoloader

* Mon Aug 10 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Thu Jul 30 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Thu Jul 30 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
