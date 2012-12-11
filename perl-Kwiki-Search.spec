%define upstream_name	 Kwiki-Search
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Kwiki Search Plugin
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
Enables a plain text search button for searching the content of the pages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 403385
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.12-6mdv2009.0
+ Revision: 257503
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.12-5mdv2009.0
+ Revision: 245611
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.12-3mdv2008.1
+ Revision: 122830
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdk
- better sources URL
- better buildrequires syntax

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk 
- first mandriva release

