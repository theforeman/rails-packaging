%global scl_name_prefix tfm-
%global scl_name_base ror
%global scl_name_version 52
%global scl_vendor theforeman
%global scl %{scl_name_prefix}%{scl_name_base}%{scl_name_version}
%global _scl_prefix /opt/%{scl_vendor}

# Fallback to rh-ruby24. rh-ruby24-scldevel is probably not available in
# the buildroot.
%{!?scl_ruby:%global scl_ruby rh-ruby25}
%{!?scl_prefix_ruby:%global scl_prefix_ruby %{scl_ruby}-}

# Do not produce empty debuginfo package.
%global debug_package %{nil}

# Support SCL over NFS.
# nfsmountable macro must be defined before defining the scl_package macro
%global nfsmountable 1

%scl_package %scl

Summary: Package that installs %scl
Name:    %scl_name
Version: 1.0
Release: 3%{?dist}
License: GPLv2+
Source0: README
Source1: LICENSE
Source2: macros.tfm-ror52

BuildRequires: help2man
BuildRequires: scl-utils-build
BuildRequires: %{scl_prefix_ruby}scldevel
BuildRequires: %{scl_prefix_ruby}rubygems-devel

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils
# enable scriptlet depends on ruby executable.
Requires: %{scl_prefix_ruby}ruby

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build
Requires: %{scl_runtime}
Requires: %{scl_prefix_ruby}scldevel

%description build
Package shipping essential configuration macros to build %scl Software Collection.

%package scldevel
Summary: Package shipping development files for %scl
Provides: scldevel(%{scl_name_base})

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.

%prep
%setup -T -c

# Expand macros used in README file.
cat > README << EOF
%{expand:%(cat %{SOURCE0})}
EOF

cp %{SOURCE1} .

%build
# Generate a helper script that will be used by help2man.
cat > h2m_help << 'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} %{version} Software Collection" || cat README
EOF
chmod a+x h2m_help

# Generate the man page from include.h2m and ./h2m_help --help output.
help2man -N --section 7 ./h2m_help -o %{scl_name}.7

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH="%{_bindir}:%{_sbindir}\${PATH:+:\${PATH}}"
export LD_LIBRARY_PATH="%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}"
export MANPATH="%{_mandir}:\${MANPATH:-}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}"
export GEM_PATH="\${GEM_PATH:=%{gem_dir}:\`scl enable %{scl_ruby} -- ruby -e "print Gem.path.join(':')"\`}"
export GEM_HOME="%{gem_dir}"

. scl_source enable %{scl_ruby}
EOF

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF

# additional rpm macros for builds in the collection to set the vendor correctly
cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name}-config << EOF
%%scl_vendor %{scl_vendor}
%%_scl_prefix %{_scl_prefix}
EOF

# Install generated man page.
mkdir -p %{buildroot}%{_mandir}/man7/
install -p -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/

scl enable %{scl_ruby} - << \EOF
set -e

GEM_PATH=%{gem_dir}:`ruby -e "print Gem.path.join(':')"` \
X_SCLS=%{scl} \
ruby -rfileutils > rubygems_filesystem.list << \EOR
  # Create RubyGems filesystem.
  Gem.ensure_gem_subdirectories '%{buildroot}%{gem_dir}'
  FileUtils.mkdir_p File.join '%{buildroot}', Gem.default_ext_dir_for('%{gem_dir}')

  # Output the relevant directories.
  Gem.default_dirs['%{scl}_system'.to_sym].values
EOR
EOF

# Create directory for license files (rhbz#1431083).
%{?_licensedir:mkdir -p %{buildroot}%{_licensedir}}

install -m 644 %{SOURCE2} %{buildroot}%{_root_sysconfdir}/rpm/macros.tfm-ror52

%files

%files runtime -f rubygems_filesystem.list
%doc README LICENSE
%scl_files
%{?_licensedir:%dir %{_licensedir}}
# Own the manual directories (rhbz#1080036, rhbz#1072319).
%dir %{_mandir}/man1
%dir %{_mandir}/man5
%dir %{_mandir}/man7
%{_mandir}/man7/%{scl_name}.*

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config
%{_root_sysconfdir}/rpm/macros.tfm-ror52

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0-3
- Drop install-dir and add GEM_HOME

* Wed Aug 08 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0-2
- Add gem_intall macro workaround

* Tue Jul 10 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0-1
- rebuilt

