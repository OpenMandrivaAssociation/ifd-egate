Name:		ifd-egate
Version:	0.05
Release:	%{mkrel 3}
Summary:	PC/SC drivers for USB egate smart cart readers
License:	BSD or LGPLv2+
Group:		System/Libraries
Source0:	http://secure.netroedge.com/~phil/egate/%{name}-%{version}.tar.bz2
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-egatec.patch
Patch2:		%{name}-responsecode.patch
URL:		http://secure.netroedge.com/~phil/egate/
BuildRequires:	pcsc-lite-devel
BuildRequires:	libusb-devel
Requires:	pcsc-lite
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This library provides a PC/SC IFD handler implementation for the USB
egate smart card readers.  This package is needed to communicate with
the egate smartcard readers through the PC/SC Lite resource manager
(pcscd).

%prep
rm -rf %{buildroot}
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%make

%install
mkdir -p %{buildroot}%_defaultdocdir/%{name}-%{version}
mkdir -p %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux
install -m 644 Info.plist %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents
install -m 755 libifd_egate.so  %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYRIGHT LICENSE PROTOCOL README
%{_libdir}/pcsc/drivers/ifd-egate.bundle/Contents


