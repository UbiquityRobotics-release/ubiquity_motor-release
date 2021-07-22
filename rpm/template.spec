%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ubiquity-motor
Version:        0.13.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ubiquity_motor package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-requests
Requires:       ros-noetic-controller-manager
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-diff-drive-controller
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-joint-state-controller
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Provides a ROS interface to Ubiquity Robotics Magni motor controllers

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Jul 22 2021 Rohan Agrawal <rohan@aleopile.com> - 0.13.1-1
- Autogenerated by Bloom

* Tue Jul 20 2021 Rohan Agrawal <rohan@aleopile.com> - 0.13.0-1
- Autogenerated by Bloom

