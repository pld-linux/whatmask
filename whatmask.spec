Summary:	Address format change and calculation utility
Summary(pl.UTF-8):	Narzędzie do zmiany formatu i przeliczania adresów
Name:		whatmask
Version:	1.2
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://downloads.laffeycomputer.com/current_builds/whatmask/%{name}-%{version}.tar.gz
# Source0-md5:	26aeff74dbba70262ccd426e681dcf4a
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

%description -l pl.UTF-8
whatmask to niewielki program w C pomagający przy konfiguracji sieci.
Obsługiwane notacje to CIDR (np. /24), maska sieci (np. 255.255.255.0)
i maska Wildcatd (np. 0.0.0.255). Te notacje znaczą to samo. Notacja
CIDR zazwyczaj ma "/" przed liczbą (oznaczającą liczbę bitów).
whatmask akceptuje te notacje z lub bez "/". Może przyjąć dowolny
adres IP w podsieci wraz z maską w dowolnym formacie, a wypisze maskę
w trzech formatach, adres sieci, adres broadcastu, liczbę używalnych
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
%{_mandir}/man1/*
