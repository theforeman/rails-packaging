# Generated from sass-rails-5.0.7.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sass-rails

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.0.7
Release: 2%{?dist}
Summary: Sass adapter for the Rails asset pipeline
Group:   Development/Languages
License: MIT
URL:     https://github.com/rails/sass-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(railties)
Requires: %{?scl_prefix}rubygem(sass)
Requires: %{?scl_prefix}rubygem(sprockets-rails)
Requires: %{?scl_prefix}rubygem(sprockets)
Requires: %{?scl_prefix}rubygem(tilt)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Sass adapter for the Rails asset pipeline.


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
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.0.7-2
- rebuilt

* Wed Nov 29 2017 Eric D. Helms <ericdhelms@gmail.com> - 5.0.7-1
- Initial package
