%define name    mozilla-sunbird-l10n
%define oname   mozilla-sunbird
%define version 0.9
%define release %mkrel 5

%define sunbird_package mozilla-sunbird
%define sunbird_version %{version}
%define sunbird_appid \{718e30fb-e89b-41dd-9da7-e25a45638b28\}
%define sunbird_extdir %{_datadir}/mozilla/extensions/%{sunbird_appid}
%define xpidir http://releases.mozilla.org/pub/mozilla.org/calendar/sunbird/releases/%version/langpacks/

# Supported l10n language lists
%define langlist	ca cs da de es_AR es_ES eu fr ga hu is it ja ka ko lt mk mn nb_NO nl nn_NO pa_IN pl pt_BR pt_PT ro ru sk sl sv_SE tr uk zh_CN zh_TW

# Disabled l10n languages, for any reason
%define disabled_langlist	%{nil}

# Disabled myspell dicts, for any reason
%define disabled_dict_langlist	eu ja ko mk mn pa_IN tr zh_CN zh_TW

%define use_dict 1
%if %mdkversion == 200600
# CS4 doesn't have myspell, but has firefox.
%define use_dict 0
%endif
%if %mdkversion >= 200810
# We moved to pointing mozilladir/dictionaries -> /usr/share/dict/mozilla
%define use_dict 0
%endif

# Language descriptions
%define language_ca ca
%define langname_ca Catalan
%define language_cs cs
%define langname_cs Czech
%define language_da da
%define langname_da Dansk
%define language_de de
%define langname_de German
%define language_es_AR es-AR
%define langname_es_AR Spanish (Argentina)
%define language_es_ES es-ES
%define langname_es_ES Spanish
%define language_eu eu
%define langname_eu Basque
%define language_fr fr
%define langname_fr French
%define language_ga ga-IE
%define langname_ga Irish
%define language_hu hu
%define langname_hu Hungarian
%define language_is is
%define langname_is Icelandic
%define language_it it
%define langname_it Italian
%define language_ja ja
%define langname_ja Japanese
%define language_ka ka
%define langname_ka Georgian
%define language_ko ko
%define langname_ko Korean
%define language_lt lt
%define langname_lt Lithuanian
%define language_mk mk
%define langname_mk Macedonian
%define language_mn mn
%define langname_mn Mongolian
%define language_nb_NO nb-NO
%define langname_nb_NO Norwegian Bokmaal
%define language_nl nl
%define langname_nl Dutch
%define language_nn_NO nn-NO
%define langname_nn_NO Norwegian Nynorsk
%define language_pa_IN pa-IN
%define langname_pa_IN Punjabi (gurmukhi)
%define language_pl pl
%define langname_pl Polish
%define language_pt_BR pt-BR
%define langname_pt_BR Brazilian portuguese
%define language_pt_PT pt-PT
%define langname_pt_PT Portuguese
%define language_ro ro
%define langname_ro Romanian
%define language_ru ru
%define langname_ru Russian
%define language_sk sk
%define langname_sk Slovak
%define language_sl sl
%define langname_sl Slovenian
%define language_sv_SE sv-SE
%define langname_sv_SE Swedish
%define language_tr tr
%define langname_tr Turkish
%define language_uk uk
%define langname_uk Ukrainian
%define language_zh_CN zh-CN
%define langname_zh_CN Simplified Chinese
%define language_zh_TW zh-TW
%define langname_zh_TW Traditional Chinese

# --- Danger line ---

# Defaults (all languages enabled by default)
# l10n
%{expand:%(for lang in %langlist; do echo "%%define with_$lang 1"; done)}
%{expand:%(for lang in %disabled_langlist; do echo "%%define with_$lang 0"; done)}
# dicts
%if %use_dict
%{expand:%(for lang in %langlist; do echo "%%define with_dict_$lang 1"; done)}
%{expand:%(for lang in %disabled_dict_langlist; do echo "%%define with_dict_$lang 0"; done)}
%else
%{expand:%(for lang in %langlist; do echo "%%define with_dict_$lang 0"; done)}
%{expand:%(for lang in %disabled_dict_langlist; do echo "%%define with_dict_$lang 0"; done)}
%endif

# Locales
%{expand:%(for lang in %langlist; do echo "%%define locale_$lang `echo $lang | cut -d _ -f 1` "; done)}

