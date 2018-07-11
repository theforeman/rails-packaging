# Generated from arel-9.0.0.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name arel

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 9.0.0
Release: 1%{?dist}
Summary: Arel Really Exasperates Logicians  Arel is a SQL AST manager for Ruby
Group:   Development/Languages
License: MIT
URL:     https://github.com/rails/arel
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Arel Really Exasperates Logicians
Arel is a SQL AST manager for Ruby. It
1. Simplifies the generation of complex SQL queries
2. Adapts to various RDBMSes
It is intended to be a framework framework; that is, you can build your own
ORM
with it, focusing on innovative object and collection modeling as opposed to
database compatibility and query generation.


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
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 9.0.0-1
- Initial package
