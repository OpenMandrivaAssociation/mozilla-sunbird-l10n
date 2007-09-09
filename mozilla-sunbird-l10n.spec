

%define name    mozilla-sunbird-l10n
%define oname   mozilla-sunbird
%define version 0.5
%define release %mkrel 1

%define sunbird_package mozilla-sunbird
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
Localisations for Sunbird
#-------------------------------------------------------------------

%package -n %{oname}-ca
%define  language_ca  ca
%define  locale_ca %(echo %language_ca|sed -e 's/-.*//g')
%define  langname_ca Catalan

Summary: %{langname_ca} interface for Sunbird
Source0: %xpidir/ca.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_ca}


%description  -n %{oname}-ca
%{langname_ca} localization for Sunbird

%files -n %{oname}-ca
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_ca}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome/calendar-ca.jar
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/chrome/ca.jar
%{mozillalibdir}/extensions/langpack-ca@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-cs
%define  language_cs  cs
%define  locale_cs %(echo %language_cs|sed -e 's/-.*//g')
%define  langname_cs Czech

Summary: %{langname_cs} interface for Sunbird
Source1: %xpidir/cs.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_cs}


%description  -n %{oname}-cs
%{langname_cs} localization for Sunbird

%files -n %{oname}-cs
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_cs}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome/calendar-cs.jar
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/chrome/cs.jar
%{mozillalibdir}/extensions/langpack-cs@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-da
%define   language_da  da
%define   locale_da %(echo %language_da|sed -e 's/-.*//g')
%define   langname_da Dansk

Summary:  %{langname_da} interface for Sunbird
Source2:  %xpidir/da.xpi
Patch2 :  mozilla-sunbird-da-fix-xml.patch
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_da}


%description  -n %{oname}-da
%{langname_da} localization for Sunbird

%files -n %{oname}-da
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_da}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome/calendar-da.jar
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/chrome/da.jar
%{mozillalibdir}/extensions/langpack-da@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------
%package -n %{oname}-de
%define   language_de  de
%define   locale_de %(echo %language_de|sed -e 's/-.*//g')
%define   langname_de German

Summary:  %{langname_de} interface for Sunbird
Source3:  %xpidir/de.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_de}


%description  -n %{oname}-de
%{langname_da} localization for Sunbird

%files -n %{oname}-de
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_de}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome/calendar-de.jar
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/chrome/de.jar
%{mozillalibdir}/extensions/langpack-de@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------
%package -n %{oname}-es
%define   language_es  es-ES
%define   locale_es %(echo %language_es|sed -e 's/-.*//g')
%define   langname_es Spanish

Summary:  %{langname_es} interface for Sunbird
Source4:  %xpidir/es-ES.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_es}


%description  -n %{oname}-es
%{langname_da} localization for Sunbird

%files -n %{oname}-es
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_es}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome/calendar-es-ES.jar
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/chrome/es-ES.jar
%{mozillalibdir}/extensions/langpack-es@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-eu
%define   language_eu  eu
%define   locale_eu %(echo %language_eu|sed -e 's/-.*//g')
%define   langname_eu Basque

Summary:  %{langname_eu} interface for Sunbird
Source5:  %xpidir/eu.xpi
License:  GPL
Group:    Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_eu}


%description  -n %{oname}-eu
%{langname_da} localization for Sunbird

%files -n %{oname}-eu
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_eu}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome/calendar-eu.jar
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/chrome/eu.jar
%{mozillalibdir}/extensions/langpack-eu@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-fr
%define  language_fr  fr
%define  locale_fr %(echo %language_fr|sed -e 's/-.*//g')
%define  langname_fr French

Summary: %{langname_fr} interface for Sunbird
Source6: %xpidir/fr.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_fr}


%description  -n %{oname}-fr
%{langname_fr} localization for Sunbird

%files -n %{oname}-fr
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_fr}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome/calendar-fr.jar
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/chrome/fr.jar
%{mozillalibdir}/extensions/langpack-fr@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-ga
%define  language_ga  ga-IE
%define  locale_ga %(echo %language_ga|sed -e 's/-.*//g')
%define  langname_ga Irish

Summary: %{langname_ga} interface for Sunbird
Source7: %xpidir/ga-IE.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_ga}


%description  -n %{oname}-ga
%{langname_ga} localization for Sunbird

%files -n %{oname}-ga
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_ga}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome/calendar-ga-IE.jar
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/chrome/ga-IE.jar
%{mozillalibdir}/extensions/langpack-ga@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-hu
%define  language_hu  hu
%define  locale_hu %(echo %language_hu|sed -e 's/-.*//g')
%define  langname_hu Hungarian

Summary: %{langname_hu} interface for Sunbird
Source8: %xpidir/hu.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_hu}


%description  -n %{oname}-hu
%{langname_hu} localization for Sunbird

%files -n %{oname}-hu
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_hu}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome/calendar-hu.jar
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/chrome/hu.jar
%{mozillalibdir}/extensions/langpack-hu@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-it
%define  language_it  it
%define  locale_it %(echo %language_it|sed -e 's/-.*//g')
%define  langname_it Italian

