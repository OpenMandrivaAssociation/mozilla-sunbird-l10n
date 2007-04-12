%if %mdkversion == 300
%define build_for_corp3 1
%else
%define build_for_corp3 0
%endif

%if %build_for_corp3
%define distversion C30
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}
%endif

%if %mdkversion < 200700
%define subrel 2
%endif
%define sunbird_package mozilla-sunbird


%define name    mozilla-sunbird-l10n
%define oname   mozilla-sunbird
%define version 0.3.1
%define release %mkrel 2
%define _buildroot %{_tmppath}/%{name}-buildroot
%define sunbird_version %{version}
%define mozillalibdir %{_libdir}/sunbird-%{sunbird_version}
%define xpidir http://releases.mozilla.org/pub/mozilla.org/calendar/sunbird/releases/%version/langpacks/

Summary:   Localisations for Sunbird (virtual package)
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Group:     Networking/WWW
Url:       http://www.mozilla.org/
BuildRoot: %{_buildroot}
BuildRequires: libxml2-utils

%description
Localisations for Firefox
#-------------------------------------------------------------------

%package -n %{oname}-ca
%define  language_ca  ca
%define  locale_ca %(echo %language_ca|sed -e 's/-.*//g')
%define  langname_ca Catalan

Summary: %{langname_ca} interface for Firefox
Source0: %xpidir/sunbird-0.3.ca.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_ca}


%description  -n %{oname}-ca
%{langname_ca} localization for Firefox

%files -n %{oname}-ca
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_ca}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome/calendar-ca.jar
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome/ca.jar
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-cs
%define  language_cs  cs
%define  locale_cs %(echo %language_cs|sed -e 's/-.*//g')
%define  langname_cs Czech

Summary: %{langname_cs} interface for Firefox
Source1: %xpidir/sunbird-0.3.cs.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_cs}


%description  -n %{oname}-cs
%{langname_cs} localization for Firefox

%files -n %{oname}-cs
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_cs}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome/calendar-cs.jar
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome/cs.jar
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-da
%define   language_da  da
%define   locale_da %(echo %language_da|sed -e 's/-.*//g')
%define   langname_da Dansk

Summary:  %{langname_da} interface for Firefox
Source2:  %xpidir/sunbird-0.3.da.langpack.xpi
Patch0 :  mozilla-sunbird-da-fix-xml.patch
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_da}


%description  -n %{oname}-da
%{langname_da} localization for Firefox

%files -n %{oname}-da
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_da}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome/calendar-da.jar
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome/da.jar
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------
%package -n %{oname}-de
%define   language_de  de
%define   locale_de %(echo %language_de|sed -e 's/-.*//g')
%define   langname_de German

Summary:  %{langname_de} interface for Firefox
Source3:  %xpidir/sunbird-0.3.de.langpack.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_de}


%description  -n %{oname}-de
%{langname_da} localization for Firefox

%files -n %{oname}-de
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_de}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome/calendar-de.jar
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome/de.jar
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------
%package -n %{oname}-es
%define   language_es  es-ES
%define   locale_es %(echo %language_es|sed -e 's/-.*//g')
%define   langname_es Spanish

Summary:  %{langname_es} interface for Firefox
Source4:  %xpidir/sunbird-0.3.es-ES.langpack.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_es}


%description  -n %{oname}-es
%{langname_da} localization for Firefox

%files -n %{oname}-es
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_es}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome/calendar-es-ES.jar
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome/es-ES.jar
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-eu
%define   language_eu  eu
%define   locale_eu %(echo %language_eu|sed -e 's/-.*//g')
%define   langname_eu Basque

Summary:  %{langname_eu} interface for Firefox
Source5:  %xpidir/sunbird-0.3.eu.langpack.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_eu}


%description  -n %{oname}-eu
%{langname_da} localization for Firefox

%files -n %{oname}-eu
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_eu}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome/calendar-eu.jar
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome/eu.jar
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-fr
%define  language_fr  fr
%define  locale_fr %(echo %language_fr|sed -e 's/-.*//g')
%define  langname_fr French

Summary: %{langname_fr} interface for Firefox
Source6: %xpidir/sunbird-0.3.fr.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_fr}


%description  -n %{oname}-fr
%{langname_fr} localization for Firefox

