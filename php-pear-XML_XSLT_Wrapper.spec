%define		_class		XML
%define		_subclass	XSLT
%define		_pearname	%{_class}_%{_subclass}_Wrapper

%define		_requires_exceptions pear(XSLT/XSLT_Wrapper.php)

Summary:	%{_pearname} - single interface to the different XSLT interface or commands
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	%mkrel 7
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/XML_XSLT_Wrapper/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend

install %{_pearname}-%{version}/XSLT_Wrapper.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper.php
install %{_pearname}-%{version}/Backend/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend

# remove windows class:
rm %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend/*Com.php

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{TODO,examples/*}
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Wrapper
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Wrapper/Backend/*.php

%{_datadir}/pear/packages/%{_pearname}.xml


