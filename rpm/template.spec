Name:           ros-hydro-uwsim-osgocean
Version:        1.0.3
Release:        1%{?dist}
Summary:        ROS uwsim_osgocean package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

Requires:       OpenSceneGraph
Requires:       OpenSceneGraph-devel
Requires:       OpenThreads
Requires:       OpenThreads-devel
Requires:       boost-devel
Requires:       fftw
Requires:       fftw-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ros-hydro-catkin
BuildRequires:  OpenSceneGraph
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  OpenThreads
BuildRequires:  OpenThreads-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fftw
BuildRequires:  fftw-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel

%description
The OSG Ocean library adapted to UWSim. See https://code.google.com/p/osgocean

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Feb 05 2015 Mario Prats <marioprats@gmail.com> - 1.0.3-1
- Autogenerated by Bloom

* Thu Jan 15 2015 Mario Prats <marioprats@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

