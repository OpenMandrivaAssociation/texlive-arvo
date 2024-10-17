Name:		texlive-arvo
Version:	57213
Release:	2
Summary:	The Arvo font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arvo
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arvo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arvo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Arvo family of fonts designed by
Anton Koovit, with support for LaTeX and pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/arvo
%{_texmfdistdir}/fonts/vf/public/arvo
%{_texmfdistdir}/fonts/truetype/public/arvo
%{_texmfdistdir}/fonts/tfm/public/arvo
%{_texmfdistdir}/fonts/map/dvips/arvo
%{_texmfdistdir}/fonts/enc/dvips/arvo
%doc %{_texmfdistdir}/doc/fonts/arvo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
