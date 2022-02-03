%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	UML diagramming tool for KDE
Name:		umbrello
Version:	21.12.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source10:	umbrello.rpmlintrc
Patch0:		umbrello-20.03.80-llvm-10.patch
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
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
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
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KDevelop-PG-Qt)
BuildRequires:	cmake(LLVM)
BuildRequires:	cmake(Clang)
BuildRequires:	cmake(KDevPlatform)
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
# FIXME can be removed when LLVM cmake files stop referencing them
BuildRequires:	llvm-mlir-tools
BuildRequires:	spirv-llvm-translator
BuildRequires:	%{_lib}gpuruntime

%description
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -f %{name}.lang
%{_bindir}/umbrello5
%{_bindir}/po2xmi5
%{_bindir}/xmi2pot5
%{_datadir}/applications/org.kde.umbrello.desktop
%{_datadir}/metainfo/org.kde.umbrello.appdata.xml
%{_datadir}/umbrello5
%{_iconsdir}/hicolor/*/*/*.*[gz]
%doc %{_docdir}/qt5/*.qch

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -G Ninja -DBUILD_KF5:BOOL=ON

%build
%ninja_build -C build
# FIXME why doesn't ninja do this? It does respect the
# generated files in the install step...
cd build
doxygen Doxyfile.apidoc

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
