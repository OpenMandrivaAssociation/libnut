%define	major	0
%define	libname	%mklibname nut %{major}
%define	devname	%mklibname -d nut

Name:		libnut
%define	svnrev	675
Version:	0.0.%{svnrev}
Release:	1
Url:		http://wiki.multimedia.cx/index.php?title=NUT
License:	MIT
Group:		System/Libraries
Summary:	NUT Multimedia Container Library
# svn checkout svn://svn.mplayerhq.hu/nut/src/trunk libnut ; tar -Jcf libnut-r$(LC_ALL=C svn info libnut | sed -n 's/Revision: //p').tar.xz libnut
Source0:	%{name}-r%{svnrev}.tar.xz
Patch0:		libnut-libdir.patch
Patch1:		libnut-shared.patch
Patch2:		libnut-r675-ldflags.patch

%description
Library for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%package -n	%{libname}
Group:		System/Libraries
Summary:	NUT Multimedia Container Library

%description -n	%{libname}
Library for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%package -n	%{devname}
Group:		Development/C
Summary:	Development files for NUT Multimedia Container Library
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package contains development files for the NUT Multimedia Container
Library.

%package	utils
Group:		Video
Summary:	NUT Multimedia Container Utilites

%description	utils
Utilities for manipulation with NUT multimedia streams.

Unlike many popular containers, a NUT file can largely be viewed as a
byte stream, opposed to having a global block structure. NUT files
consist of a sequence of packets, which can contain global headers,
file metadata, stream headers for the individual media streams,
optional index data to accelerate seeking, and, of course, the actual
encoded media frames.

%prep
%setup -q -n %{name}
%patch0 -p0 -b .libdir~
%patch1 -p1 -b .shared~
%patch2 -p1 -b .ldflags~

%build
%setup_compile_flags
%make prefix=%{_prefix} libdir=%{_libdir}

%install
%makeinstall

%files utils
%{_bindir}/*

%files -n %{libname}
%doc COPYING README
%{_libdir}/libnut.so.%{major}*

%files -n %{devname}
%{_includedir}/libnut.h
%{_libdir}/libnut.so
%{_libdir}/libnut.a



%changelog
* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.0.675-1
+ Revision: 733109
- imported package libnut


* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.0.675-1
- initial Mandriva package adapted from SuSE

* Mon Jan 26 2009 crrodriguez@suse.de
- fix -devel package requires
* Wed Oct 22 2008 mrueckert@suse.de
- fix debug_packages_requires define
* Tue Aug 19 2008 sbrabec@suse.cz
- Updated to the latest SVN snapshot 659:
  * fixed libnut muxer creating of header_count_minus1 and
    main_flags
* Fri Aug  1 2008 ro@suse.de
- fix requires for debuginfo package
* Mon Apr 28 2008 sbrabec@suse.cz
- Updated to the latest SVN snapshot 658:
  * Documentation fixes.
  * Code cleanup.
  * Debugging messages cleanup.
- Enabled shared library support.
* Tue Jan 15 2008 sbrabec@suse.cz
- Minor spec file cleanup.
- Updated to the latest SVN snapshot 514 (no change).
- Install all tools.
* Wed Jul 25 2007 sbrabec@suse.cz
- Updated to the latest SVN snapshot 505:
  * Added nutparse.
  * Minor fixes.
* Wed Mar 21 2007 sbrabec@suse.cz
- New SuSE package, SVN snapshot 282.
