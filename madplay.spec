#
# Conditional build:
# _without_alsa	- without ALSA support
#
Summary:	MPEG audio decoder and player
Summary(pl):	Dekoder i odtwarzacz audio w formacie MPEG
Name:		madplay
Version:	0.15.0b
Release:	0.9
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	35762ddeb46fba8bbf0a260b6c425e82
URL:		http://www.underbit.com/products/mad/
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	esound-devel
BuildRequires:	libmad-devel
BuildRequires:	libid3tag-devel
Obsoletes:	mad
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Madplay is a command-line MPEG audio decoder and player based on the
MAD library (libmad). For details about MAD, see the libmad package
distributed separately.

%description -l pl
Madplay to dzia³aj±cy w oparciu o wiersz poleceñ odtwarzacz plików
MPEG audio (m.in. mp3). Jest on oparty na bibliotece dekoduj±cej MAD
(libmad).

%prep
%setup -q

%build
%configure \
	%{!?_without_alsa:--with-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README CREDITS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
