Name     : ltp
Version  : 20180515
Release  : 20
URL      : https://linux-test-project.github.io/
Source0  : https://github.com/linux-test-project/ltp/releases/download/20180515/ltp-full-20180515.tar.xz
Summary  : Test tool for driving IO to block, raw, filesystem targets
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : libcap-dev
BuildRequires : zip
Patch1: 0001-Fix-build-for-cve-2015-3290.c.patch

%define debug_package %{nil}

%description
This package provides the disk testing utility for performing IO testing to
block, raw, and filesystem targets.

Authors:
--------
    Brent Yardley <yardleyb@us.ibm.com>

%prep
%setup -q -n ltp-full-20180515
%patch1 -p1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
chmod 0755 %{buildroot}/usr/bin/*
chmod 0755 %{buildroot}/usr/testcases/bin/*

%files
%defattr(-,root,root,-)
/usr/IDcheck.sh
/usr/Version
/usr/bin/create_dmesg_entries_for_each_test.awk
/usr/bin/create_kernel_faults_in_loops_and_probability.awk
/usr/bin/create_valgrind_check.awk
/usr/bin/execltp
/usr/bin/ffsb
/usr/bin/genhtml.pl
/usr/bin/html_report_header.txt
/usr/bin/insert_kernel_faults.sh
/usr/bin/ltp-bump
/usr/bin/ltp-pan
/usr/bin/make-file.sh
/usr/bin/restore_kernel_faults_default.sh
/usr/runltp
/usr/runltplite.sh
/usr/runtest/*
/usr/scenario_groups/default
/usr/scenario_groups/network
/usr/share/man/man1/doio.1
/usr/share/man/man1/iogen.1
/usr/share/man/man1/ltp-bump.1
/usr/share/man/man1/ltp-pan.1
/usr/share/man/man3/parse_opts.3
/usr/share/man/man3/parse_ranges.3
/usr/share/man/man3/random_range.3
/usr/share/man/man3/random_range_seed.3
/usr/share/man/man3/tst_res.3
/usr/share/man/man3/tst_sig.3
/usr/share/man/man3/tst_tmpdir.3
/usr/share/man/man3/usctest.3
/usr/testcases/bin/*
/usr/testcases/data/*
/usr/testscripts/*
/usr/ver_linux
