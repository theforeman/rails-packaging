# Generated from rails-5.1.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.6
Release: 1%{?dist}
Summary: Full-stack web application framework
Group:   Development/Languages
License: MIT
URL:     http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(actioncable) = %{version}
Requires: %{?scl_prefix}rubygem(actionmailer) = %{version}
Requires: %{?scl_prefix}rubygem(actionpack) = %{version}
Requires: %{?scl_prefix}rubygem(actionview) = %{version}
Requires: %{?scl_prefix}rubygem(activejob) = %{version}
Requires: %{?scl_prefix}rubygem(activemodel) = %{version}
Requires: %{?scl_prefix}rubygem(activerecord) = %{version}
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix_ruby}rubygem(bundler) >= 1.3.0
Requires: %{?scl_prefix_ruby}rubygem(bundler) < 2.0
Requires: %{?scl_prefix}rubygem(railties) = %{version}
Requires: %{?scl_prefix}rubygem(sprockets-rails)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 1.8.11
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


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

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 03 2018 Eric D. Helms <ericdhelms@gmail.com> 5.1.6-1
- Release tfm-ror51-rubygem-rails 5.1.6

* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-4
- rebuilt

* Wed Nov 22 2017 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-1
- Initial package