Summary: %{langname_it} interface for Sunbird
Source9: %xpidir/it.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_it}


%description  -n %{oname}-it
%{langname_hu} localization for Sunbird

%files -n %{oname}-it
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_it}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome/calendar-it.jar
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/chrome/it.jar
%{mozillalibdir}/extensions/langpack-it@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-mk
%define  language_mk  mk
%define  locale_mk %(echo %language_mk|sed -e 's/-.*//g')
%define  langname_mk Macedonian

Summary: %{langname_mk} interface for Sunbird
Source10: %xpidir/mk.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_mk}


%description  -n %{oname}-mk
%{langname_mk} localization for Sunbird

%files -n %{oname}-mk
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_mk}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-mk@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-mk@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-mk@sunbird.mozilla.org/chrome/calendar-mk.jar
%{mozillalibdir}/extensions/langpack-mk@sunbird.mozilla.org/chrome/mk.jar
%{mozillalibdir}/extensions/langpack-mk@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-mn
%define  language_mn  mn
%define  locale_mn %(echo %language_mn|sed -e 's/-.*//g')
%define  langname_mn Mongolian

Summary: %{langname_mn} interface for Sunbird
Source11: %xpidir/mn.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_mn}


%description  -n %{oname}-mn
%{langname_mn} localization for Sunbird

%files -n %{oname}-mn
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome/calendar-mn.jar
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/chrome/mn.jar
%{mozillalibdir}/extensions/langpack-mn@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-nb
%define  language_nb  nb-NO
%define  locale_nb %(echo %language_nb|sed -e 's/-.*//g')
%define  langname_nb Norwegian

Summary: %{langname_nb} interface for Sunbird
Source12: %xpidir/nb-NO.xpi
Patch12:  nb-NO-utf8.patch
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_nb}


%description  -n %{oname}-nb
%{langname_nb} localization for Sunbird

%files -n %{oname}-nb
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_nb}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-nb@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-nb@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-nb@sunbird.mozilla.org/chrome/calendar-nb-NO.jar
%{mozillalibdir}/extensions/langpack-nb@sunbird.mozilla.org/chrome/nb-NO.jar
%{mozillalibdir}/extensions/langpack-nb@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-nl
%define  language_nl  nl
%define  locale_nl %(echo %language_nl|sed -e 's/-.*//g')
%define  langname_nl Dutch

Summary: %{langname_nl} interface for Sunbird
Source13: %xpidir/nl.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_nl}


%description  -n %{oname}-nl
%{langname_nl} localization for Sunbird

%files -n %{oname}-nl
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome/calendar-nl.jar
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/chrome/nl.jar
%{mozillalibdir}/extensions/langpack-nl@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-pa
%define  language_pa  pa-IN
%define  locale_pa %(echo %language_pa|sed -e 's/-.*//g')
%define  langname_pa Punjabi

Summary: %{langname_pa} interface for Sunbird
Source14: %xpidir/pa-IN.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_pa}


%description  -n %{oname}-pa
%{langname_pa} localization for Sunbird

%files -n %{oname}-pa
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_pa}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-pa@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-pa@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-pa@sunbird.mozilla.org/chrome/calendar-pa-IN.jar
%{mozillalibdir}/extensions/langpack-pa@sunbird.mozilla.org/chrome/pa-IN.jar
%{mozillalibdir}/extensions/langpack-pa@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-pl
%define  language_pl  pl
%define  locale_pl %(echo %language_pl|sed -e 's/-.*//g')
%define  langname_pl Polish

Summary: %{langname_pl} interface for Sunbird
Source15: %xpidir/pl.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_pl}


%description  -n %{oname}-pl
%{langname_pl} localization for Sunbird

%files -n %{oname}-pl
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_pl}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-pl@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-pl@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-pl@sunbird.mozilla.org/chrome/calendar-pl.jar
%{mozillalibdir}/extensions/langpack-pl@sunbird.mozilla.org/chrome/pl.jar
%{mozillalibdir}/extensions/langpack-pl@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-pt
%define  language_pt  pt-BR
%define  locale_pt %(echo %language_pt|sed -e 's/-.*//g')
%define  langname_pt Portuguese

Summary: %{langname_pt} interface for Sunbird
Source16: %xpidir/pt-BR.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_pt}


%description  -n %{oname}-pt
%{langname_pt} localization for Sunbird

%files -n %{oname}-pt
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_pt}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-pt@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-pt@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-pt@sunbird.mozilla.org/chrome/calendar-pt-BR.jar
%{mozillalibdir}/extensions/langpack-pt@sunbird.mozilla.org/chrome/pt-BR.jar
%{mozillalibdir}/extensions/langpack-pt@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-ru
%define  language_ru  ru
%define  locale_ru %(echo %language_ru|sed -e 's/-.*//g')
%define  langname_ru Russian

Summary: %{langname_ru} interface for Sunbird
Source17: %xpidir/ru.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_ru}


