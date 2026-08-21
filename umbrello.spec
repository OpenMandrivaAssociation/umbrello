%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Summary:	UML diagramming tool for KDE
Name:		umbrello
Version:	26.08.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source10:	umbrello.rpmlintrc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildSystem:	cmake
BuildOption:	-DBUILD_WITH_QT6:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBUILD_APIDOC:BOOL=OFF
BuildOption:	-DBUILD_QCH:BOOL=OFF

%description
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -f %{name}.lang
%{_bindir}/umbrello6
%{_bindir}/po2xmi6
%{_bindir}/xmi2pot6
%{_datadir}/applications/org.kde.umbrello.desktop
%{_datadir}/metainfo/org.kde.umbrello.appdata.xml
%{_datadir}/umbrello6
%{_iconsdir}/hicolor/*/*/*

#----------------------------------------------------------------------------

%install -a
%find_lang %{name} --all-name --with-html
