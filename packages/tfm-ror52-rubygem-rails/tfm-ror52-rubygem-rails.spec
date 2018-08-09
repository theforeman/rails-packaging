# Generated from rails-5.2.0.gem by gem2rpm -*- rpm-spec -*-
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails

Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 5.2.0
Release: 1%{?dist}
Summary: Full-stack web application framework
Group:   Development/Languages
License: MIT
URL:     http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(actionpack)
Requires: %{?scl_prefix}rubygem(actionview)
Requires: %{?scl_prefix}rubygem(activemodel) = %{version}
Requires: %{?scl_prefix}rubygem(activerecord) = %{version}
Requires: %{?scl_prefix}rubygem(actionmailer)
Requires: %{?scl_prefix}rubygem(activejob) = %{version}
Requires: %{?scl_prefix}rubygem(actioncable)
Requires: %{?scl_prefix}rubygem(activestorage) = %{version}
Requires: %{?scl_prefix}rubygem(railties)
Requires: %{?scl_prefix}rubygem(bundler)
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


%files
%dir %{gem_instdir}

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
