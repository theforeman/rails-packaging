# Generated from thread_safe-0.3.6.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name thread_safe

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.6
Release: 1%{?dist}
Summary: Thread-safe collections and utilities for Ruby
Group:   Development/Languages
License: Apache-2.0
URL:     https://github.com/ruby-concurrency/thread_safe
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
A collection of data structures and utilities to make thread-safe programming
in Ruby easier.


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
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/ext
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_instdir}/thread_safe.gemspec
%{gem_instdir}/yard-template
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
* Mon Nov 20 2017 Eric D. Helms <ericdhelms@gmail.com> - 0.3.6-1
- Initial package
