# Generated from jquery-turbolinks-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name jquery-turbolinks

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: jQuery plugin for drop-in fix binded events problem caused by Turbolinks
Group:   Development/Languages
License: MIT
URL:     https://github.com/kossnocorp/jquery.turbolinks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(railties)
Requires: %{?scl_prefix}rubygem(turbolinks)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
jQuery plugin for drop-in fix binded events problem caused by Turbolinks.


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
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/NOTES.md
%exclude %{gem_instdir}/jquery-turbolinks.gemspec
%{gem_libdir}
%{gem_instdir}/package.json
%{gem_instdir}/src
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Thu Dec 07 2017 Ondrej Prazak - 2.1.0-1
- Initial package
