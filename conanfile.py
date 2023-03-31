from conans import ConanFile, CMake, python_requires

build_tools = "sqpBuildTools/[~3.0]@tools/release"
sqp = python_requires(build_tools)

class LibsqpSpiSlaveLinuxConan(ConanFile):
    name = "libsqpSpiSlaveLinux"
    version = sqp.get_version()
    sqp.git_information()
    license = "proprietary"
    author = "swissQprint software@swissqprint.com"
    url = "www.swissqprint.com"
    description = "The libsqpSpiSlaveLinux includes the ioctl-definitions kernel- <-> userspace"
    # settings = "arch"
    # No settings/options are necessary, this is header only
    generators = "cmake_paths"
    build_requires = (build_tools)
    exports_sources = "spi-slave-dev.h", "CMakeLists.txt", "cmake/sqpSpiSlaveLinuxConfig.cmake.in"
    exports = "gitinfo.json"

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = "conan_paths.cmake"
        cmake.definitions.update(sqp.get_cmake_definitions(self.version))
        cmake.configure()
        return cmake

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

