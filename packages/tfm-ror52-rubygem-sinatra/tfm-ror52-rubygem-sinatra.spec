# Generated from sinatra-2.0.3.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name sinatra

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.3
Release: 1%{?dist}
Summary: Classy web-development dressed in a DSL
Group:   Development/Languages
License: MIT
URL:     http://www.sinatrarb.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rack)
Requires: %{?scl_prefix}rubygem(tilt)
Requires: %{?scl_prefix}rubygem(rack-protection)
Requires: %{?scl_prefix}rubygem(mustermann)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.2.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
mkdir -p ./opt/rh/%{scl_ruby}/root/usr/bin
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MAINTENANCE.md
%{gem_instdir}/SECURITY.md
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_instdir}/sinatra.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.de.md
%doc %{gem_instdir}/README.es.md
%doc %{gem_instdir}/README.fr.md
%doc %{gem_instdir}/README.hu.md
%doc %{gem_instdir}/README.ja.md
%doc %{gem_instdir}/README.ko.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README.pt-br.md
%doc %{gem_instdir}/README.pt-pt.md
%doc %{gem_instdir}/README.ru.md
%doc %{gem_instdir}/README.zh.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples

%changelog
* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-1
- Initial package
