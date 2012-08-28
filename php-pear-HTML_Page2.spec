%define		status		beta
%define		pearname	HTML_Page2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - base class for XHTML page generation
Summary(pl.UTF-8):	%{pearname} - klasa bazowa do generowania dokumentów XHTML
Name:		php-pear-%{pearname}
Version:	0.6.3
Release:	1
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	e17df6db5cc52d178e8c50b99aee76eb
URL:		http://pear.php.net/package/HTML_Page2/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa PEAR::HTML_Page2 dostarcza prosty interfejs do generowania stron
zgodnych z XHTML.
- wsparcie dla praktycznie wszystkich typów HTML, od HTML 2.0 przez
  XHTML 1.1 i XHTML Basic 1.0 do podstawowego wsparcia dla XHTML 2.0
- wsparcie dla przestrzeni nazw
- globalna deklaracja języka dokumentu
- pełne wsparcie dla znaczników META
- wsparcie dla deklaracji stylu w sekcji head
- wsparcie dla deklaracji skryptów w sekcji head
- wsparcie dla stylów i skryptów osadzonych w innych plikach
- pełne wsparcie dla odnośników w nagłówku
- ciało dokumentu może być ciągiem znaków, obiektem z metodami toHtml
  lub toString lub też tablicą

Klasa może być wykorzystana do:
- sprawdzania poprawności klasy względem XHTML

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv docs/%{pearname}/examples .
mv .%{php_pear_dir}/data/HTML_Page2/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/Page2.php
%dir %{php_pear_dir}/HTML/Page2
%{php_pear_dir}/HTML/Page2/Doctypes.php
%{php_pear_dir}/HTML/Page2/Namespaces.php
%{php_pear_dir}/HTML/Page2/Frameset.php
%dir %{php_pear_dir}/HTML/Page2/Frameset
%{php_pear_dir}/HTML/Page2/Frameset/Frame.php
%{_examplesdir}/%{name}-%{version}
