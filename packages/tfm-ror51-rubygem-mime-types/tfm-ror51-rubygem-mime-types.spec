# Generated from mime-types-3.1.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name mime-types

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 3.1
Release: 1%{?dist}
Summary: The mime-types library provides a library and registry for information about MIME content type definitions
Group:   Development/Languages
License: MIT
URL:     https://github.com/mime-types/ruby-mime-types/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(mime-types-data)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
The mime-types library provides a library and registry for information about
MIME content type definitions. It can be used to determine defined filename
extensions for MIME types, or to use filename extensions to look up the likely
MIME type definitions.
Version 3.0 is a major release that requires Ruby 2.0 compatibility and
removes
deprecated functions. The columnar registry format introduced in 2.6 has been
made the primary format; the registry data has been extracted from this
library
and put into {mime-types-data}[https://github.com/mime-types/mime-types-data].
Additionally, mime-types is now licensed exclusively under the MIT licence and
there is a code of conduct in effect. There are a number of other smaller
changes described in the History file.


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
%license %{gem_instdir}/Licence.rdoc
%{gem_instdir}/Manifest.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Code-of-Conduct.rdoc
%doc %{gem_instdir}/Contributing.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Dec 21 2017 Eric D. Helms <ericdhelms@gmail.com> - 3.1-1
- Initial package
