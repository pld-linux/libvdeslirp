#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	libslirp for Linux made easy
Summary(pl.UTF-8):	Łatwiejsze obudowanie libslirp dla Linuksa
Name:		libvdeslirp
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/virtualsquare/libvdeslirp/releases
Source0:	https://github.com/virtualsquare/libvdeslirp/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7b9bcdb74e4872e8f35dd49a6419a2c8
URL:		https://github.com/virtualsquare/libvdeslirp
BuildRequires:	cmake >= 3.13
BuildRequires:	libslirp-devel >= 4
BuildRequires:	vde2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Originally designed to provide PPP/SLIP over terminal lines, slirp is
a general purpose TCP/IP emulator widely used by virtual machine
hypervisors to provide virtual networking services.

Qemu, VirtualBox, user-mode Linux include slirp to provide the guest
OS with a virtual network while requiring neither configuration nor
privileged services on the host.

This project wraps the slirp code in a library featuring a clean and
simple interface.

%description -l pl.UTF-8
slirp, pierwotnie zaprojektowany na potrzeby protokołów PPP/SLIP po
liniach terminalowych, jest emulatorem TCP/IP ogólnego przeznaczenia,
używanym przede wszystkim przez hipernadzorców maszyn wirtualnych w
celu zapewnienia wirtualnych usług sieciowych.

Qemu, VirtualBox czy Linux przestrzeni użytkownika (UM) zawierają
slirp, aby udostępnić systemom gości sieć wirtualną bez wymagania
konfiguracji czy uprzywilejowanych usług w systemie gospodarza.

Ten projekt obudowuje kod slirp w bibliotekę o czystym i prostym
interfejsie.

%package devel
Summary:	Header files for libvdeslirp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvdeslirp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libslirp-devel >= 4

%description devel
Header files for libvdeslirp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvdeslirp.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_BINDIR=bin \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libvdeslirp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdeslirp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvdeslirp.so
%{_includedir}/slirp/libvdeslirp.h
%{_pkgconfigdir}/vdeslirp.pc
%{_mandir}/man3/libvdeslirp*.3*
%{_mandir}/man3/vdeslirp_*.3*
