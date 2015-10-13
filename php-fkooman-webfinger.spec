%global composer_vendor         fkooman
%global composer_project        webfinger
%global composer_namespace      %{composer_vendor}/WebFinger

%global github_owner            fkooman
%global github_name             php-lib-webfinger
%global github_commit           8a802d6a3d946a0e24dec2db92854edf47b96fc4
%global github_short            %(c=%{github_commit}; echo ${c:0:7})
%if 0%{?rhel} == 5
%global with_tests              0%{?_with_tests:1}
%else
%global with_tests              0%{!?_without_tests:1}
%endif

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.0
Release:    2%{?dist}
Summary:    WebFinger client library

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

%if %{with_tests}
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-filter
BuildRequires:  php-spl
BuildRequires:  php-composer(symfony/class-loader)
BuildRequires:  %{_bindir}/phpunit
BuildRequires:  %{_bindir}/phpab
BuildRequires:  php-composer(guzzlehttp/guzzle) >= 5.3
BuildRequires:  php-composer(guzzlehttp/guzzle) < 6.0
%endif

Requires:   php(language) >= 5.4
Requires:   php-filter
Requires:   php-spl
Requires:   php-composer(symfony/class-loader)
Requires:   php-composer(guzzlehttp/guzzle) >= 5.3
Requires:   php-composer(guzzlehttp/guzzle) < 6.0

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This is a WebFinger (RFC 7033) client implementation written in PHP. It 
locates the WebFinger data based on a resource.

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
* Tue Oct 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- no longer require workaround for php-guzzlehttp-guzzle autoloader

* Tue Oct 06 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
