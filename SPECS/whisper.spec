Summary:       Fixed size round-robin style database
Name:          whisper
Version:       0.9.9
Release:       2%{?dist}
Source:        https://launchpad.net/graphite/0.9/%{version}/%{name}-%{version}.tar.gz
License:       Apache Software License 2.0
Group:         Development/Libraries
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix:        %{_prefix}
BuildArch:     noarch
Vendor:        Chris Davis <chrismd@gmail.com>
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT

install -d -m 0755 $RPM_BUILD_ROOT%{_localstatedir}/lib/graphite/storage/whisper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/rrd2whisper.py
%{_bindir}/whisper-create.py
%{_bindir}/whisper-fetch.py
%{_bindir}/whisper-info.py
%{_bindir}/whisper-resize.py
%{_bindir}/whisper-set-aggregation-method.py
%{_bindir}/whisper-update.py
%{python_sitelib}/%{name}-%{version}-py%{pyver}.egg-info
%{python_sitelib}/%{name}.py
%{python_sitelib}/%{name}.pyc
%{python_sitelib}/%{name}.pyo
%attr(0755,graphite,graphite) %dir %{_localstatedir}/lib/graphite
%attr(0755,graphite,graphite) %dir %{_localstatedir}/lib/graphite/storage
%attr(0755,graphite,graphite) %dir %{_localstatedir}/lib/graphite/storage/whisper

%changelog
* Sun Nov  6 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.9-2
- Rename python-whisper to whisper

* Wed Oct 26 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.9-1
- Bump to version 0.9.9

* Wed Oct 26 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.7-1
- Initial package
