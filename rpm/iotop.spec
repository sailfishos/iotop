Name:       iotop

Summary:    Simple top-like I/O monitor
Version:    0.6.0
Release:    1
License:    GPLv2+
BuildArch:  noarch
URL:        http://guichaz.free.fr/iotop/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
Requires:   python3-curses

%description
Iotop does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".


%package doc
Summary:    Documentation for simple top-like I/O monitor
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%py3_build

%install
%py3_install

%files
%defattr(-,root,root,-)
%license COPYING
%{_sbindir}/iotop
%{python3_sitelib}/iotop-*
%{python3_sitelib}/iotop/*

%files doc
%defattr(-,root,root,-)
%doc NEWS README THANKS
%{_mandir}/man*/*
