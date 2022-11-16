Name:		texlive-robotarm
Version:	63116
Release:	1
Summary:	TikZ powered LaTeX package to draw parameterized 2D robot arms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/robotarm
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robotarm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package uses TikZ to draw parameterized 2D robot
arms, for example to be used in educational material.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/robotarm
%{_texmfdistdir}/tex/latex/robotarm
%doc %{_texmfdistdir}/doc/latex/robotarm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
