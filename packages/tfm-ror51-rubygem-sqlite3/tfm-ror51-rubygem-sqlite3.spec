# Generated from sqlite3-1.3.13.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sqlite3

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.13
Release: 1%{?dist}
Summary: This module allows Ruby programs to interface with the SQLite3 database engine (http://www.sqlite.org)
Group:   Development/Languages
License: BSD-3
URL:     https://github.com/sparklemotion/sqlite3-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.3.5
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 1.8.7
BuildRequires: sqlite-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
This module allows Ruby programs to interface with the SQLite3
database engine (http://www.sqlite.org).  You must have the
SQLite engine installed in order to build this module.
Note that this module is only compatible with SQLite 3.6.16 or newer.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/Manifest.txt
%{gem_instdir}/faq
%{gem_libdir}
%{gem_instdir}/setup.rb
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/API_CHANGES.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/ChangeLog.cvs
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Nov 29 2017 Eric D. Helms <ericdhelms@gmail.com> - 1.3.13-1
- Initial package
