%define		_class		XML
%define		_subclass	XSLT
%define		upstream_name	%{_class}_%{_subclass}_Wrapper

%define		_requires_exceptions pear(XSLT/XSLT_Wrapper.php)

Name:		php-pear-%{upstream_name}
Version:	0.2.2
Release:	%mkrel 6
Summary:	Single interface to the different XSLT interface or commands
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
URL:		http://pear.php.net/package/XML_XSLT_Wrapper/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package was written to provide a simpler, cross-library and cross
commands interface to doing XSL transformations. It provides support
for: DOM XSLT PHP extension, XSLT PHP extension, MSXML using COM PHP
extension, XT command line
(http://www.blnz.com/xt/xt-20020426a-src/index.html), Sablotron
command line
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
XT java interface, xml.apache.org java and C interface
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Batch mode: XML:
multiple transformations of a single XML file, XSL: multiple
transformations of multiple XML files using a single XSL.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

# remove windows class:
rm %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend/*Com.php

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/TODO
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


