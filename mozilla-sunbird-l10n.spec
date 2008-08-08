%define name    mozilla-sunbird-l10n
%define oname   mozilla-sunbird
%define version 0.8
%define release %mkrel 4

%define sunbird_package mozilla-sunbird
%define sunbird_version %{version}
%define mozillalibdir %{_libdir}/sunbird-%{sunbird_version}
%define xpidir http://releases.mozilla.org/pub/mozilla.org/calendar/sunbird/releases/%version/langpacks/

# Supported l10n language lists
%define langlist	ca cs da de es_AR es_ES eu fr ga hu it ja ka ko lt mk mn nb_NO nl pa_IN pl pt_BR pt_PT ru sk sl sv_SE tr uk zh_CN

# Disabled l10n languages, for any reason
%define disabled_langlist	%{nil}

# Disabled myspell dicts, for any reason
%define disabled_dict_langlist	eu ja ko mk mn pa_IN tr zh_CN

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
%define language_pa_IN pa-IN
%define langname_pa_IN Punjabi (gurmukhi)
%define language_pl pl
%define langname_pl Polish
%define language_pt_BR pt-BR
%define langname_pt_BR Brazilian portuguese
%define language_pt_PT pt-PT
%define langname_pt_PT Portuguese
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

# Macro for easy adding i18n sources
# auto-increment as called.
%define src 1

%define l10nsrc() Source%src: %{xpidir}/%{1}.xpi\
%define src2 %(echo $((%src+1)))\
%define src %{src2}

Summary: Localizations for Sunbird (virtual package)
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/WWW
Url: http://www.mozilla.org/
# Language package template
Source0: %{name}-template.spec
Patch0: mozilla-sunbird-da-fix-xml.patch
# l10n sources
%{expand:%(\
	for lang in %langlist; do\
		echo "%%{expand:%%l10nsrc %%{language_$lang}}";\
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
		echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %{_sourcedir}/%{name}-template.spec 2> /dev/null)}";\
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
	unzip %{_sourcedir}/${language}.xpi
	cd ..

	# dict
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

	mkdir -p ${language}-dict/dictionaries
	cd ${language}-dict
	if [ -e %{_datadir}/dict/ooo/$lang.aff ]; then
		ln -s %{_datadir}/dict/ooo/$lang.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/$lang.dic ./dictionaries/$language.dic
	elif [ -e %{_datadir}/dict/ooo/$locale.aff ]; then
		ln -s %{_datadir}/dict/ooo/$locale.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/$locale.dic ./dictionaries/$language.dic
	else
		ln -s %{_datadir}/dict/ooo/${locale}_*.aff ./dictionaries/$language.aff
		ln -s %{_datadir}/dict/ooo/${locale}_*.dic ./dictionaries/$language.dic
	fi
	cd ..
done

cd da
%patch0 -p0
cd -

cd it
%patch0 -p0
cd -

%build
# All install.rdf files must validate
xmllint --noout */install.rdf

%install
rm -rf %buildroot

# Convert rpm macros to bash variables
%{expand:%(for lang in %langlist; do echo "language_$lang=%%{language_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "with_$lang=%%{with_$lang}"; done)}
%{expand:%(for lang in %langlist; do echo "dict_$lang=%%{with_dict_$lang}"; done)}

# Create dicts dir
%if %use_dict
mkdir -p %buildroot%{mozillalibdir}/dictionaries
%endif

# Install all languages
for lang in %langlist; do
	with="with_$lang"
	with=${!with}
	[ $with -eq 0 ] && continue

	language="language_$lang"
	language=${!language}

	# l10n
	cd $language
	mkdir -p %buildroot%{mozillalibdir}/extensions/langpack-${language}@sunbird.mozilla.org/
	cp -f -r * %buildroot%{mozillalibdir}/extensions/langpack-${language}@sunbird.mozilla.org/
	cd ..

	# Dicts
	dict="dict_$lang"
	dict=${!dict}
	[ $dict -eq 0 ] && continue

	cp -af $language-dict/dictionaries/*.{aff,dic} \
		%buildroot%{mozillalibdir}/dictionaries/
done

%clean
rm -rf %buildroot

