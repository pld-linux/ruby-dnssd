%define tarname dnssd
%define tarversion 0_6_0
Summary:	DNS Service Discovery module for Ruby
Summary(pl.UTF-8):	Moduł DNS Service Discovery dla języka Ruby
Name:		ruby-dnssd
Version:	0.6.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1656/%{tarname}-%{tarversion}.tar.gz
# Source0-md5:	6615f4a34246ab020382f507295de46d
Patch0:		%{name}-libname.patch
URL:		http://dnssd.rubyforge.org/
BuildRequires:	mdns-bonjour-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.3.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DNS Service Discovery module for Ruby - a binding to the DNS Service
Discovery (Rendezvous) API.

%description -l pl.UTF-8
Moduł DNS Service Discovery (wyszukiwania usługi DNS) dla języka Ruby
- dowiązanie do API DNS Service Discovery (znanego też jako
Rendezvous).

%prep
%setup -q -n %{tarname}-%{tarversion}
cp %{_datadir}/setup.rb .
%patch0 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_archdir}/*
%{ruby_rubylibdir}/dnssd*