%files -n %{oname}-fr
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_fr}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome/calendar-fr.jar
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome/fr.jar
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-ga
%define  language_ga  ga-IE
%define  locale_ga %(echo %language_ga|sed -e 's/-.*//g')
%define  langname_ga Irish

Summary: %{langname_ga} interface for Firefox
Source7: %xpidir/sunbird-0.3.ga-IE.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_ga}


%description  -n %{oname}-ga
%{langname_ga} localization for Firefox

%files -n %{oname}-ga
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_ga}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome/calendar-ga-IE.jar
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome/ga-IE.jar
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-hu
%define  language_hu  hu
%define  locale_hu %(echo %language_hu|sed -e 's/-.*//g')
%define  langname_hu Hungarian

Summary: %{langname_hu} interface for Firefox
Source8: %xpidir/sunbird-0.3.hu.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_hu}


%description  -n %{oname}-hu
%{langname_hu} localization for Firefox

%files -n %{oname}-hu
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_hu}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome/calendar-hu.jar
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome/hu.jar
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-it
%define  language_it  it
%define  locale_it %(echo %language_it|sed -e 's/-.*//g')
%define  langname_it Italian

Summary: %{langname_it} interface for Firefox
Source9: %xpidir/sunbird-0.3.it.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_it}


%description  -n %{oname}-it
%{langname_hu} localization for Firefox

%files -n %{oname}-it
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_it}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome/calendar-it.jar
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome/it.jar
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-mn
%define  language_mn  mn
%define  locale_mn %(echo %language_mn|sed -e 's/-.*//g')
%define  langname_mn Mongolian

Summary: %{langname_mn} interface for Firefox
Source10: %xpidir/sunbird-0.3.mn.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_mn}


%description  -n %{oname}-mn
%{langname_hu} localization for Firefox

%files -n %{oname}-mn
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome/calendar-mn.jar
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome/mn.jar
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-nl
%define  language_nl  nl
%define  locale_nl %(echo %language_nl|sed -e 's/-.*//g')
%define  langname_nl Dutch

Summary: %{langname_nl} interface for Firefox
Source11: %xpidir/sunbird-0.3.nl.langpack.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_nl}


%description  -n %{oname}-nl
%{langname_hu} localization for Firefox

%files -n %{oname}-nl
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome/calendar-nl.jar
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome/nl.jar
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------


%prep
%setup -q -c -T

%build

%install
rm -rf %buildroot

# Ca translation
unzip  %SOURCE0
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ca}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ca}@sunbird.mozilla.org/
rm -fr *

# Cs translation
unzip  %SOURCE1
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_cs}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_cs}@sunbird.mozilla.org/
rm -fr *

# Da translation
unzip  %SOURCE2
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_da}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_da}@sunbird.mozilla.org/
cd %buildroot%{mozillalibdir}/extensions/langpack-%{locale_da}@sunbird.mozilla.org/
patch -p0 < %{PATCH0}
cd -
rm -fr *

# De translation
unzip  %SOURCE3
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_de}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_de}@sunbird.mozilla.org/
rm -fr *

# Es translation
unzip  %SOURCE4
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_es}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_es}@sunbird.mozilla.org/
rm -fr *

# Eu translation
unzip  %SOURCE5
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_eu}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_eu}@sunbird.mozilla.org/
rm -fr *

# Fr translation
unzip  %SOURCE6
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_fr}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_fr}@sunbird.mozilla.org/
rm -fr *

# Ga translation
unzip  %SOURCE7
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ga}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ga}@sunbird.mozilla.org/
rm -fr *

# Hu translation
unzip  %SOURCE8
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_hu}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_hu}@sunbird.mozilla.org/
rm -fr *

# It translation
unzip  %SOURCE9
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_it}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_it}@sunbird.mozilla.org/
rm -fr *

# Mn translation
unzip  %SOURCE10
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org/
rm -fr *

# Nl translation
unzip  %SOURCE11
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org/
rm -fr *

# disable version check
#sed -i -e 's/maxVersion>.*</maxVersion>2.0.*</g' %buildroot%{mozillalibdir}/extensions/langpack-*@sunbird.mozilla.org/install.rdf

# all install.rdf files must validate
xmllint --noout %buildroot%{mozillalibdir}/extensions/langpack-*@sunbird.mozilla.org/install.rdf

%clean
rm -rf $RPM_BUILD_ROOT


