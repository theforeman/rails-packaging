# Generated from nokogiri-1.8.4.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name nokogiri

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.4
Release: 2%{?dist}
Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Group:   Development/Languages
License: MIT
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(mini_portile2)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.1.0
BuildRequires: %{?scl_prefix}rubygem-mini_portile2
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%{?scl:Requires: %{?scl_prefix}runtime}

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among
Nokogiri's many features is the ability to search documents via XPath
or CSS3 selectors.


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
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/nokogiri
%{gem_extdir_mri}
%{gem_instdir}/.autotest
%{gem_instdir}/.cross_rubies
%{gem_instdir}/.editorconfig
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE-DEPENDENCIES.md
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/Manifest.txt
%{gem_instdir}/ROADMAP.md
%{gem_instdir}/SECURITY.md
%{gem_instdir}/STANDARD_RESPONSES.md
%{gem_instdir}/Y_U_NO_GEMSPEC.md
%{gem_instdir}/appveyor.yml
%{gem_instdir}/bin
%{gem_instdir}/build_all
%{gem_instdir}/dependencies.yml
%{gem_libdir}
%{gem_instdir}/patches
%{gem_instdir}/suppressions
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/C_CODING_STYLE.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile-libxml-ruby
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-2
- Add missing gem_docdir

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-1
- Initial package
