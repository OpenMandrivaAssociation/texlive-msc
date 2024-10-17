Name:		texlive-msc
Version:	67718
Release:	1
Summary:	Draw MSC diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/msc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/msc
%doc %{_texmfdistdir}/doc/latex/msc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
