Summary:	libslirp for Linux made easy
Summary(pl.UTF-8):	Łatwiejsze obudowanie libslirp dla Linuksa
Name:		libvdeslirp
Version:	0.1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/virtualsquare/libvdeslirp/tags
Source0:	https://github.com/virtualsquare/libvdeslirp/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8504bcaa5d27046e784384254d38619d
URL:		https://github.com/virtualsquare/libvdeslirp
BuildRequires:	cmake >= 3.25
BuildRequires:	libslirp-devel >= 4.9
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
Requires:	glib2-devel >= 2.0
Requires:	libslirp-devel >= 4

%description devel
Header files for libvdeslirp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvdeslirp.

%prep
%setup -q

%build
%cmake -B build \
	-DCMAKE_INSTALL_BINDIR=bin \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make} -C build

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
%{_libdir}/libvdeslirp.so.*.*.*
%ghost %{_libdir}/libvdeslirp.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libvdeslirp.so
%{_includedir}/slirp/libvdeslirp.h
%{_pkgconfigdir}/vdeslirp.pc
%{_mandir}/man3/libvdeslirp*.3*
%{_mandir}/man3/vdeslirp_*.3*
