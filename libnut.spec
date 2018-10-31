%define	gitrev	20160626
%define	major	0
%define	libname	%mklibname nut %{major}
%define	devname	%mklibname -d nut

Summary:	NUT Multimedia Container Library
Name:		libnut
Version:	0.0.%{gitrev}
Release:	2
License:	MIT
Group:		System/Libraries
Url:		http://wiki.multimedia.cx/index.php?title=NUT
# git clone git://git.ffmpeg.org/nut ; cd nut/src ; mv trunk libnut ; tar cf libnut-$(date +%Y%m%d).tar libnut ; xz -9ef *.tar ; mv libnut trunk
Source0:	%{name}-%{gitrev}.tar.xz
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
%setup -qn %{name}
%apply_patches

%build
%setup_compile_flags
%make prefix=%{_prefix} libdir=%{_libdir}

%install
%makeinstall

rm -f %{buildroot}%{_libdir}/*.a

%files utils
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libnut.so.%{major}*

%files -n %{devname}
%doc COPYING README
%{_includedir}/libnut.h
%{_libdir}/libnut.so

