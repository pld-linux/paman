Summary:	PulseAudio Manager
Summary(pl.UTF-8):	PulseAudio Manager - zarządca serwera dźwięku PulseAudio
Name:		paman
Version:	0.9.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/paman/%{name}-%{version}.tar.gz
# Source0-md5:	4a77b129b0de8d261f2794ce3db518cc
Patch0:		%{name}-desktop.patch
URL:		http://0pointer.de/lennart/projects/paman/
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.7
Requires:	pulseaudio-libs >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Manager (paman) is a simple GTK+ frontend for the
PulseAudio sound server.

%description -l pl.UTF-8
PulseAudio Manager (paman) to prosty frontend GTK+ dla serwera dźwięku
PulseAudio.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/paman
%{_datadir}/paman
%{_desktopdir}/paman.desktop
