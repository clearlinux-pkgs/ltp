Name     : ltp
Version  : 20150420
Release  : 7
URL      : https://linux-test-project.github.io/
Source0  : http://downloads.sourceforge.net/ltp/ltp-full-20150420.tar.xz
Summary  : Test tool for driving IO to block, raw, filesystem targets
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : libcap-dev
BuildRequires : zip

%define debug_package %{nil}

%description
This package provides the disk testing utility for performing IO testing to
block, raw, and filesystem targets.

Authors:
--------
    Brent Yardley <yardleyb@us.ibm.com>

%prep
%setup -q -n ltp-full-20150420

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/IDcheck.sh
/usr/Version
/usr/bin/STPfailure_report.pl
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
/usr/bin/rand_lines
/usr/bin/restore_kernel_faults_default.sh
/usr/runalltests.sh
/usr/runltp
/usr/runltplite.sh
/usr/runtest/*
/usr/scenario_groups/default
/usr/scenario_groups/network
/usr/share/man/man1/doio.1
/usr/share/man/man1/iogen.1
/usr/share/man/man1/ltp-bump.1
/usr/share/man/man1/ltp-pan.1
/usr/share/man/man3/bytes_by_prefix.3
/usr/share/man/man3/forker.3
/usr/share/man/man3/get_attrib.3
/usr/share/man/man3/parse_open_flags.3
/usr/share/man/man3/parse_opts.3
/usr/share/man/man3/parse_ranges.3
/usr/share/man/man3/pattern.3
/usr/share/man/man3/random_range.3
/usr/share/man/man3/random_range_seed.3
/usr/share/man/man3/rmobj.3
/usr/share/man/man3/string_to_tokens.3
/usr/share/man/man3/tst_res.3
/usr/share/man/man3/tst_set_error.3
/usr/share/man/man3/tst_sig.3
/usr/share/man/man3/tst_tmpdir.3
/usr/share/man/man3/usctest.3
/usr/share/man/man3/write_log.3
/usr/testcases/bin/*
/usr/testcases/data/*
/usr/testscripts/*
/usr/ver_linux
