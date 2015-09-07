%global composer_vendor  fkooman
%global composer_project rest-plugin-authentication-tls

%global github_owner     fkooman
%global github_name      php-lib-rest-plugin-authentication-tls

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.1
Release:    1%{?dist}
Summary:    TLS Client Certificate Authentication plugin for fkooman/rest

Group:      System Environment/Libraries
License:    ASL 2.0
URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    https://github.com/%{github_owner}/%{github_name}/archive/%{version}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Requires:   php(language) >= 5.4
Requires:   php-composer(fkooman/rest) >= 1.0.0
Requires:   php-composer(fkooman/rest) < 2.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) >= 1.0.0
Requires:   php-composer(fkooman/rest-plugin-authentication) < 2.0.0
Requires:   php-composer(fkooman/base64) >= 1.0.0
Requires:   php-composer(fkooman/base64) < 2.0.0
Requires:   php-composer(symfony/class-loader)

BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(fkooman/rest) >= 1.0.0
BuildRequires:  php-composer(fkooman/rest) < 2.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) >= 1.0.0
BuildRequires:  php-composer(fkooman/rest-plugin-authentication) < 2.0.0
BuildRequires:  php-composer(fkooman/base64) >= 1.0.0
BuildRequires:  php-composer(fkooman/base64) < 2.0.0

%description
Library written in PHP to make it easy to develop REST applications.

%prep
%setup -qn %{github_name}-%{version}
cp %{SOURCE1} src/%{composer_vendor}/Rest/Plugin/Authentication/Tls/autoload.php

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%check
%{_bindir}/phpab --output tests/bootstrap.php tests
echo 'require "%{buildroot}%{_datadir}/php/%{composer_vendor}/Rest/Plugin/Authentication/Tls/autoload.php";' >> tests/bootstrap.php
%{_bindir}/phpunit \
    --bootstrap tests/bootstrap.php

%files
%defattr(-,root,root,-)
%dir %{_datadir}/php/%{composer_vendor}/Rest/Plugin/Authentication/Tls
%{_datadir}/php/%{composer_vendor}/Rest/Plugin/Authentication/Tls/*
%doc README.md CHANGES.md composer.json
%license COPYING

%changelog
* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Fri Sep 04 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Mon Jul 20 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
