# Generated from tzinfo-1.2.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name tzinfo

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.4
Release: 3%{?dist}
Summary: Daylight savings aware timezone library
Group:   Development/Languages
License: MIT
URL:     http://tzinfo.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix}rubygem(thread_safe)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.8.7
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
TZInfo provides daylight savings aware transformations between times in
different time zones.


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
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/CHANGES.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/tzinfo.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.2.4-3
- rebuilt

* Mon Nov 20 2017 Eric D. Helms <ericdhelms@gmail.com> - 1.2.4-1
- Initial package
