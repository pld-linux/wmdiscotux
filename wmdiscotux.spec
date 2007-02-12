Summary:	An XMMS plugin for WindowMaker
Summary(pl.UTF-8):   Wtyczka dla XMMS-a dla WindowMakera
Name:		wmdiscotux
Version:	1.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://fragment.stc.cx/files/%{name}-%{version}.tar.gz
# Source0-md5:	8043c73f29f1305446594a0353ad7839
Patch0:		%{name}-gcc33.patch
URL:		http://wmdiscotux.stc.cx/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmDiscoTux is a simple XMMS visualization plugin that sits nicely in
windowmaker'a dock. Tux moves his bodyparts with the music.

%description -l pl.UTF-8
wmDiscoTux jest prostą wtyczką graficzną dla XMMS-a, która ładnie
komponuje się z WindowMakerem. Tux porusza ciałem w rytm muzyki.

%prep
%setup -q
%patch0 -p1

%build
rm -f *.so
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fPIC `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{xmms_visualization_plugindir}}

install *.so $RPM_BUILD_ROOT%{xmms_visualization_plugindir}
install tux-icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_visualization_plugindir}/libwmdiscotux.so
%{_pixmapsdir}/tux-icon.xpm
