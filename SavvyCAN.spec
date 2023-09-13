%global gittag V%{version}

Name:           SavvyCAN
Version:        213
Release:        1%{?dist}
Summary:        Qt based cross platform canbus tool

License:        MIT
URL:            https://www.savvycan.com/
Source0:        https://github.com/collin80/SavvyCAN/archive/%{gittag}/%{name}-%{version}.tar.gz

# qmake-qt5
BuildRequires:  qt5-qtbase-devel
# module: qml
BuildRequires:  qt5-qtdeclarative-devel
# module: serialbus
BuildRequires:  qt5-qtserialbus-devel
# module: serialport
BuildRequires:  qt5-qtserialport-devel
# module: help
BuildRequires:  qt5-qttools-devel


%description
A Qt5 based cross platform tool which can be used to load, save, and capture
canbus frames.
This tool is designed to help with visualization, reverse engineering,
debugging, and capturing of canbus frames.


%prep
%autosetup


%build
export QTDIR="%{_qt5_prefix}"
export PATH="%{_qt5_bindir}:$PATH"

%qmake_qt5 PREFIX=%{buildroot}/%{_prefix}
%make_build


%install
make install
  

%files
%{_bindir}/SavvyCAN
%{_datadir}/applications/SavvyCAN.desktop
%license LICENSE
%doc README.md

# examples
%exclude %{_datadir}/savvycan/examples/examples/BusMasterLog.log
%exclude %{_datadir}/savvycan/examples/examples/CRTD_Log.txt
%exclude %{_datadir}/savvycan/examples/examples/CaptureAllMsgTypes.js
%exclude %{_datadir}/savvycan/examples/examples/CarBusAnalyzer.trc
%exclude %{_datadir}/savvycan/examples/examples/GVRET_Log.csv
%exclude %{_datadir}/savvycan/examples/examples/GenericID_Log.csv
%exclude %{_datadir}/savvycan/examples/examples/GetCANandTick.js
%exclude %{_datadir}/savvycan/examples/examples/LeafPowertrainBus.dbc
%exclude %{_datadir}/savvycan/examples/examples/MicrochipLog.log
%exclude %{_datadir}/savvycan/examples/examples/RLEC.js
%exclude %{_datadir}/savvycan/examples/examples/ThinkCity.dbc
%exclude %{_datadir}/savvycan/examples/examples/UpdateParameter.js
%exclude %{_datadir}/savvycan/examples/examples/bms.dbc
%exclude %{_datadir}/savvycan/examples/examples/candump.log

# icons
%{_datadir}/icons/icons/SavvyIcon.icns
%{_datadir}/icons/icons/SavvyIcon.png
%{_datadir}/icons/icons/hicolor/256x256/apps/SavvyCAN.png
%{_datadir}/icons/icons/hicolor/scalable/apps/SavvyCAN.png

# helpfiles
%exclude %{_bindir}/help/bisector.md
%exclude %{_bindir}/help/canbridge.md
%exclude %{_bindir}/help/connectionwindow.md
%exclude %{_bindir}/help/customsender.md
%exclude %{_bindir}/help/dbc_editor.md
%exclude %{_bindir}/help/dbc_manager.md
%exclude %{_bindir}/help/filecomparison.md
%exclude %{_bindir}/help/flowview.md
%exclude %{_bindir}/help/framedetails.md
%exclude %{_bindir}/help/fuzzingwindow.md
%exclude %{_bindir}/help/graphsetup.md
%exclude %{_bindir}/help/graphwindow.md
%exclude %{_bindir}/help/images/Bisector.png
%exclude %{_bindir}/help/images/CANBridge.png
%exclude %{_bindir}/help/images/ConnectionWindow.png
%exclude %{_bindir}/help/images/CustomSender.png
%exclude %{_bindir}/help/images/DBCEditor.png
%exclude %{_bindir}/help/images/DBCManager.png
%exclude %{_bindir}/help/images/DBCMessageEditor.png
%exclude %{_bindir}/help/images/FileComparator.png
%exclude %{_bindir}/help/images/FlowView.png
%exclude %{_bindir}/help/images/FrameInfoWindow.png
%exclude %{_bindir}/help/images/FuzzingWindow.png
%exclude %{_bindir}/help/images/GraphSetup.png
%exclude %{_bindir}/help/images/GraphingView.png
%exclude %{_bindir}/help/images/ISOTPDecoder.png
%exclude %{_bindir}/help/images/MainScreen.png
%exclude %{_bindir}/help/images/NewConnection.png
%exclude %{_bindir}/help/images/Playback.png
%exclude %{_bindir}/help/images/Preferences.png
%exclude %{_bindir}/help/images/RangeState.png
%exclude %{_bindir}/help/images/ScriptingWindow.png
%exclude %{_bindir}/help/images/SignalEditor.png
%exclude %{_bindir}/help/images/Sniffer.png
%exclude %{_bindir}/help/images/TemporalWindow.png
%exclude %{_bindir}/help/images/UDS_Scanner.png
%exclude %{_bindir}/help/isotp_decoder.md
%exclude %{_bindir}/help/mainscreen.md
%exclude %{_bindir}/help/newconnection.md
%exclude %{_bindir}/help/playbackwindow.md
%exclude %{_bindir}/help/preferences.md
%exclude %{_bindir}/help/rangestate.md
%exclude %{_bindir}/help/scriptingwindow.md
%exclude %{_bindir}/help/signaleditor.md
%exclude %{_bindir}/help/sniffer.md
%exclude %{_bindir}/help/temporalwindow.md
%exclude %{_bindir}/help/uds_scanner.md


%changelog
* Wed Sep 13 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial package

