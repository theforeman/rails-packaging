# Generated from railties-5.1.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name railties

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.4
Release: 2%{?dist}
Summary: Tools for creating, working with, and running Rails applications
Group:   Development/Languages
License: MIT
URL:     http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(rake)
Requires: %{?scl_prefix}rubygem(thor)
Requires: %{?scl_prefix}rubygem(method_source)
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(actionpack) = %{version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildRequires: %{?scl_prefix}rubygem(actionview) = %{version}
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Rails internals: application bootup, plugins, generators, and rake tasks.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rails
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RDOC_MAIN.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Nov 22 2017 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-1
- Initial package
