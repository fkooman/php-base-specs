%global composer_vendor  fkooman
%global composer_project tpl-twig

%global github_owner     fkooman
%global github_name      php-lib-tpl-twig

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.0
Release:    2%{?dist}
Summary:    Twig for Simple Template Abstraction Library

Group:      System Environment/Libraries
License:    ASL 2.0
URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    https://github.com/%{github_owner}/%{github_name}/archive/%{version}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Requires:   php(language) >= 5.3.3
Requires:   php-spl
Requires:   php-standard

Requires:   php-composer(fkooman/tpl) >= 2.0.0
Requires:   php-composer(fkooman/tpl) < 3.0.0
Requires:   php-pear(pear.twig-project.org/Twig) >= 1.18
Requires:   php-pear(pear.twig-project.org/Twig) < 2.0
Requires:   php-composer(symfony/class-loader)

BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/tpl) >= 2.0.0
BuildRequires:  php-composer(fkooman/tpl) < 3.0.0
BuildRequires:  php-pear(pear.twig-project.org/Twig) >= 1.18
BuildRequires:  php-pear(pear.twig-project.org/Twig) < 2.0

%description
Simple Template Abstraction Library.

%prep
%setup -qn %{github_name}-%{version}
cp %{SOURCE1} src/%{composer_vendor}/Tpl/Twig/autoload.php

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%check
%{_bindir}/phpab --output tests/bootstrap.php tests
echo 'require "%{buildroot}%{_datadir}/php/%{composer_vendor}/Tpl/Twig/autoload.php";' >> tests/bootstrap.php
%{_bindir}/phpunit \
    --bootstrap tests/bootstrap.php

%files
%defattr(-,root,root,-)
%dir %{_datadir}/php/%{composer_vendor}/Tpl/Twig
%{_datadir}/php/%{composer_vendor}/Tpl/Twig
%doc README.md CHANGES.md composer.json
%license COPYING

%changelog
* Fri Sep 04 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Mon Aug 10 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