%if %use_dict
# myspell dicts, allows setting preferences between several providers.
%{expand:%(for lang in %langlist; do echo "%%define myspell_$lang myspell-$lang"; done)}
%define myspell_de myspell-de_DE
%define myspell_fr myspell-fr_FR
%endif

Summary: Localizations for Sunbird (virtual package)
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/WWW
Url: http://www.mozilla.org/projects/calendar/sunbird/
BuildArch: noarch
# Language package template
Source0: %{name}-template.in
# l10n sources
%{expand:%(\
	i=1;\
	for lang in %langlist; do\
		echo "%%{expand:Source$i: %{xpidir}/%%{language_$lang}.xpi}";\
		i=$[i+1];\
	done\
	)
}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-utils
%if %use_dict
%{expand:%(\
	disabled="%{disabled_dict_langlist}";\
	for lang in %langlist; do\
		echo "$disabled" | grep -q "\<$lang\>" || \
			echo "BuildRequires: %%{myspell_$lang}";\
	done\
	)
}
%endif

%description
Localizations for Sunbird

# Expand all languages packages.
%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %{_sourcedir}/%{name}-template.in 2> /dev/null)}";\
	done\
	)
}

%prep
%setup -q -c -T

# Convert rpm macros to bash variables
%{expand:%(for lang in %langlist; do echo "language_$lang=%%{language_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "locale_$lang=%%{locale_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "with_$lang=%%{with_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "dict_$lang=%%{with_dict_$lang}"; done)}

# Unpack all languages
for lang in %langlist; do
	with="with_$lang"
	with=${!with}
	[ $with -eq 0 ] && continue

	language="language_$lang"
	language=${!language}

	locale="locale_$lang"
	locale=${!locale}

	# l10n
	mkdir ${language}
	cd ${language}
	unzip -qq %{_sourcedir}/${language}.xpi
	cd ..

	# dict
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

done

%build
# All install.rdf files must validate
xmllint --noout */install.rdf

%install
rm -rf %buildroot

# Convert rpm macros to bash variables
%{expand:%(for lang in %langlist; do echo "language_$lang=%%{language_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "with_$lang=%%{with_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "dict_$lang=%%{with_dict_$lang}"; done)}

# Install all languages
for lang in %langlist; do
	with="with_$lang"
	with=${!with}
	[ $with -eq 0 ] && continue

	language="language_$lang"
	language=${!language}

	# l10n
	cd $language
	mkdir -p %buildroot%{sunbird_extdir}/langpack-${language}@sunbird.mozilla.org/
	cp -f -r * %buildroot%{sunbird_extdir}/langpack-${language}@sunbird.mozilla.org/
	cd ..

	# Dicts
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

done

%clean
rm -rf %buildroot



%changelog
* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.9-5mdv2011.0
+ Revision: 634039
- restruct to new mozilla layout

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-4mdv2011.0
+ Revision: 620397
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.9-3mdv2010.0
+ Revision: 440140
- rebuild

* Mon Jan 12 2009 Funda Wang <fwang@mandriva.org> 0.9-2mdv2009.1
+ Revision: 328580
- rebuild for new rpm

* Fri Nov 21 2008 Funda Wang <fwang@mandriva.org> 0.9-1mdv2009.1
+ Revision: 305431
- drop merged patch
- update URL
- New version 0.9

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.8-4mdv2009.0
+ Revision: 268150
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.8-3mdv2009.0
+ Revision: 206538
- fix obsolete old package

* Fri May 09 2008 Funda Wang <fwang@mandriva.org> 0.8-2mdv2009.0
+ Revision: 204812
- obsoletes old lang packages

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.8-1mdv2009.0
+ Revision: 200989
- Switch to firefox-l10n template
- New version 0.8

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Jérôme Soyer <saispo@mandriva.org> 0.7-1mdv2008.1
+ Revision: 103865
- Update

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-2mdv2008.0
+ Revision: 89950
- rebuild

* Sun Sep 09 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5-1mdv2008.0
+ Revision: 83452
- Update for Sunbird 0.5


* Sun Feb 25 2007 Jérôme Soyer <saispo@mandriva.org> 0.3.1-2mdv2007.0
+ Revision: 125445
- Rebuild

* Fri Dec 08 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-1mdv2007.1
+ Revision: 93603
- Import mozilla-sunbird-l10n

