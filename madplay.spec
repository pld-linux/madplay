#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	MPEG audio decoder and player
Summary(pl):	Dekoder i odtwarzacz audio w formacie MPEG
Name:		madplay
Version:	0.15.1b
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
# Source0-md5:	49f31fe08af0be7bf29d9d11a13abecc
URL:		http://www.underbit.com/products/mad/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
BuildRequires:	automake
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
cp -f /usr/share/automake/config.* .
%{?with_alsa:CPPFLAGS="-DALSA_PCM_OLD_HW_PARAMS_API"}
%configure \
	%{?with_alsa:--with-alsa}

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
