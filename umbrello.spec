Summary:	UML diagramming tool for KDE
Name:		umbrello
Version:	15.12.0
Release:	2
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
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)

%description
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files
%{_bindir}/umbrello                                                                                    
%{_bindir}/po2xmi                                                                                      
%{_bindir}/xmi2pot                                                                                     
%{_datadir}/applications/kde4/umbrello.desktop                                                         
%{_datadir}/apps/umbrello                                                                              
%{_iconsdir}/*/*/*/umbrello*                                                                           
%{_iconsdir}/*/*/mimetypes/application-x-uml.png                                                       
%doc %{_docdir}/*/*/umbrello 

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

