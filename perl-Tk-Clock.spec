%define upstream_name    Tk-Clock
%define upstream_version 0.28

%define _requires_exceptions /pro/bin/perl

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Canvas based Clock widget
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl(Carp)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::Canvas)
BuildRequires: perl(Tk::Derived)
BuildRequires: perl(Tk::Widget)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*
