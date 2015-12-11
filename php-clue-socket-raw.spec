%global composer_vendor         clue
%global composer_project        socket-raw
%global composer_namespace      Socket/Raw

%global github_owner            clue
%global github_name             php-socket-raw
%global github_commit           8a10282bcb1e45e076a8a8285237681380e55ea5
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.2.0
Release:    1%{?dist}
Summary:    Simple and lightweight OOP wrapper for PHP's low level sockets extension

Group:      System Environment/Libraries
License:    MIT

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

Patch0:     %{name}-remove-autoload-from-test.diff

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
%endif

Requires:   php(language) >= 5.3
Requires:   php-sockets
Requires:   php-composer(symfony/class-loader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Simple and lightweight OOP wrapper for PHP's low level sockets extension 
(ext-sockets).

%prep
%setup -qn %{github_name}-%{github_commit} 
%patch0 -p1
cp %{SOURCE1} src/autoload.php

%build

%install
rm -rf %{buildroot} 
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php/%{composer_namespace}
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php/%{composer_namespace}

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
%doc README.md CHANGELOG.md composer.json
%{!?_licensedir:%global license %%doc} 
%license LICENSE

%changelog
* Fri Dec 11 2015 François Kooman <fkooman@tuxed.net> - 1.2.0-1
- initial package
