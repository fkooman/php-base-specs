%global composer_vendor         fkooman
%global composer_project        tpl
%global composer_namespace      %{composer_vendor}/Tpl

%global github_owner            fkooman
%global github_name             php-lib-tpl
%global github_commit           d6abca430ff050890f93eb353158b8ed3dc91bf4
%global github_short            %(c=%{github_commit}; echo ${c:0:7})


Name:       php-%{composer_vendor}-%{composer_project}
Version:    2.1.0
Release:    1%{?dist}
Summary:    Simple Template Abstraction Library

Group:      System Environment/Libraries
License:    ASL 2.0

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_short}.tar.gz
Source1:    %{name}-autoload.php

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Requires:   php(language) >= 5.3.3
Requires:   php-standard

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Simple Template Abstraction Library.

%prep
%setup -qn %{github_name}-%{github_commit} 
cp %{SOURCE1} src/%{composer_namespace}/autoload.php

%build

%install
rm -rf %{buildroot} 
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/php/%{composer_namespace}
%doc README.md CHANGES.md composer.json
%{!?_licensedir:%global license %%doc} 
%license COPYING

%changelog
* Thu Feb 04 2016 François Kooman <fkooman@tuxed.net> - 2.1.0-1
- update to 2.1.0

* Tue Sep 08 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-3
- change source0 to commit reference
- other cleanups

* Thu Sep 03 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-2
- add autoloader

* Mon Aug 10 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- update to 2.0.0

* Thu Jul 30 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Thu Jul 30 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- update to 1.0.0
