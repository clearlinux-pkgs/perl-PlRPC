#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PlRPC
Version  : 0.2020
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MN/MNOONING/PlRPC/PlRPC-0.2020.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MN/MNOONING/PlRPC/PlRPC-0.2020.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-PlRPC-perl = %{version}-%{release}
Requires: perl(Net::Daemon)
Requires: perl(Storable)
BuildRequires : buildreq-cpan
BuildRequires : perl(Net::Daemon)
BuildRequires : perl(Net::Daemon::Test)

%description
NAME
RPC::PlServer - Perl extension for writing PlRPC servers
SYNOPSIS
# Create a subclass of RPC::PlServer
use RPC::PlServer;

%package dev
Summary: dev components for the perl-PlRPC package.
Group: Development
Provides: perl-PlRPC-devel = %{version}-%{release}
Requires: perl-PlRPC = %{version}-%{release}

%description dev
dev components for the perl-PlRPC package.


%package perl
Summary: perl components for the perl-PlRPC package.
Group: Default
Requires: perl-PlRPC = %{version}-%{release}

%description perl
perl components for the perl-PlRPC package.


%prep
%setup -q -n PlRPC
cd %{_builddir}/PlRPC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Bundle::PlRPC.3
/usr/share/man/man3/RPC::PlClient.3
/usr/share/man/man3/RPC::PlServer.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Bundle/PlRPC.pm
/usr/lib/perl5/vendor_perl/5.30.1/RPC/PlClient.pm
/usr/lib/perl5/vendor_perl/5.30.1/RPC/PlClient/Comm.pm
/usr/lib/perl5/vendor_perl/5.30.1/RPC/PlServer.pm
/usr/lib/perl5/vendor_perl/5.30.1/RPC/PlServer/Comm.pm
/usr/lib/perl5/vendor_perl/5.30.1/RPC/PlServer/Test.pm
