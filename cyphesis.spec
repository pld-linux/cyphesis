#
#
Summary:	A simple personal server for the WorldForge project
Name:		cyphesis
Version:	0.5.6
Release:	0.1
License:	GPL
Group:		Games
URL:		http://www.worldforge.org/dev/eng/servers/cyphesis
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	cyclient.init
Source3:	%{name}.sysconfig
BuildRequires:	Atlas-C++-devel >= 0.6.0
BuildRequires:	mercator-devel >= 0.2.0
BuildRequires:	varconf-devel >= 0.6.2
BuildRequires:	skstream-devel >= 0.3.2
BuildRequires:	readline-devel
BuildRequires:	postgresql-devel >= 7.1
BuildRequires:	openssl-devel
BuildRequires:	python-devel >= 2.0.0
BuildRequires:	howl-devel
# from configure
BuildRequires:	libgcrypt-devel >= 1.2.0
Requires:	initscripts /usr/sbin/useradd /sbin/chkconfig
Requires:	postgresql-server
Obsoletes:	cyphesis-service 
Obsoletes:	cyphesis-mason
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cyphesis is a very simple world simulator. NPCs that do things according to
rules. They have minds with simple input and output. They can
use/move/make things and have simple discussion. They can deduce
simple things (like where I can get these things and where I should
be). They have simple memory and use it too. They can have goals (like
build home for me or go to dinner).
This package includes the rules data, scripts and map data required for the
Mason game. Use this package if you intend to run an Mason server.

#%package acorn
#Summary: Game data for running the Acorn game in cyphesis
#Group: Amusements/Games
#Requires: %{name} = %{version}

#%description acorn
#This is the rules data, scripts and map data required for the Acorn
#game. Install this package if you intend to run an Acorn server.
#Acorn is deprecated. See README for details.

#%package werewolf
#Summary: Game data for running the Werewolf game in cyphesis
#Group: Amusements/Games
#Requires: %{name} = %{version} %{name}-acorn

#%description werewolf
#This is the rules data, scripts and map data required for the Werewolf
#game. Install this package if you intend to run an Werewolf server.
#Werewolf is not yet functional.

%prep
%setup -q

%build
%configure \
	--enable-static 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#if [ -d /etc/rc.d/init.d ]
#then
#        install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
#        install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/cyphesis
#        install -m 755 %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/cyclient
#        echo /etc/rc.d/init.d/cyphesis >> service.lst
#        echo /etc/rc.d/init.d/cyclient >> service.lst
#fi
#if [ -d /etc/sysconfig ]
#then
#        install -d $RPM_BUILD_ROOT/etc/sysconfig
#        install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/cyphesis
#        echo %config\(noreplace\) /etc/sysconfig/cyphesis >> service.lst
#fi

#%pre
#useradd -M -n -r -s /bin/bash -c "Cyphesis user" cyphesis >/dev/null 2>&1 || :

#%post
#chkconfig --add cyphesis
#chkconfig --add cyclient

# If we obsolete cyphesis-service, then it will delete its service entries
# and account after our %pre and %post have run. We need to ensure they
# are re-added.
#%triggerpostun -- cyphesis-service
#useradd -M -n -r -s /bin/bash -c "Cyphesis user" cyphesis >/dev/null 2>&1 || :
#chkconfig --add cyphesis
#chkconfig --add cyclient

#%preun
#if [ $1 = 0 ] ; then
#        chkconfig --del cyphesis
#        chkconfig --del cyclient
#fi

#%postun
#if [ $1 -ge 1 ]; then
#        %service cyphesis condrestart >/dev/null 2>&1
#fi
#if [ $1 = 0 ] ; then
#        userdel cyphesis >/dev/null 2>&1 || :
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f service.lst
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/cyphesis/cyphesis.vconf
%config %{_sysconfdir}/cyphesis/basic.xml
%config %{_sysconfdir}/cyphesis/acorn.xml
%config %{_sysconfdir}/cyphesis/mason.xml
%config %{_sysconfdir}/cyphesis/werewolf.xml
%attr(755,root,root) %{_bindir}/cy*
%{_datadir}/cyphesis/rulesets/basic
%{_datadir}/cyphesis/rulesets/mason
%{_mandir}/man1/*.1*
%doc README COPYING AUTHORS THANKS NEWS

#%files acorn
#%defattr(-,root,root)
#%config %{_sysconfdir}/cyphesis/acorn.xml
#%{_datadir}/cyphesis/rulesets/acorn

#%files werewolf
#%defattr(-,root,root)
#%config %{_sysconfdir}/cyphesis/werewolf.xml
#%{_datadir}/cyphesis/rulesets/werewolf
