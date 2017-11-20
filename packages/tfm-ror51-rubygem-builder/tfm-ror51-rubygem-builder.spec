# Generated from builder-3.2.3.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name builder

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.3
Release: 1%{?dist}
Summary: Builders for MarkUp
Group:   Development/Languages
License: MIT
URL:     http://onestepback.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Builder provides a number of builder objects that make creating structured
data
simple to do.  Currently the following builder objects are supported:
* XML Markup
* XML Events.


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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/CHANGES
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Mon Nov 20 2017 Eric D. Helms <ericdhelms@gmail.com> - 3.2.3-1
- Initial package
