%define name            ifd-egate
%define version         0.05
%define release         %mkrel 2

Name:	 %{name}
Version: %{version}
Release: %{release}
Summary: PC/SC drivers for USB egate smart cart readers
License: GPL
Group:   System/Libraries
Source0: %{name}-%{version}.tar.bz2
Patch0:	 %{name}-Makefile.patch.bz2
Patch1:	 %{name}-egatec.patch.bz2
Patch2:	 %{name}-responsecode.patch
URL:     http://secure.netroedge.com/~phil/egate/
BuildRequires: libpcsclite1
Requires: pcsc-lite

%description
This library provides a PC/SC IFD handler implementation 
for the USB egate smart card readers.  This package is 
needed to communicate with the egate smartcard readers 
through the PC/SC Lite resource manager (pcscd).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n  %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%make

%install
mkdir -p $RPM_BUILD_ROOT%_defaultdocdir/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux
install -m 644 Info.plist $RPM_BUILD_ROOT%_libdir/pcsc/drivers/ifd-egate.bundle/Contents
install -m 755 libifd_egate.so  $RPM_BUILD_ROOT%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux
install -m 644 ChangeLog COPYRIGHT COPYING.LIB LICENSE PROTOCOL README $RPM_BUILD_ROOT%_defaultdocdir/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_libdir/pcsc/drivers/ifd-egate.bundle/Contents
%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux
%_defaultdocdir/%{name}-%{version}
