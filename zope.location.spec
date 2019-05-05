#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.location
Version  : 4.2
Release  : 20
URL      : https://files.pythonhosted.org/packages/0c/c3/f9ab5358f8289fbd1996075ae1d7914b25cbfc1a65823ae0258aec03837d/zope.location-4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/c3/f9ab5358f8289fbd1996075ae1d7914b25cbfc1a65823ae0258aec03837d/zope.location-4.2.tar.gz
Summary  : Zope Location
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.location-license = %{version}-%{release}
Requires: zope.location-python = %{version}-%{release}
Requires: zope.location-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.component
Requires: zope.interface
Requires: zope.proxy
Requires: zope.schema
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : zope.event
BuildRequires : zope.interface
BuildRequires : zope.proxy
BuildRequires : zope.schema

%description
===================
``zope.location``
===================
.. image:: https://img.shields.io/pypi/v/zope.location.svg
:target: https://pypi.python.org/pypi/zope.location/
:alt: Latest release

%package license
Summary: license components for the zope.location package.
Group: Default

%description license
license components for the zope.location package.


%package python
Summary: python components for the zope.location package.
Group: Default
Requires: zope.location-python3 = %{version}-%{release}

%description python
python components for the zope.location package.


%package python3
Summary: python3 components for the zope.location package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.location package.


%prep
%setup -q -n zope.location-4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557023557
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.location
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.location/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.location/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
