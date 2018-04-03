# Generated from actioncable-5.1.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name actioncable

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.6
Release: 1%{?dist}
Summary: WebSocket framework for Rails
Group:   Development/Languages
License: MIT
URL:     http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(nio4r)
Requires: %{?scl_prefix}rubygem(websocket-driver)
Requires: %{?scl_prefix}rubygem(actionpack) = %{version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.2
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Structure many real-time application concerns into channels over a single
WebSocket connection.


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
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 03 2018 Eric D. Helms <ericdhelms@gmail.com> 5.1.6-1
- Release tfm-ror51-rubygem-actioncable 5.1.6

* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-3
- rebuilt

* Wed Nov 22 2017 Eric D. Helms <ericdhelms@gmail.com> - 5.1.4-1
- Initial package
