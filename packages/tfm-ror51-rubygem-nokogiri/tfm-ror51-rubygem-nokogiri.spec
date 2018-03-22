# Generated from nokogiri-1.8.1.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name nokogiri

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.1
Release: 2%{?dist}
Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Group:   Development/Languages
License: MIT
URL:     http://nokogiri.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.1.0
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
%setup -n %{pkg_name}-%{version} -q -T -c

%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

cd %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

sed -i -e '\@mini_portile@d' %{gem_name}.gemspec

%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

mv *.gem ../
cd ../

%build
mkdir -p .%{gem_dir}

export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
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
%exclude %{gem_instdir}/ROADMAP.md
%exclude %{gem_instdir}/STANDARD_RESPONSES.md
%exclude %{gem_instdir}/Y_U_NO_GEMSPEC.md
%exclude %{gem_instdir}/appveyor.yml
%{gem_instdir}/bin
%exclude %{gem_instdir}/build_all
%exclude %{gem_instdir}/dependencies.yml
%{gem_libdir}
%{gem_instdir}/patches
%{gem_instdir}/ports
%{gem_instdir}/suppressions
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/CONTRIBUTING.md
%exclude %{gem_instdir}/C_CODING_STYLE.rdoc

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile-libxml-ruby
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.1-2
- rebuilt

* Tue Nov 21 2017 Eric D. Helms <ericdhelms@gmail.com> - 1.8.1-1
- Initial package
