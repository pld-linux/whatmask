Summary:	Address format change and calculation utility
Summary(pl):	Narz�dzie do zmiany formatu i przeliczania adres�w
Name:		whatmask
Version:	1.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	http://www.laffeycomputer.com/current_builds/whatmask/%{name}-%{version}.tar.gz
URL:		http://www.laffeycomputer.com/whatmask.html
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whatmask is a small C program that helps with network settings.
Notations supported are CIDR (e.g. /24), Netmask (e.g. 255.255.255.0),
and Wilcard Bits (e.g. 0.0.0.255). These notations are all identical.
CIDR notation commonly has a "/" in front of the number (representing
the number of bits). Whatmask can accept these notations with or
without a slash. It can take any IP in the subnet along with the
netmask in any format, and it will echo back the netmask in three
formats, the network address, the broadcast address, the number of
useable IPs, and the range of IPs in the subnet.

%prep
%setup -q

%build
rm -rf missing
aclocal
autoconf
automake -a -c
%configure
%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README AUTHORS NEWS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
