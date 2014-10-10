# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name optparse-applicative

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        0.11.0.1
Release:        1%{?dist}
Summary:        Utilities and combinators for parsing command line options

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-compat-devel
# End cabal-rpm deps

%description
Utilities and combinators for parsing command line options.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
# test-suite requires test-framework*


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc README.md


%changelog
* Fri Oct 10 2014 Ricky Elrod <relrod@redhat.com> - 0.11.0.1-1
- Latest upstream release.

* Tue Sep 23 2014 Ricky Elrod <relrod@redhat.com> - 0.10.0-1
- Latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Ricky Elrod <relrod@redhat.com> - 0.9.0-1
- Latest upstream release.

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.8.1-2
- F21 rebuild

* Mon May 12 2014 Ricky Elrod <rleord@redhat.com> - 0.8.1-1
- Latest upstream release.

* Mon May 5 2014 Jens Petersen <petersen@redhat.com> - 0.8.0.1-2
- add comment about testsuite requiring test-framework

* Thu Apr 10 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.8.0.1-1
- spec file generated by cabal-rpm-0.8.10
