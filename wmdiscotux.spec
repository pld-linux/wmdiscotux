Summary:	An XMMS plugin for WindowMaker
Summary(pl):	Wtyczka graficzna dla WindowMakera
Name:		wmdiscotux
Version:	1.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://fragment.stc.cx/files/%{name}-%{version}.tar.gz
Icon:		tux-icon.xpm
URL:		http://wmdiscotux.stc.cx/
BuildRequires:	xmms-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --visualization-plugin-dir)

%description
wmDiscoTux is a simple xmms visualization plugin that sits nicely
in windowmaker'a dock. Tux moves his bodyparts with the music.

%description -l pl
wmDiscoTux jest prost� wtyczk� graficzn�, kt�ra �adnie komponuje
si� z WindowMakerem. Tux porusza cia�em w rytm muzyki.

%prep
%setup -q

%build
rm -f *.so
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fPIC `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_xmms_plugin_dir}}

install *.so $RPM_BUILD_ROOT%{_xmms_plugin_dir}
install tux-icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)                                                     
%doc README
%attr(755,root,root) %{_xmms_plugin_dir}/libwmdiscotux.so
%attr(644,root,root) %{_pixmapsdir}/tux-icon.xpm
