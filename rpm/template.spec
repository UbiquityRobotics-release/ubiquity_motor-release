Name:           ros-kinetic-ubiquity-motor
Version:        0.5.0
Release:        0%{?dist}
Summary:        ROS ubiquity_motor package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-diff-drive-controller
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-joint-state-controller
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-serial
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-serial
BuildRequires:  ros-kinetic-tf

%description
Provides a ROS interface to Ubiquity Robotics Magni motor controllers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 05 2016 Rohan Agrawal <rohan@aleopile.com> - 0.5.0-0
- Autogenerated by Bloom

