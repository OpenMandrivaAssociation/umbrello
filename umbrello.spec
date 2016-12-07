Summary:	UML diagramming tool for KDE
Name:		umbrello
Version:	16.08.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source10:	umbrello.rpmlintrc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

%description
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files
%{_bindir}/umbrello
%{_bindir}/po2xmi
%{_bindir}/xmi2pot
%{_datadir}/applications/org.kde.umbrello.desktop
%{_datadir}/kxmlgui5/umbrello
%{_datadir}/metainfo/org.kde.umbrello.appdata.xml
%{_datadir}/umbrello
%{_iconsdir}/hicolor/*/*/*.*[gz]
%doc %{_docdir}/*/*/umbrello

#----------------------------------------------------------------------------

%prep
%setup -q

%build
sed -i 's/BUILD_UNITTESTS 1/BUILD_UNITTESTS 0/' CMakeLists.txt
%cmake_kde5 -DBUILD_KF5=1 -DBUILD_UNITTESTS=0
%ninja

%install
%ninja_install -C build

