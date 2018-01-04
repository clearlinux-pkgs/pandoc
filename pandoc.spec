#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pandoc
Version  : 1.0.2
Release  : 1
URL      : https://pypi.debian.net/pandoc/pandoc-1.0.2.tar.gz
Source0  : https://pypi.debian.net/pandoc/pandoc-1.0.2.tar.gz
Summary  : Pandoc Documents for Python
Group    : Development/Tools
License  : MIT
Requires: pandoc-python3
Requires: pandoc-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : ply-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pandoc (Python Library)
=======================
|Python| |PyPi| |Status| |Build Status|

%package python
Summary: python components for the pandoc package.
Group: Default
Requires: pandoc-python3

%description python
python components for the pandoc package.


%package python3
Summary: python3 components for the pandoc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pandoc package.


%prep
%setup -q -n pandoc-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515085191
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
