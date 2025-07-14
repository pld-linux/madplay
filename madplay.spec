#
# Conditional build:
%bcond_without	alsa	# without ALSA support
%bcond_without	esd	# without esd support
#
Summary:	MPEG audio decoder and player
Summary(pl.UTF-8):	Dekoder i odtwarzacz audio w formacie MPEG
Name:		madplay
Version:	0.15.2b
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	6814b47ceaa99880c754c5195aa1aac1
Patch0:		%{name}-locale_names.patch
URL:		http://www.underbit.com/products/mad/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	libmad-devel
BuildRequires:	libid3tag-devel
Obsoletes:	mad
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Madplay is a command-line MPEG audio decoder and player based on the
MAD library (libmad). For details about MAD, see the libmad package
distributed separately.

%description -l pl.UTF-8
Madplay to działający w oparciu o wiersz poleceń odtwarzacz plików
MPEG audio (m.in. MP3). Jest on oparty na bibliotece dekodującej MAD
(libmad).

%prep
%setup -q
%patch -P0 -p1

mv -f po/{no,nb}.po

%build
cp -f /usr/share/automake/config.* .
%configure \
	%{?with_alsa:--with-alsa} \
	%{!?with_esd:--without-esd}

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
