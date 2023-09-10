from typing import Any

from ..cmd import Command

extension_name_re: Any

def show_compilers() -> None: ...

class build_ext(Command):
    description: str
    sep_by: Any
    user_options: Any
    boolean_options: Any
    help_options: Any
    extensions: Any
    build_lib: Any
    plat_name: Any
    build_temp: Any
    inplace: int
    package: Any
    include_dirs: Any
    define: Any
    undef: Any
    libraries: Any
    library_dirs: Any
    rpath: Any
    link_objects: Any
    debug: Any
    force: Any
    compiler: Any
    swig: Any
    swig_cpp: Any
    swig_opts: Any
    user: Any
    parallel: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_extensions_list(self, extensions) -> None: ...
    def get_source_files(self): ...
    def get_outputs(self): ...
    def build_extensions(self) -> None: ...
    def build_extension(self, ext) -> None: ...
    def swig_sources(self, sources, extension): ...
    def find_swig(self): ...
    def get_ext_fullpath(self, ext_name: str) -> str: ...
    def get_ext_fullname(self, ext_name: str) -> str: ...
    def get_ext_filename(self, ext_name: str) -> str: ...
    def get_export_symbols(self, ext): ...
    def get_libraries(self, ext): ...
