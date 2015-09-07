%global composer_vendor         fkooman
%global composer_project        ini
%global composer_namespace      %{composer_vendor}/Ini

%global github_owner            fkooman
%global github_name             php-lib-ini
%global github_commit           b380a88e42ce2184e822cc8b89223cd777c484be
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.0
Release:    4%{?dist}
Summary:    Handle INI configuration files

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
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Simple library for reading INI-style configuration files.

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
* Mon Sep 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-4
- change source0 to commit reference
- other cleanups

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-3
- require phpab

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- run tests on build
- include autoload script

* Mon Jul 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0

* Thu Oct 23 2014 François Kooman <fkooman@tuxed.net> - 0.2.0-1
- update to 0.2.0

* Wed Oct 22 2014 François Kooman <fkooman@tuxed.net> - 0.1.0-1
- initial package
