Name:       iotop-c

Summary:    Simple top-like I/O monitor
Version:    1.27
Release:    1
License:    GPLv2+
URL:        https://github.com/sailfishos/iotop/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
Obsoletes:  iotop < %{version}
Provides:   iotop = %{version}

%description
iotop-c does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".

iotop-c requires a Linux kernel built with the CONFIG_TASKSTATS,
CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING and
CONFIG_VM_EVENT_COUNTERS config options on.

iotop-c is an alternative re-implementation of iotop in C, optimized for
performance. Normally a monitoring tool intended to be used on a system
under heavy stress should use the least additional resources as
possible.

%package doc
Summary:    Documentation for simple top-like I/O monitor
Requires:   %{name} = %{version}-%{release}
Obsoletes:  iotop-doc < %{version}
Provides:   iotop-doc = %{version}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%make_build NO_FLTO=1

%install
%make_install

%files
%license COPYING
%license LICENSE
%{_sbindir}/iotop

%files doc
%doc README.md
%{_mandir}/man*/*
