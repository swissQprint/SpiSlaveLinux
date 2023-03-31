cmake_minimum_required(VERSION 3.12)

project(sqpSpiSlaveLinux VERSION 0.1.0.0)
#include(sqpTools)
#SQP_SetVersionInfo()

##############################################
# Create target
add_library(sqpSpiSlaveLinux INTERFACE)

#Set target properties
target_include_directories(sqpSpiSlaveLinux
    INTERFACE
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spi-slave-dev.h>
)

#Add an alias so that library can be used inside the build tree, e.g. when testing
add_library(sqpSpiSlaveLinux::sqpSpiSlaveLinux ALIAS sqpSpiSlaveLinux)

##############################################
# Installation instructions

include(GNUInstallDirs)
set(INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/cmake/sqpSpiSlaveLinux)

install(TARGETS sqpSpiSlaveLinux EXPORT sqpSpiSlaveLinux-targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(FILES "spi-slave-dev.h" DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

#Export the targets to a script
install(EXPORT sqpSpiSlaveLinux-targets
    DESTINATION ${INSTALL_CONFIGDIR}
    FILE sqpSpiSlaveLinuxTargets.cmake
    NAMESPACE sqpSpiSlaveLinux::
)

#Create a ConfigVersion.cmake file
include(CMakePackageConfigHelpers)
set(TEMP_CMAKE_SIZEOF_VOID_P ${CMAKE_SIZEOF_VOID_P})
unset(CMAKE_SIZEOF_VOID_P)
write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/sqpSpiSlaveLinuxConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)
set(CMAKE_SIZEOF_VOID_P ${TEMP_CMAKE_SIZEOF_VOID_P})

configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/cmake/sqpSpiSlaveLinuxConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/sqpSpiSlaveLinuxConfig.cmake
    INSTALL_DESTINATION ${INSTALL_CONFIGDIR}
)

#Install the config and configversion
install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/sqpSpiSlaveLinuxConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/sqpSpiSlaveLinuxConfigVersion.cmake
    DESTINATION ${INSTALL_CONFIGDIR}
)

