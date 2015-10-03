%global composer_vendor         yosymfony
%global composer_project        toml
%global composer_namespace      Yosymfony/Toml

%global github_owner            yosymfony
%global github_name             Toml
%global github_commit           b0a28913e488389b6a088c2893c83037d80ec020
%global github_short            %(c=%{github_commit}; echo ${c:0:7})

%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    0.3.3
Release:    1%{?dist}
Summary:    A PHP parser for TOML

Group:      System Environment/Libraries
License:    MIT

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-standard
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
%endif

Requires:   php(language) >= 5.3.0
Requires:   php-date
Requires:   php-json
Requires:   php-pcre
Requires:   php-spl
Requires:   php-standard
Requires:   php-composer(symfony/class-loader)
    
Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A PHP parser for TOML compatible with specification 0.4.0.

%prep
%setup -qn %{github_name}-%{github_commit} 
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
* Wed Sep 30 2015 François Kooman <fkooman@tuxed.net> - 0.3.3-1
- initial package
