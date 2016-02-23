%{?scl:%scl_package nodejs-node-uuid}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
%global enable_tests 1

Name:       %{?scl_prefix}nodejs-node-uuid
Version:    1.4.1
Release:    3%{?dist}
Summary:    Simple and fast generation of RFC4122 (v1 and v4) UUIDs for Node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/broofa/node-uuid
Source0:    http://registry.npmjs.org/node-uuid/-/node-uuid-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This Node.js module provides simple and fast generation of RFC4122 (v1 and v4)
UUIDs. It runs in Node.js and all browsers and can also generate
cryptographically strong random numbers.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-uuid
cp -pr package.json uuid.js \
    %{buildroot}%{nodejs_sitelib}/node-uuid

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%{?scl:scl enable %{scl} "}
ln -sf %{nodejs_sitelib} .
%__nodejs test/test.js
%{?scl:"}
%endif

%files
%doc LICENSE.md README.md
%{nodejs_sitelib}/node-uuid

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-3
- rebuilt

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.4.1-2
- replace provides and requires with macro

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.1-1
- update to upstream release 1.4.1

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-5
- add ExclusiveArch logic

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-4
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-3
- add macro to enable dependency generation in EPEL

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-3
- Add support for software collections

* Fri Apr 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-2
- do not include benchmark/ directory

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-1
- initial package
