%if 0%{?rhel} < 6
%define python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; import sys; sys.stdout.write(get_python_lib())")
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; import sys; sys.stdout.write(get_python_lib(1))")
%define python_version  %(%{__python} -c "import sys; sys.stdout.write(sys.version[:3])")
%endif

Summary:       Fixed size round-robin style database
Name:          whisper
Version:       0.9.10
Release:       2%{?dist}
Source:        https://launchpad.net/graphite/0.9/%{version}/%{name}-%{version}.tar.gz
License:       Apache Software License 2.0
Group:         Development/Libraries
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:        %{_prefix}
BuildArch:     noarch
URL:           https://launchpad.net/graphite
BuildRequires: python(abi) >= 2.6
Requires:      python(abi) >= 2.6
Provides:      python(whisper) = %{version}
Obsoletes:     python-whisper


%description
Fixed size round-robin style database


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} -O1

install -d -m 0755 %{buildroot}%{_sharedstatedir}/graphite/storage/whisper


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/rrd2whisper.py
%{_bindir}/whisper*.py
%{python_sitelib}/%{name}-%{version}-py%{pyver}.egg-info
%{python_sitelib}/%{name}.py
%{python_sitelib}/%{name}.pyc
%{python_sitelib}/%{name}.pyo
%attr(0755,graphite,graphite) %{_sharedstatedir}/graphite/

%changelog
* Fri Aug 24 2012 Jason Antman <jason@jasonantman.com> - 0.9.10-2
- Fix issue with missing .pyo files on Cent6.2

* Tue Jul 10 2012 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.10-1
- Update to version 0.9.10

* Sun Nov  6 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.9-2
- Rename python-whisper to whisper

* Wed Oct 26 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.9-1
- Bump to version 0.9.9

* Wed Oct 26 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.7-1
- Initial package
