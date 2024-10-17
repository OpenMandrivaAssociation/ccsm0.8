%define oname ccsm
%define oversion 0.8

%define git 20130330

%if  %{git}
%define srcname %{oname}-compiz-%{oversion}.tar.bz2
%define distname %{oname}-compiz-%{oversion}
%define rel 0.%{git}.1
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define rel 1
%endif

Name:		%{oname}%{oversion}
Version:	0.8.8
Release:	%{rel}
Summary:	Compiz Config Settings Manager
Group:		System/X11
License:	GPL
URL:		https://www.compiz-fusion.org/
Source:		http://cgit.compiz.org/compiz/compizconfig/ccsm/snapshot/%{srcname}
BuildRequires:	compiz0.8-devel
BuildRequires:	python-compizconfig0.8
BuildRequires:	pygtk2.0-devel
BuildRequires:	intltool
BuildRequires:	desktop-file-utils

Requires:	python-compizconfig0.8
Requires:	pygtk2.0
Suggests:	python-sexy
Conflicts:	%{oname} > 0.9

BuildArch:	noarch

%description
Configuration tool for Compiz when used with the ccp configuration
plugin (default).

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
python setup.py build --prefix=%{_prefix}

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

rm -f %{buildroot}%{py_puresitedir}/*.egg-info

%find_lang %{oname}

desktop-file-install \
  --vendor="" \
  --remove-category="Compiz" \
  --add-category="GTK" \
  --add-category="Settings" \
  --add-category="DesktopSettings" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{oname}.desktop

%files -f %{oname}.lang
%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_iconsdir}/hicolor/*/apps/%{oname}.*
%dir %{py_puresitedir}/ccm
%{py_puresitedir}/ccm/*.py

