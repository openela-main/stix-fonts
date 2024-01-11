# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/stipub/stixfonts/
Version: 2.0.2
%forgemeta

Release: 11%{?dist}
URL:     http://www.stixfonts.org/

%global foundry           STIX
%global fontlicense       OFL
%global fontlicenses      docs/STIX_%{version}_license.pdf
%global fontdocs          *.md docs/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        STIX
%global fontsummary       STIX, a scientific and engineering font family
%global fontpkgheader     %{expand:
Obsoletes: stix-math-fonts < %{version}-%{release}
}
%global fonts             OTF/STIX2Text*otf OTF/STIX2Math*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The mission of the Scientific and Technical Information Exchange (STIX) font
creation project is the preparation of a comprehensive set of fonts that serve
the scientific and engineering community in the process from manuscript
creation through final publication, both in electronic and print formats.
}


Source0:  %{forgesource0}
Source10: 65-%{fontpkgname0}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%license docs/STIX_%{version}_license.pdf
%doc docs/charts/*pdf

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com>
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com>
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Parag Nemade <pnemade AT redhat DOT com>
- 2.0.2-8
- Fix this spec file to build for F33+

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.0.2-1
✅ Convert to fonts-rpm-macros use

* Thu Nov 1 2007 Nicolas Mailhot <nim@fedoraproject.org>
- 0.9-4
✅ Initial packaging
