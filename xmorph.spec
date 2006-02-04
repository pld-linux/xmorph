#
# Conditional build:
%bcond_with	gimp	# build as gimp plugin (broken)
#
Summary:	An X Window System tool for creating morphed images
Summary(pl):	Narzêdzie do morphingu pod X Window System
Name:		xmorph
Version:	20060130
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xmorph/%{name}_%{version}.tar.gz
# Source0-md5:	09c386be10b4318070d58bdfe494830e
Patch0:		%{name}-gimp.patch
Patch1:		%{name}-libname.patch
Patch2:		%{name}-info.patch
URL:		http://xmorph.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-devel >= 3.0
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.2}
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRequires:	waili-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins
%endif

%description
Xmorph is a digital image warping (aka morphing) program. Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs: changing one image into another. Xmorph runs under the
X Window System.

%description -l pl
xmorph jest programem do cyfrowego przekszta³cania obrazów
(morphingu). Pakiet dostarcza potrzebne narzêdzia oraz opis jak
tworzyæ przekszta³cenia. Dzia³a w ¶rodowisku X Window System.

%package gtk
Summary:	gtkmorph - GTK+ version of xmorph
Summary(pl):	gtkmorph - wersja xmorpha oparta na GTK+
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description gtk
gtkmorph - GTK+ version of xmorph.

%description gtk -l pl
gtkmorph - wersja xmorpha oparta na GTK+.

%package devel
Summary:	Header files for xmorph library
Summary(pl):	Pliki nag³ówkowe biblioteki xmorph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for xmorph library.

%description devel -l pl
Pliki nag³ówkowe biblioteki xmorph.

%package static
Summary:	Static xmorph library
Summary(pl):	Statyczna biblioteka xmorph
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xmorph library.

%description static -l pl
Statyczna biblioteka xmorph.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo 'AM_DEFUN([AM_PATH_GTK],[$3])' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gtk=2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so xmorph.1' > $RPM_BUILD_ROOT%{_mandir}/man1/morph.1

# gtkmorph locales despite the xmorph name
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY README TODO libmorph/README.libmorph debian/changelog
%attr(755,root,root) %{_bindir}/morph
%attr(755,root,root) %{_bindir}/xmorph
%attr(755,root,root) %{_libdir}/libxmorph.so.*.*.*
%{_datadir}/xmorph
%{_mandir}/man1/morph.1*
%{_mandir}/man1/xmorph.1*
%{_infodir}/xmorph.info*
%if %{with gimp}
%attr(755,root,root) %{gimpplugindir}/xmorph
%endif

%files gtk -f %{name}.lang
%defattr(644,root,root,755)
%doc gtkmorph/README
%attr(755,root,root) %{_bindir}/gtkmorph
%{_mandir}/man1/gtkmorph.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmorph.so
%{_libdir}/libxmorph.la
%{_includedir}/xmorph

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmorph.a
