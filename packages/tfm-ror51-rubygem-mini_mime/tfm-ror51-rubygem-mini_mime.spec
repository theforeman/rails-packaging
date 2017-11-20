# Generated from mini_mime-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name mini_mime

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: A lightweight mime type lookup toy
Group:   Development/Languages
License: MIT
URL:     https://github.com/discourse/mini_mime
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
A lightweight mime type lookup toy.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bench
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/mini_mime.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Mon Nov 20 2017 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-1
- Initial package