%description  -n %{oname}-ru
%{langname_ru} localization for Sunbird

%files -n %{oname}-ru
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_ru}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-ru@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-ru@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-ru@sunbird.mozilla.org/chrome/calendar-ru.jar
%{mozillalibdir}/extensions/langpack-ru@sunbird.mozilla.org/chrome/ru.jar
%{mozillalibdir}/extensions/langpack-ru@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-sk
%define  language_sk  sk
%define  locale_sk %(echo %language_sk|sed -e 's/-.*//g')
%define  langname_sk Slovak

Summary: %{langname_sk} interface for Sunbird
Source18: %xpidir/sk.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_sk}


%description  -n %{oname}-sk
%{langname_sk} localization for Sunbird

%files -n %{oname}-sk
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_sk}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-sk@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-sk@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-sk@sunbird.mozilla.org/chrome/calendar-sk.jar
%{mozillalibdir}/extensions/langpack-sk@sunbird.mozilla.org/chrome/sk.jar
%{mozillalibdir}/extensions/langpack-sk@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-sl
%define  language_sl  sl
%define  locale_sl %(echo %language_sl|sed -e 's/-.*//g')
%define  langname_sl Slovenian

Summary: %{langname_sl} interface for Sunbird
Source19: %xpidir/sl.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_sl}


%description  -n %{oname}-sl
%{langname_sl} localization for Sunbird

%files -n %{oname}-sl
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_sl}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-sl@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-sl@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-sl@sunbird.mozilla.org/chrome/calendar-sl.jar
%{mozillalibdir}/extensions/langpack-sl@sunbird.mozilla.org/chrome/sl.jar
%{mozillalibdir}/extensions/langpack-sl@sunbird.mozilla.org/install.rdf

#-------------------------------------------------------------------

%package -n %{oname}-sv
%define  language_sv  sv-SE
%define  locale_sv %(echo %language_sv|sed -e 's/-.*//g')
%define  langname_sv Swedish

Summary: %{langname_sv} interface for Sunbird
Source20: %xpidir/sv-SE.xpi
License: GPL
Group:   Networking/WWW
Url:      http://www.mozilla.org/products/sunbird/
Requires: %{sunbird_package} = %{sunbird_version}
Requires: locales-%{locale_sv}


%description  -n %{oname}-sv
%{langname_sv} localization for Sunbird

%files -n %{oname}-sv
%defattr(644,root,root,755)
%dir %{mozillalibdir}/extensions/langpack-%{locale_sv}@sunbird.mozilla.org
%{mozillalibdir}/extensions/langpack-sv@sunbird.mozilla.org/chrome.manifest
%{mozillalibdir}/extensions/langpack-sv@sunbird.mozilla.org/chrome/chromelist.txt
%{mozillalibdir}/extensions/langpack-sv@sunbird.mozilla.org/chrome/calendar-sv-SE.jar
%{mozillalibdir}/extensions/langpack-sv@sunbird.mozilla.org/chrome/sv-SE.jar
%{mozillalibdir}/extensions/langpack-sv@sunbird.mozilla.org/install.rdf

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
patch -p0 < %{PATCH2}
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

# Mk translation
unzip  %SOURCE10
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mk}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mk}@sunbird.mozilla.org/
rm -fr *

# Mn translation
unzip  %SOURCE11
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_mn}@sunbird.mozilla.org/
rm -fr *

# Nb translation
unzip  %SOURCE12
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nb}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nb}@sunbird.mozilla.org/
cd %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nb}@sunbird.mozilla.org/
patch -p0 < %{PATCH12}
cd -
rm -fr *

# Nl translation
unzip  %SOURCE13
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_nl}@sunbird.mozilla.org/
rm -fr *

# Pa translation
unzip  %SOURCE14
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pa}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pa}@sunbird.mozilla.org/
rm -fr *

# Pl translation
unzip  %SOURCE15
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pl}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pl}@sunbird.mozilla.org/
rm -fr *

# Pt translation
unzip  %SOURCE16
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pt}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_pt}@sunbird.mozilla.org/
rm -fr *

# Ru translation
unzip  %SOURCE17
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ru}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_ru}@sunbird.mozilla.org/
rm -fr *

# Sk translation
unzip  %SOURCE18
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sk}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sk}@sunbird.mozilla.org/
rm -fr *

# Sl translation
unzip  %SOURCE19
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sl}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sl}@sunbird.mozilla.org/
rm -fr *

# Sv translation
unzip  %SOURCE20
mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sv}@sunbird.mozilla.org/
cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-%{locale_sv}@sunbird.mozilla.org/
rm -fr *

# disable version check
#sed -i -e 's/maxVersion>.*</maxVersion>2.0.*</g' %buildroot%{mozillalibdir}/extensions/langpack-*@sunbird.mozilla.org/install.rdf

# all install.rdf files must validate
xmllint --noout %buildroot%{mozillalibdir}/extensions/langpack-*@sunbird.mozilla.org/install.rdf

%clean
rm -rf $RPM_BUILD_ROOT


