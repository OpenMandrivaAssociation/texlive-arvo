%global tl_name arvo
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	The Arvo font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/arvo
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arvo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arvo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Arvo family of fonts designed by Anton Koovit,
with support for LaTeX and pdfLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/arvo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/arvo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/arvo
%dir %{_datadir}/texmf-dist/fonts/map/dvips/arvo
%dir %{_datadir}/texmf-dist/fonts/tfm/public/arvo
%dir %{_datadir}/texmf-dist/fonts/truetype/public/arvo
%dir %{_datadir}/texmf-dist/fonts/vf/public/arvo
%doc %{_datadir}/texmf-dist/doc/fonts/arvo/LICENSE.TXT
%doc %{_datadir}/texmf-dist/doc/fonts/arvo/README
%doc %{_datadir}/texmf-dist/doc/fonts/arvo/arvo-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/arvo/arvo-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_6czsg4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_fibvii.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_fin2th.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_jtfq37.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_od575u.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_vt66fp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/arvo/a_zmrji7.enc
%{_datadir}/texmf-dist/fonts/map/dvips/arvo/Arvo.map
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-BoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/arvo/Arvo-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/truetype/public/arvo/Arvo-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/arvo/Arvo-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/arvo/Arvo-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/arvo/Arvo-Regular.ttf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Bold-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-BoldItalic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-BoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-BoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Italic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/arvo/Arvo-tlf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/arvo/Arvo.sty
%{_datadir}/texmf-dist/tex/latex/arvo/LY1Arvo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arvo/OT1Arvo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arvo/T1Arvo-TLF.fd
%{_datadir}/texmf-dist/tex/latex/arvo/TS1Arvo-TLF.fd
