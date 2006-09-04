%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Page2
%define		_status		beta
%define		_pearname	HTML_Page2

Summary:	%{_pearname} - base class for XHTML page generation
Summary(pl):	%{_pearname} - klasa bazowa do genrowania dokumentów XHTML
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}beta.tgz
# Source0-md5:	a10646c904fafb3a39ecaf6920f0d174
URL:		http://pear.php.net/package/HTML_Page2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Page2 package provides a simple interface for
generating an XHTML compliant page.
- supports virtually all HTML doctypes, from HTML 2.0 through XHTML
  1.1 and XHTML Basic 1.0 plus preliminary support for XHTML 2.0
- namespace support
- global language declaration for the document
- line ending styles
- full META tag support
- support for stylesheet declaration in the head section
- support for script declaration in the head section
- support for linked stylesheets and scripts
- full support for header link tags
- body can be a string, object with toHtml or toString methods or an
  array (can be combined)

Ideas for use:
- Use to validate the output of a class for XHTML compliance
- Quick prototyping using PEAR packages is now a breeze

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::HTML_Page2 dostarcza prostego interfejsu do generowania
stron zgodnych z XHTML.
- wsparcie dla praktycznie wszystkich typów HTML, od HTML 2.0 przez
  XHTML 1.1 i XHTML Basic 1.0 do podstawowego wsparcia dla XHTML 2.0
- wsparcie dla przestrzeni nazw
- globalna deklaracja jêzyka dokumentu
- pe³ne wsparcie dla znaczników META
- wsparcie dla deklaracji stylu w sekcji head
- wsparcie dla deklaracji skryptów w sekcji head
- wsparcie dla stylów i skryptów osadzonych w innych plikach
- pe³ne wsparcie dla odno¶ników w nag³ówku
- cia³o dokumentu mo¿e byæ ci±giem znaków, obiektem z metodami toHtml
  lub toString lub te¿ tablic±

Klasa mo¿e byæ wykorzystana do:
- sprawdzania poprawno¶ci klasy wzglêdem XHTML

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/{examples/Page2_NoDoctype.php,examples/Page2_Simple.php,examples/Page2_Complex.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/Page2.php
%{php_pear_dir}/HTML/Page2/Doctypes.php
%{php_pear_dir}/HTML/Page2/Namespaces.php
