Name     : pandoc
Version  : 2.1.1
Release  : 5
URL      : https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-linux.tar.gz
Source0  : https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-linux.tar.gz
Summary  : The universal markup converter
Group    : Development/Tools
License  : GPL-2.0 WTFPL MIT BSD-3-Clause

%description
Pandoc is a Haskell library for converting from one markup format to another, 
and a command-line tool that uses this library.

%prep
%setup -q -n pandoc-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515085191

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr
cp -r bin %{buildroot}/usr/
cp -r share %{buildroot}/usr/

%files
%defattr(-,root,root,-)
/usr/bin/pandoc
/usr/bin/pandoc-citeproc
/usr/share/man/man1/pandoc-citeproc.1.gz
/usr/share/man/man1/pandoc.1.gz
