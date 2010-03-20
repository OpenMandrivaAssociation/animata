%define name	animata
%define version	 004
%define date	091218
%define release	%mkrel 0.%date.1
%define Summary	 Open source real-time animation software

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://animata.googlecode.com/files/%{name}_%{version}-%{date}.tar.gz
Patch0:		animata-004-mdv-fix-FL-include-path.patch
License:	GPLv3
Group:		Graphics
URL:		http://animata.kibu.hu/
BuildRequires:	scons
BuildRequires:	fltk-devel
BuildRequires:	mesaglu-devel
BuildRequires:	x11-server-xvfb
%description
Animata is an open source real-time animation software, designed to create
animations, interactive background projections for concerts, theatre and dance
performances.

%files  
%defattr(-,root,root)
%doc	README AUTHORS CHANGES COPYING examples 
%_bindir/%{name}
%_datadir/icons/animata_icon.png
%_datadir/applications/mandriva-%{name}.desktop

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p 0

%build
/usr/bin/xvfb-run -a %scons


%install
%__rm -rf %buildroot
%__mkdir -p %buildroot/%_bindir
%__mkdir -p %buildroot/%_datadir/icons/
%__cp build/%{name}	%buildroot/%_bindir
%__cp data/animata_icon.png	%buildroot/%_datadir/icons/

%__mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Animata
Comment=Open source real-time animation software
Exec=animata
Icon=animata_icon
StartupNotify=true
Type=Application
Categories=3DGraphics;Graphics;Viewer;
EOF

%clean
%__rm -rf %buildroot
