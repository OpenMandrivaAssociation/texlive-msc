# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/msc
# catalog-date 2008-06-02 14:52:39 +0200
# catalog-license lppl
# catalog-version 1.16
Name:		texlive-msc
Version:	1.16
Release:	1
Summary:	Draw MSC diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/msc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package should be useful to all people that prepare their
texts with LaTeX and want to draw Message Sequence Charts in
their texts. The package is not an MSC editor; it simply takes
a textual description of an MSC and draws the corresponding
MSC. The current version of the MSC macro package supports the
full MSC2000 language.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/msc/biblio.bib
%{_texmfdistdir}/tex/latex/msc/msc.sty
%doc %{_texmfdistdir}/doc/latex/msc/COPYRIGHT.txt
%doc %{_texmfdistdir}/doc/latex/msc/README
%doc %{_texmfdistdir}/doc/latex/msc/maintenance.pdf
%doc %{_texmfdistdir}/doc/latex/msc/maintenance.tex
%doc %{_texmfdistdir}/doc/latex/msc/manual.pdf
%doc %{_texmfdistdir}/doc/latex/msc/manual.tex
%doc %{_texmfdistdir}/doc/latex/msc/refman.pdf
%doc %{_texmfdistdir}/doc/latex/msc/refman.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
