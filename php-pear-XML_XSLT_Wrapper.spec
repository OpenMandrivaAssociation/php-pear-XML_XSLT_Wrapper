%define		_class		XML
%define		_subclass	XSLT
%define		upstream_name	%{_class}_%{_subclass}_Wrapper

Name:		php-pear-%{upstream_name}
Version:	0.2.2
Release:	8
Summary:	Single interface to the different XSLT interface or commands
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
URL:		https://pear.php.net/package/XML_XSLT_Wrapper/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/TODO
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-6mdv2012.0
+ Revision: 742315
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-5
+ Revision: 679617
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-4mdv2011.0
+ Revision: 613802
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-3mdv2010.1
+ Revision: 464972
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-2mdv2010.0
+ Revision: 441771
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 368305
- Update php pear XML_XSLT_Wrapper to 0.2.2 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-9mdv2009.1
+ Revision: 323007
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-8mdv2009.0
+ Revision: 237175
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-7mdv2007.0
+ Revision: 82966
- Import php-pear-XML_XSLT_Wrapper

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdk
- initial Mandriva package (PLD import)

