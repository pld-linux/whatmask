Summary:	Address format change and calculation utility
Summary(pl):	Narzêdzie do zmiany formatu i przeliczania adresów
Name:		whatmask
Version:	1.1
Release:	2
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.laffeycomputer.com/current_builds/whatmask/%{name}-%{version}.tar.gz
# Source0-md5:	2fa6b1bb18f037d0f9c3c8b2eed19277
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

%description -l pl
whatmask to niewielki program w C pomagaj±cy przy konfiguracji sieci.
Obs³ugiwane notacje to CIDR (np. /24), maska sieci (np. 255.255.255.0)
i maska Wildcatd (np. 0.0.0.255). Te notacje znacz± to samo. Notacja
CIDR zazwyczaj ma "/" przed liczb± (oznaczaj±c± liczbê bitów).
whatmask akceptuje te notacje z lub bez "/". Mo¿e przyj±æ dowolny
adres IP w podsieci wraz z mask± w dowolnym formacie, a wypisze maskê
w trzech formatach, adres sieci, adres broadcastu, liczbê u¿ywalnych
IP oraz zakres IP w podsieci.

%prep
%setup -q

%build
rm -rf missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
