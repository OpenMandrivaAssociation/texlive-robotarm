%global tl_name robotarm
%global tl_revision 63116

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	TikZ powered LaTeX package to draw parameterized 2D robot arms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/robotarm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package uses TikZ to draw parameterized 2D robot arms, for
example to be used in educational material.

