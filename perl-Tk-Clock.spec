%define upstream_name    Tk-Clock
%define upstream_version 0.34
%if %{_use_internal_dependency_generator}
%define __noautoreq '/pro/bin/perl'
%else
%define _requires_exceptions /pro/bin/perl
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.34
Release:	1

Summary:	Canvas based Clock widget
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/Tk-Clock-0.34.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Tk)
BuildRequires:	perl(Tk::Canvas)
BuildRequires:	perl(Tk::Derived)
BuildRequires:	perl(Tk::Widget)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
This module implements a Canvas-based clock widget for perl-Tk with lots of
options to change the appearance.

Both analog and digital clocks are implemented.

Options
    Below is a description of the options currently available. Their
    default value is in between parenthesis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# %check
# xvfb-run %make test

%install
%makeinstall_std

%files
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.290.0-2mdv2011.0
+ Revision: 656832
- rebuild for updated spec-helper

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 569959
- update to 0.29

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-2mdv2011.0
+ Revision: 521833
- filter out an automtic extraction, used as shebang on examples

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 521762
- import perl-Tk-Clock


* Tue Mar 16 2010 cpan2dist 0.28-1mdv
- initial mdv release, generated with cpan2dist


