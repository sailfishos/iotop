Name:       iotop

Summary:    Simple top-like I/O monitor
Version:    0.4.3
Release:    1
Group:      System/Console
License:    GPLv2+
BuildArch:  noarch
URL:        http://guichaz.free.fr/iotop/
Source0:    http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRequires:  python

%description
Iotop does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".


%package doc
Summary:    Documentation for simple top-like I/O monitor
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./setup.py build

%install
rm -rf %{buildroot}
./setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/iotop
%{python_sitelib}/iotop-*
%{python_sitelib}/iotop/*
%{_mandir}/man*/*

%files doc
%defattr(-,root,root,-)
%doc COPYING NEWS README THANKS
