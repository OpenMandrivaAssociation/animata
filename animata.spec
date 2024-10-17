%define date	091218

Summary:	Open source real-time animation software
Name:		animata
Version:	004
Release:	0.%{date}.6
License:	GPLv3
Group:		Graphics
URL:		https://animata.kibu.hu/
Source0:	http://animata.googlecode.com/files/%{name}_%{version}-%{date}.tar.gz
Patch0:		animata-004-mdv-fix-FL-include-path.patch
Patch1:		animata-fltk-1.3.patch
Patch2:		animata-004-gcc4.7.patch
BuildRequires:	scons
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	x11-server-xvfb

%description
Animata is an open source real-time animation software, designed to create
animations, interactive background projections for concerts, theatre and dance
performances.

%files
%doc README AUTHORS CHANGES COPYING examples
%{_bindir}/%{name}
%{_datadir}/icons/animata_icon.png
%{_datadir}/applications/mandriva-%{name}.desktop

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p1
sed -i -e "s/^LINKFLAGS =.*/LINKFLAGS = '%{ldflags}'/" src/SConscript

%build
%setup_compile_flags
/usr/bin/xvfb-run -a %scons

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/
cp build/%{name}	%{buildroot}%{_bindir}
cp data/animata_icon.png	%{buildroot}%{_datadir}/icons/

mkdir -p %{buildroot}%{_datadir}/applications
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

