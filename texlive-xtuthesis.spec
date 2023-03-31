Name:		texlive-xtuthesis
Version:	47049
Release:	2
Summary:	XTU thesis template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xtuthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtuthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xtuthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a thesis template for the Xiangtan
University.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xtuthesis
%doc %{_texmfdistdir}/doc/latex/xtuthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
