Summary:	An X Window System tool for creating morphed images
Name:		xmorph
Version:	1996.07.12
Release:	7
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.x.org/contrib/graphics/%{name}-11sep97.tar.gz
Patch0:		xmorph-11sep97-make.patch
Patch1:		xmorph-11sep97-glibc.patch
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

%prep
%setup -q -n xmorph-11sep97
%patch0 -p1
%patch1 -p1

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s xmorph $RPM_BUILD_ROOT%{_bindir}
install xmorph.man $RPM_BUILD_ROOT%{_mandir}/man1/xmorph.1x

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/xmorph.1x \
	README HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz HISTORY.gz
%attr(755,root,root) %{_bindir}/xmorph
%{_mandir}/man1/xmorph.1x.gz
