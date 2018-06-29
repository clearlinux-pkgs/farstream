#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1D388E5A4ED9A2BB (tester@tester.ca)
#
Name     : farstream
Version  : 0.2.8
Release  : 4
URL      : https://freedesktop.org/software/farstream/releases/farstream/farstream-0.2.8.tar.gz
Source0  : https://freedesktop.org/software/farstream/releases/farstream/farstream-0.2.8.tar.gz
Source99 : https://freedesktop.org/software/farstream/releases/farstream/farstream-0.2.8.tar.gz.asc
Summary  : Farstream base classes and utilities
Group    : Development/Tools
License  : LGPL-2.1
Requires: farstream-lib
Requires: farstream-data
Requires: farstream-doc
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(nice)
BuildRequires : valgrind

%description
Farstream
==========
http://www.freedesktop.org/wiki/Software/Farstream
Farstream is a collection of GStreamer modules and libraries for
videoconferencing. The API is described in the documentation in the
docs/ directory.

%package data
Summary: data components for the farstream package.
Group: Data

%description data
data components for the farstream package.


%package dev
Summary: dev components for the farstream package.
Group: Development
Requires: farstream-lib
Requires: farstream-data
Provides: farstream-devel

%description dev
dev components for the farstream package.


%package doc
Summary: doc components for the farstream package.
Group: Documentation

%description doc
doc components for the farstream package.


%package lib
Summary: lib components for the farstream package.
Group: Libraries
Requires: farstream-data

%description lib
lib components for the farstream package.


%prep
%setup -q -n farstream-0.2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511983092
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1511983092
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Farstream-0.2.typelib
/usr/share/farstream/0.2/fsrawconference/default-element-properties
/usr/share/farstream/0.2/fsrtpconference/default-codec-preferences
/usr/share/farstream/0.2/fsrtpconference/default-element-properties
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/farstream-0.2/farstream/fs-candidate.h
/usr/include/farstream-0.2/farstream/fs-codec.h
/usr/include/farstream-0.2/farstream/fs-conference.h
/usr/include/farstream-0.2/farstream/fs-element-added-notifier.h
/usr/include/farstream-0.2/farstream/fs-enumtypes.h
/usr/include/farstream-0.2/farstream/fs-participant.h
/usr/include/farstream-0.2/farstream/fs-plugin.h
/usr/include/farstream-0.2/farstream/fs-rtp.h
/usr/include/farstream-0.2/farstream/fs-session.h
/usr/include/farstream-0.2/farstream/fs-stream-transmitter.h
/usr/include/farstream-0.2/farstream/fs-stream.h
/usr/include/farstream-0.2/farstream/fs-transmitter.h
/usr/include/farstream-0.2/farstream/fs-utils.h
/usr/lib64/libfarstream-0.2.so
/usr/lib64/pkgconfig/farstream-0.2.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/farstream-libs-0.2/FsConference.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsElementAddedNotifier.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsParticipant.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsSession.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsStream.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsStreamTransmitter.html
/usr/share/gtk-doc/html/farstream-libs-0.2/FsTransmitter.html
/usr/share/gtk-doc/html/farstream-libs-0.2/ch01.html
/usr/share/gtk-doc/html/farstream-libs-0.2/ch02.html
/usr/share/gtk-doc/html/farstream-libs-0.2/ch03.html
/usr/share/gtk-doc/html/farstream-libs-0.2/ch04.html
/usr/share/gtk-doc/html/farstream-libs-0.2/ch05.html
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-0.2.devhelp2
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsCandidate.html
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsCodec.html
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsPlugin.html
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-RTP-Specific-types.html
/usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-Utility-functions.html
/usr/share/gtk-doc/html/farstream-libs-0.2/home.png
/usr/share/gtk-doc/html/farstream-libs-0.2/index.html
/usr/share/gtk-doc/html/farstream-libs-0.2/index.sgml
/usr/share/gtk-doc/html/farstream-libs-0.2/left-insensitive.png
/usr/share/gtk-doc/html/farstream-libs-0.2/left.png
/usr/share/gtk-doc/html/farstream-libs-0.2/pt01.html
/usr/share/gtk-doc/html/farstream-libs-0.2/pt02.html
/usr/share/gtk-doc/html/farstream-libs-0.2/right-insensitive.png
/usr/share/gtk-doc/html/farstream-libs-0.2/right.png
/usr/share/gtk-doc/html/farstream-libs-0.2/style.css
/usr/share/gtk-doc/html/farstream-libs-0.2/up-insensitive.png
/usr/share/gtk-doc/html/farstream-libs-0.2/up.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsMsnCamSendConference.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsMsnConference.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsMsnParticipant.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRTPXdataDepay.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRTPXdataPay.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRawConference.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpConference.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpParticipant.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpSession.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpStream.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/FsVideoanyrate.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/ch01.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/ch02.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/ch03.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-0.2.devhelp2
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsMsnCamCamRecvConference.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsMsnSession.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsMsnStream.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsMulticastStreamTransmitter.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsNiceStreamTransmitter.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawParticipant.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawSession.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawStream.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawUdpStreamTransmitter.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsShmStreamTransmitter.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/home.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/index.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/index.sgml
/usr/share/gtk-doc/html/farstream-plugins-0.2/left-insensitive.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/left.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/pt01.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/pt02.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/pt03.html
/usr/share/gtk-doc/html/farstream-plugins-0.2/right-insensitive.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/right.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/style.css
/usr/share/gtk-doc/html/farstream-plugins-0.2/up-insensitive.png
/usr/share/gtk-doc/html/farstream-plugins-0.2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/farstream-0.2/libmulticast-transmitter.so
/usr/lib64/farstream-0.2/libnice-transmitter.so
/usr/lib64/farstream-0.2/librawudp-transmitter.so
/usr/lib64/farstream-0.2/libshm-transmitter.so
/usr/lib64/gstreamer-1.0/libfsmsnconference.so
/usr/lib64/gstreamer-1.0/libfsrawconference.so
/usr/lib64/gstreamer-1.0/libfsrtpconference.so
/usr/lib64/gstreamer-1.0/libfsrtpxdata.so
/usr/lib64/gstreamer-1.0/libfsvideoanyrate.so
/usr/lib64/libfarstream-0.2.so.5
/usr/lib64/libfarstream-0.2.so.5.1.0
