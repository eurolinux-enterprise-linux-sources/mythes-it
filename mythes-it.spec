Name: mythes-it
Summary: Italian thesaurus
Version: 2.0.9l
Release: 10%{?dist}
Source: http://downloads.sourceforge.net/sourceforge/linguistico/thesaurus2_it_02_09_l_2008_11_29.zip
Group: Applications/Text
URL: http://linguistico.sourceforge.net/pages/thesaurus_italiano.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: AGPLv3
BuildArch: noarch
Requires: mythes

%description
Italian thesaurus.

%prep
%setup -q -c

%build
for i in th_it_IT_README th_it_IT_ChangeLog th_it_IT_AUTHORS; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_it_IT.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.dat
cp -p th_it_IT.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_it_IT_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s th_it_IT_v2.dat "th_"$lang"_v2.dat"
        ln -s th_it_IT_v2.idx "th_"$lang"_v2.idx"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc th_it_IT_README th_it_IT_ChangeLog th_it_IT_COPYING th_it_IT_INSTALL th_it_IT_copyright_licenza.txt th_it_IT_lettera_in_inglese.txt  th_it_IT_AUTHORS
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.0.9l-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 04 2010 Caolan McNamara <caolanm@redhat.com> - 2.0.9l-5
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Caolan McNamara <caolanm@redhat.com> - 2.0.9l-3
- tidy spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9l-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Caolan McNamara <caolanm@redhat.com> - 2.0.9l-1
- initial version
