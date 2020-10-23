#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pandoc
Version  : 2.11.0.4
Release  : 12
URL      : https://github.com/jgm/pandoc/releases/download/2.11.0.4/pandoc-2.11.0.4-linux-amd64.tar.gz
Source0  : https://github.com/jgm/pandoc/releases/download/2.11.0.4/pandoc-2.11.0.4-linux-amd64.tar.gz
Summary  : The universal markup converter
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT WTFPL
Requires: pandoc-bin = %{version}-%{release}
Requires: pandoc-man = %{version}-%{release}

%description
Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library.

%package bin
Summary: bin components for the pandoc package.
Group: Binaries

%description bin
bin components for the pandoc package.


%package man
Summary: man components for the pandoc package.
Group: Default

%description man
man components for the pandoc package.


%prep
%setup -q -n pandoc-2.11.0.4
cd %{_builddir}/pandoc-2.11.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603479728
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  || :


%install
export SOURCE_DATE_EPOCH=1603479728
rm -rf %{buildroot}
:
## install_append content
mkdir -p %{buildroot}/usr
cp -r bin %{buildroot}/usr/
cp -r share %{buildroot}/usr/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pandoc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pandoc.1.gz
