Name:		ifd-egate
Version:	0.05
Release:	4
Summary:	PC/SC drivers for USB egate smart cart readers
License:	BSD or LGPLv2+
Group:		System/Libraries
Source0:	http://secure.netroedge.com/~phil/egate/%{name}-%{version}.tar.bz2
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-egatec.patch
Patch2:		%{name}-responsecode.patch
URL:		http://secure.netroedge.com/~phil/egate/
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig(libusb)
Requires:	pcsc-lite

%description
This library provides a PC/SC IFD handler implementation for the USB
egate smart card readers.  This package is needed to communicate with
the egate smartcard readers through the PC/SC Lite resource manager
(pcscd).

%prep
rm -rf %{buildroot}
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
%make

%install
mkdir -p %{buildroot}%_defaultdocdir/%{name}-%{version}
mkdir -p %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux
install -m 644 Info.plist %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents
install -m 755 libifd_egate.so  %{buildroot}%_libdir/pcsc/drivers/ifd-egate.bundle/Contents/Linux

%files
%defattr(-,root,root)
%doc ChangeLog COPYRIGHT LICENSE PROTOCOL README
%{_libdir}/pcsc/drivers/ifd-egate.bundle/Contents




%changelog
* Sun Aug 24 2008 Adam Williamson <awilliamson@mandriva.com> 0.05-3mdv2009.0
+ Revision: 275524
- don't list a directory twice in file list
- don't package COPYING.LIB (LGPL text)
- don't manually install doc files, use %%doc in file list
- s,$RPM_BUILD_ROOT,%%{buildroot}
- rewrap description
- drop explicit libpcsclite1 buildrequire, the devel package requires it
- correct 'usb-devel' buildrequire
- bunzip2 the patches
- correct license with new policy (not GPL, dual BSD/LGPL)
- drop unnecessary %%defines

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - BR usb-devel
    - BR pcsc-lite-devel
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Anne Nicolas <anne.nicolas@mandriva.com>
    - Add patch for 2008 rebuild (erwan help)
    - Import ifd-egate



* Wed Apr 06 2006 Anne Nicolas <anne.nicolas@mandriva.com> 0.05-1mdk
- initial release
