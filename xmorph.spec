Summary: An X Window System tool for creating morphed images.
Name: xmorph
Version: 1996.07.12
Release: 7
Copyright: GPL
Group: Amusements/Graphics
Source: ftp://ftp.x.org/contrib/graphics/xmorph-11sep97.tar.gz
Patch: xmorph-11sep97-make.patch
Patch1: xmorph-11sep97-glibc.patch
Prefix: /usr
BuildRoot: /var/tmp/xmorph-root

%description
Xmorph is a digital image warping (aka morphing) program.  Xmorph
provides the tools needed and comprehensible instructions for you to
create morphs:  changing one image into another.  Xmorph runs under the
X Window System.

Install the xmorph package if you need a program that will create morphed
images.

%prep
%setup -q -n xmorph-11sep97
%patch0 -p1 -b .make
%patch1 -p1 -b .glibc

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

install -s xmorph $RPM_BUILD_ROOT/usr/X11R6/bin
install xmorph.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xmorph.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README HISTORY
/usr/X11R6/bin/xmorph
/usr/X11R6/man/man1/xmorph.1
