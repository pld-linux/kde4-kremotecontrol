#
%define		_state		stable
%define		orgname		kremotecontrol
%define		qtver		4.8.0

Summary:	K Desktop Environment - Infrared Remote Control
Name:		kde4-kremotecontrol
Version:	4.13.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6a84af969b57245b75e59a1d81df0df0
URL:		http://www.kde.org/
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdeutils-irkick
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRemoteControl is a KDE frontend for your remote controls. It allows
to configure actions for button presses on remotes. All types of
remotes supported by Solid are also supported by KRemoteControl.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krcdnotifieritem
%attr(755,root,root) %{_libdir}/kde4/kcm_remotecontrol.so
%attr(755,root,root) %{_libdir}/kde4/kded_kremotecontroldaemon.so
%attr(755,root,root) %{_libdir}/kde4/kremotecontrol_lirc.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kremoteconrol.so
%attr(755,root,root) %{_libdir}/liblibkremotecontrol.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblibkremotecontrol.so.?
%{_datadir}/apps/kremotecontrol
%{_datadir}/apps/kremotecontroldaemon
%{_datadir}/kde4/services/kcm_remotecontrol.desktop
%{_datadir}/kde4/services/kded/kremotecontroldaemon.desktop
%{_datadir}/kde4/services/kremotecontrolbackends
%{_datadir}/kde4/services/plasma-engine-kremotecontrol.desktop
%{_datadir}/kde4/servicetypes/kremotecontrolmanager.desktop
%{_desktopdir}/kde4/krcdnotifieritem.desktop
%{_iconsdir}/hicolor/scalable/actions/krcd_flash.svgz
%{_iconsdir}/hicolor/scalable/actions/krcd_off.svgz
%{_iconsdir}/hicolor/scalable/apps/krcd.svgz
%{_iconsdir}/hicolor/scalable/devices/infrared-remote.svgz
%{_iconsdir}/hicolor/*x*/actions/krcd_flash.png
%{_iconsdir}/hicolor/*x*/actions/krcd_off.png
%{_iconsdir}/hicolor/*x*/apps/krcd.png
%{_iconsdir}/hicolor/*x*/devices/infrared-remote.png
%{_kdedocdir}/en/kcontrol
