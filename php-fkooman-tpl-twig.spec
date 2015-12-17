%global composer_vendor         fkooman
%global composer_project        tpl-twig
%global composer_namespace      %{composer_vendor}/Tpl/Twig

%global github_owner            fkooman
%global github_name             php-lib-tpl-twig
%global github_commit           c1f50f49ffe430b12e36c2a8e5441cd87830484a
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.1.0
Release:    1%{?dist}
Summary:    Twig for Simple Template Abstraction Library

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
BuildRequires:  php-composer(fkooman/tpl) >= 2.0.0
BuildRequires:  php-composer(fkooman/tpl) < 3.0.0
BuildRequires:  php-pear(pear.twig-project.org/Twig) >= 1.18
BuildRequires:  php-pear(pear.twig-project.org/Twig) < 2.0
%endif

Requires:   php(language) >= 5.3.0
Requires:   php-json
Requires:   php-spl
Requires:   php-composer(symfony/class-loader)
Requires:   php-composer(fkooman/tpl) >= 2.0.0
Requires:   php-composer(fkooman/tpl) < 3.0.0
Requires:   php-pear(pear.twig-project.org/Twig) >= 1.18
Requires:   php-pear(pear.twig-project.org/Twig) < 2.0

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Twig for Simple Template Abstraction Library.

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
* Thu Dec 17 2015 François Kooman <fkooman@tuxed.net> - 1.1.0-1
- update to 1.1.0

* Tue Sep 08 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-3
- change source0 to commit reference
- other cleanups

* Fri Sep 04 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- add autoloader
- run tests during build

* Mon Aug 10 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
