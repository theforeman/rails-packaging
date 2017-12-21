# Generated from mime-types-data-3.2016.0521.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name mime-types-data

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2016.0521
Release: 1%{?dist}
Summary: mime-types-data provides a registry for information about MIME media type definitions
Group:   Development/Languages
License: MIT
URL:     https://github.com/mime-types/mime-types-data/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


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
%{gem_instdir}/Code-of-Conduct.md
%license %{gem_instdir}/Licence.md
%{gem_instdir}/Manifest.txt
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributing.md
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Dec 21 2017 Eric D. Helms <ericdhelms@gmail.com> - 3.2016.0521-1
- Initial package
