#
# Conditional build:
%bcond_without	gimp	# without GIMP libraries (don't build as gimp plugin)
#
Summary:	An X Window System tool for creating morphed images
Summary(pl):	Narzêdzie do morphingu pod X Window System
Name:		xmorph
Version:	2001.07.27
%define	verfn	2001jul27
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.colorado-research.com/~gourlay/software/Graphics/Xmorph/pub/%{name}-%{verfn}.tar.gz
# Source0-md5:	a21e22aa7d9887cc0e85b97cdeceacbd
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-gimp1.3.patch
BuildRequires:	XFree86-devel
%{?with_gimp:BuildRequires:	gimp-devel >= 1:1.2}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gimp}
%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins
%endif

%description
Xmorph is a digital image warping (aka morphing) program. Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs: changing one image into another. Xmorph runs under the
X Window System.

Install the xmorph package if you need a program that will create
morphed images.

%description -l pl
xmorph jest programem do cyfrowego przekszta³cania obrazów
(morphingu).

%prep
%setup -q -n %{name}-%{verfn}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} depend
%{__make} xmorph xmorph.man \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{?with_gimp:`gimptool --cflags` -DGIMP -DNEED_GIMP=1}" \
	GIMPLIBS="%{?with_gimp:`gimptool --libs`}"

%{__make} clean
%{__make} morph \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xmorph $RPM_BUILD_ROOT%{_bindir}
install xmorph.man $RPM_BUILD_ROOT%{_mandir}/man1/xmorph.1

%if %{with gimp}
install -d $RPM_BUILD_ROOT%{gimpplugindir}
ln -sf %{_bindir}/xmorph $RPM_BUILD_ROOT%{gimpplugindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%attr(755,root,root) %{_bindir}/xmorph
%{_mandir}/man1/xmorph.1*
%if %{with gimp}
%attr(755,root,root) %{gimpplugindir}/xmorph
%endif
