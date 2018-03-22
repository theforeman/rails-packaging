# Generated from loofah-2.1.1.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name loofah

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.1
Release: 3%{?dist}
Summary: Loofah is a general library for manipulating and transforming HTML/XML documents and fragments
Group:   Development/Languages
License: MIT
URL:     https://github.com/flavorjones/loofah
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.5.9
Requires: %{?scl_prefix}rubygem(crass) >= 1.0.2
Requires: %{?scl_prefix}rubygem(crass) < 1.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Loofah is a general library for manipulating and transforming HTML/XML
documents and fragments. It's built on top of Nokogiri and libxml2, so
it's fast and has a nice API.
Loofah excels at HTML sanitization (XSS prevention). It includes some
nice HTML sanitizers, which are based on HTML5lib's whitelist, so it
most likely won't make your codes less secure. (These statements have
not been evaluated by Netexperts.)
ActiveRecord extensions for sanitization are available in the
`loofah-activerecord` gem (see
https://github.com/flavorjones/loofah-activerecord).


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gemtest
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_instdir}/Manifest.txt
%{gem_instdir}/benchmark
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.1.1-3
- rebuilt

* Mon Nov 20 2017 Eric D. Helms <ericdhelms@gmail.com> - 2.1.1-1
- Initial package
