#
# Conditional build:
# _without_gimp		without GIMP libraries (don't build as gimp plugin)
#
Summary:	An X Window System tool for creating morphed images
Summary(pl):	Narzêdzie do morphingu pod X Window System
Name:		xmorph
Version:	2001.07.27
%define	verfn	2001jul27
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.colorado-research.com/~gourlay/software/Graphics/Xmorph/pub/%{name}-%{verfn}.tar.gz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-glibc.patch
BuildRequires:	XFree86-devel
%{!?_without_gimp:BuildRequires:	gimp-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xmorph is a digital image warping (aka morphing) program. Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs: changing one image into another. Xmorph runs under the
X Window System.

Install the xmorph package if you need a program that will create
morphed images.

%description -l pl
xmorph jest programem do cyfrowego przekszta³cania obrazów (morphingu).

%prep
%setup -q -n %{name}-%{verfn}
%patch0 -p1
%patch1 -p1

%build
%{__make} depend
%{__make} xmorph xmorph.man \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{!?_without_gimp:-DGIMP -DNEED_GIMP=1}" \
	%{?_without_gimp:GIMPLIBS=""}

%{__make} clean
%{__make} morph CC="%{__cc}" OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xmorph $RPM_BUILD_ROOT%{_bindir}
install xmorph.man $RPM_BUILD_ROOT%{_mandir}/man1/xmorph.1x

gzip -9nf README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz HISTORY.gz
%attr(755,root,root) %{_bindir}/xmorph
%{_mandir}/man1/xmorph.1x*
