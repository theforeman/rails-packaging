# Generated from nio4r-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name nio4r

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: New IO for Ruby
Group:   Development/Languages
License: MIT
URL:     https://github.com/socketry/nio4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.2.2
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.


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
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%{gem_instdir}/.ruby-version
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/CHANGES.md
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%{gem_instdir}/logo.png
%exclude %{gem_instdir}/nio4r.gemspec
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Tue Nov 21 2017 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-1
- Initial package
