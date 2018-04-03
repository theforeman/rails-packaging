# Generated from actionview-5.1.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name actionview

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.6
Release: 1%{?dist}
Summary: Rendering framework putting the V in MVC (part of Rails)
Group:   Development/Languages
License: MIT
URL:     http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rails-dom-testing)
Requires: %{?scl_prefix}rubygem(rails-html-sanitizer)
Requires: %{?scl_prefix}rubygem(erubi)
Requires: %{?scl_prefix_ruby}rubygem(bundler) >= 1.3.0
Requires: %{?scl_prefix_ruby}rubygem(bundler) < 2.0
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildRequires: %{?scl_prefix}rubygem(activemodel) = %{version}
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Simple, battle-tested conventions and helpers for building web pages.


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
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Tue Apr 03 2018 Eric D. Helms <ericdhelms@gmail.com> 5.1.6-1
- Release tfm-ror51-rubygem-actionview 5.1.6

* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-3
- rebuilt

* Wed Nov 22 2017 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-1
- Initial package
