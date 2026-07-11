%global tl_name msc
%global tl_revision 67718

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.00
Release:	%{tl_revision}.1
Summary:	Draw MSC diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/msc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package should be useful to all people that prepare their texts with
LaTeX and want to draw Message Sequence Charts in their texts. The
package is not an MSC editor; it simply takes a textual description of
an MSC and draws the corresponding MSC. The current version of the MSC
macro package supports the full MSC2000 language.

