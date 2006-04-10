Summary:	A simple personal server for the WorldForge project
Summary(pl):	Prosty osobisty serwer dla projektu WorldForge
Name:		cyphesis
Version:	0.5.6
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	cyclient.init
Source3:	%{name}.sysconfig
URL:		http://www.worldforge.org/dev/eng/servers/cyphesis
BuildRequires:	Atlas-C++-devel >= 0.6.0
BuildRequires:	howl-devel
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	mercator-devel >= 0.2.0
BuildRequires:	openssl-devel
BuildRequires:	postgresql-devel >= 7.1
BuildRequires:	python-devel >= 2.0.0
BuildRequires:	readline-devel
BuildRequires:	skstream-devel >= 0.3.2
BuildRequires:	varconf-devel >= 0.6.2
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:	cyphesis-service 
Obsoletes:	cyphesis-mason
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cyphesis is a very simple world simulator. NPCs that do things
according to rules. They have minds with simple input and output. They
can use/move/make things and have simple discussion. They can deduce
simple things (like where I can get these things and where I should
be). They have simple memory and use it too. They can have goals (like
build home for me or go to dinner).

This package includes the rules data, scripts and map data required for the
Mason game. Use this package if you intend to run an Mason server.

%description -l pl
Cyphesis to bardzo prosty symulator ¶wiata. NPC wykonuj±ce swoje
czynno¶ci zgodnie z regu³ami. Maj± mózgi z prostym wej¶ciem i
wyj¶ciem. Mog± u¿ywaæ/przenosiæ/robiæ rzeczy i prowadziæ proste
dyskusje. Mog± wydedukowaæ proste rzeczy (np. sk±d pozyskaæ dane
przedmioty i gdzie powinny byæ). Maj± prost± pamiêæ i jej u¿ywaj±.
Mog± mieæ swoje cele (np. zbudowaæ dom lub pój¶æ na obiad).

Ten pakiet zawiera dane regu³, skrypty i dane map wymagane przez grê
Mason. Nale¿y u¿yæ tego pakietu przy uruchamianiu serwera Masona.

#%package acorn
#Summary:	Game data for running the Acorn game in Cyphesis
#Summary(pl):	Dane gry do uruchamiania gry Acorn w Cyphesis
#Group:		Applications/Games
#Requires:	%{name} = %{version}-%{release}

#%description acorn
#This is the rules data, scripts and map data required for the Acorn
#game. Install this package if you intend to run an Acorn server.
#Acorn is deprecated. See README for details.

#%description acorn -l pl
#Ten pakiet zawiera dane regu³, skrypty i dane map wymagane przez grê
#Acorn. Nale¿y u¿yæ tego pakietu przy uruchamianiu serwera Acorna.
#Acorn jest przestarza³y. Szczegó³y w pliku README.

#%package werewolf
#Summary:	Game data for running the Werewolf game in Cyphesis
#Summary(pl):	Dane gry do uruchamiania gry Werewolf w Cyphesis
#Group:		Applications/Games
#Requires:	%{name}-acorn = %{version}-%{release}

#%description werewolf
#This is the rules data, scripts and map data required for the Werewolf
#game. Install this package if you intend to run an Werewolf server.
#Werewolf is not yet functional.

#%description werewolf
#Ten pakiet zawiera dane regu³, skrypty i dane map wymagane przez grê
#Werewolf. Nale¿y u¿yæ tego pakietu przy uruchamianiu serwera
#Werewolfa. Werewolf jeszcze nie dzia³a.

%prep
%setup -q

%build
%configure

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
%doc README COPYING AUTHORS THANKS NEWS
%dir %{_sysconfdir}/cyphesis
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyphesis/cyphesis.vconf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyphesis/basic.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyphesis/acorn.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyphesis/mason.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cyphesis/werewolf.xml
%attr(755,root,root) %{_bindir}/cy*
%dir %{_datadir}/cyphesis
%dir %{_datadir}/cyphesis/rulesets
%{_datadir}/cyphesis/rulesets/basic
%{_datadir}/cyphesis/rulesets/mason
%{_mandir}/man1/*.1*

#%files acorn
#%defattr(-,root,root)
#%config %{_sysconfdir}/cyphesis/acorn.xml
#%{_datadir}/cyphesis/rulesets/acorn

#%files werewolf
#%defattr(-,root,root)
#%config %{_sysconfdir}/cyphesis/werewolf.xml
#%{_datadir}/cyphesis/rulesets/werewolf
