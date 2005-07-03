%define		module	pydev
%define		_ver	0.9.5
%define		_src_ver	%(echo %{_ver}|tr . _)
Summary:	Python development environment for Eclipse
Summary(pl):	¦rodowisko programistyczne Pythona dla Eclipse
Name:		eclipse-%{module}
Version:	%{_ver}
Release:	0.3
License:	CPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/pydev/%{module}_%{_src_ver}.zip
# Source0-md5:	b5bac4248f33ada1d8dc05db4f06a3b2
URL:		http://pydev.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
Requires:	eclipse < 3.1-1
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_eclipsedir	%{_datadir}/eclipse

%description
PyDev is a plugin for Eclipse for editing, running and debugging 
Python scripts.

%description -l pl
PyDev jest wtyczk± dla Eclipse s³u¿±c± do edycji, uruchamiania
i odpluskwiania skryptów Pythona.

%prep
%setup -q -c -T
unzip -qq %{SOURCE0} -x *.db

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/eclipse/{features,plugins}
cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_libdir}/eclipse/features
cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_libdir}/eclipse/plugins

# on future
#install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}
#cp -rf eclipse/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
#cp -rf eclipse/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/eclipse/features/org.python.pydev*
%{_libdir}/eclipse/plugins/org.python.pydev*
# on future
#%{_eclipsedir}/features/org.python.pydev*
#%{_eclipsedir}/plugins/org.python.pydev*

%triggerpostun -- %{name} > 0.9.5-0.3
%banner %{name} -e << EOF
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!                                                                !!!
!!! WARNING!!!                                                     !!!
!!!                                                                !!!
!!! An user manual intervention is required after eclipse-pydev    !!!
!!! instalation. To get this plugin working you have to add        !!!
!!! /usr/share/eclipse directory as Extension Location. Click      !!!
!!! from eclipse menu Help->Software Updates->Manage Configuration !!!
!!! ->Add an Extension Location and choose /usr/share/eclipse .    !!!
!!!                                                                !!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EOF
