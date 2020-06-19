# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name optparse-applicative
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.15.1.0
Release:        1%{?dist}
Summary:        Utilities and combinators for parsing command line options

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-ansi-wl-pprint-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-compat-prof
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-bytestring-devel
%endif
# End cabal-rpm deps

%description
Utilities and combinators for parsing command line options.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library
documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%cabal_test


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.15.1.0-1
- update to 0.15.1.0

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 0.14.3.0-5
- refresh to cabal-rpm-2.0.3
- revised .cabal

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.14.3.0-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.14.3.0-1
- update to 0.14.3.0

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.14.2.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.14.2.0-1
- update to 0.14.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.14.0.0-1
- update to 0.14.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Jens Petersen <petersen@redhat.com> - 0.13.1.0-1
- update to 0.13.1.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 25 2016 Jens Petersen <petersen@redhat.com> - 0.12.1.0-1
- update to 0.12.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov  5 2014 Jens Petersen <petersen@redhat.com> - 0.11.0.1-3
- disable hlint Annotations on archs without ghci

* Tue Nov  4 2014 Ricky Elrod <relrod@redhat.com> - 0.11.0.1-2
- Add ExclusiveArch for GHCi dependency

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
